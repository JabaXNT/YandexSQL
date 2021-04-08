import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm



class Department(SqlAlchemyBase):
    __tablename__ = 'department'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    members = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"))
    email = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.email"), nullable=True)

    user = orm.relation('User')

    def __repr__(self):
        return f"{self.id} {self.job} {self.work_size} {self.collaborators} \
{self.speciality} {self.end_date} {self.start_date} {self.is_finished}"