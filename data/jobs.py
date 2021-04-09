import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm



class Jobs(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    user = orm.relation('User')

    def __repr__(self):
        return f"{self.id} {self.job} {self.work_size} {self.collaborators} \
{self.speciality} {self.end_date} {self.start_date} {self.is_finished}"
