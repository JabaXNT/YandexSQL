from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = StringField('id Лидера')
    work_size = StringField('Время выполнения', validators=[DataRequired()])
    job = TextAreaField("Работа", validators=[DataRequired()])
    is_finished = BooleanField("Сделана ли работа?")
    collaborators = StringField('id помощников', validators=[DataRequired()])
    submit = SubmitField('Применить')