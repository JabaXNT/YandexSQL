from data import db_session
from data.users import User
from data.jobs import Jobs
from data import jobs_resources
from data import user_resources
from forms.user import LoginForm
from forms.jobs import JobsForm
from forms.reg_user import RegisterForm
from flask import Flask, render_template, request, redirect, abort
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_restful import abort, Api
from flask_ngrok import run_with_ngrok
import os

app = Flask(__name__)
api = Api(app)
run_with_ngrok(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


api.add_resource(jobs_resources.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resources.JobsResource, '/api/v2/jobs/<int:jobs_id>')
api.add_resource(user_resources.UserListResource, '/api/v2/users')
api.add_resource(user_resources.UserResource, '/api/v2/users/<int:user_id>')


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/jobs', methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.team_leader = current_user.id
        jobs.job = form.job.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_finished.data
        if current_user.id == 1:
            jobs.team_leader = form.team_leader.data
        current_user.jobs.append(jobs)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Добавление новости',
                           form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.user == current_user
                                          ).first()
        if current_user.id == 1:
            jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs:
            if current_user.id == 1:
                jobs.team_leader = form.team_leader.data
            else:
                jobs.team_leader = current_user.id
            jobs.job = form.job.data
            jobs.is_finished = form.is_finished.data
            jobs.collaborators = form.collaborators.data
            jobs.work_size = form.work_size.data
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.user == current_user
                                          ).first()
        if current_user.id == 1:
            jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs or current_user.id == 1:
            jobs.team_leader = current_user.id
            jobs.job = form.job.data
            jobs.is_finished = form.is_finished.data
            jobs.collaborators = form.collaborators.data
            jobs.work_size = form.work_size.data
            if current_user.id == 1:
                jobs.team_leader = form.team_leader.data
                if db_sess.query(Jobs).filter(Jobs.id == jobs.team_leader).first() is None:
                    jobs.team_leader = 1
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      Jobs.user == current_user
                                      ).first()
    if jobs or current_user.id == 1:
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init('db/Mars_Cool.db')
    app.run()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
