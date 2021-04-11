from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from flask import Flask, abort, jsonify
from flask_restful import reqparse, abort, Api, Resource
from data.jobs import Jobs


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('team_leader', required=True)
parser.add_argument('job', required=True, type=str)
parser.add_argument('collaborators', required=True, type=str)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('is_finished', required=True, type=bool)


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({'jobs': jobs.to_dict(
            only=('id', 'job', 'team_leader', 'work_size', 'collaborators', 'is_finished'))})

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})
    
    def post(self, jobs_id):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        jobs = Jobs(
        id=jobs_id,
        team_leader=args['team_leader'],
        job=args['job'],
        collaborators=args['collaborators'],
        work_size=args['work_size'],
        is_finished=args['is_finished'],
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify(
            {
                'jobs':
                [item.to_dict(only=('id', 'job', 'team_leader', 'work_size', 'collaborators', 'is_finished'))
                 for item in jobs]
            }
        )

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
        id=args['id'],
        team_leader=args['team_leader'],
        job=args['job'],
        collaborators=args['collaborators'],
        work_size=args['work_size'],
        is_finished=args['is_finished'],
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"Job {jobs_id} not found")
