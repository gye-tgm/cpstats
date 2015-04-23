from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    uname = Column(String)
    created_tasks = relationship("Task", backref="user")
    accounts = relationship("Account", backref="user")
    achievements = relationship("Achievement", backref="user")

    def __repr__(self):
        return 'User<%d, "%s">' % (self.id, self.uname)


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    handle = Column(String)
    url = Column(String, unique=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    oj_id = Column(Integer, ForeignKey('oj.id'))

    discriminator = Column(String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}


class RatedAccount(Account):
    __tablename__ = 'rated_account'
    __mapper_args__ = {'polymorphic_identity': 'rated_account'}

    id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    rating = Column(Integer, primary_key=True)


class CodeforcesAccount(RatedAccount):
    __tablename__ = 'cfaccount'
    __mapper_args__ = {'polymorphic_identity': 'cf_account',}
    id = Column(Integer, ForeignKey('rated_account.id'), primary_key=True)
    contribution = Column(Integer, primary_key=True)


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    oj_id = Column(Integer, ForeignKey('oj.id'))


class OnlineJudge(Base):
    __tablename__ = 'oj'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    url = Column(String, unique=True)
    problemset = relationship("Task", backref='oj')


class Submission(Base):
    __tablename__ = 'submission'
    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('task.id'), primary_key=True)
    verdict = Column(Integer)
    language = Column(String)



class Achievement(Base):
    __tablename__ = 'achievement'
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)


class Participation(Base):
    __tablename__ = 'participation'
    id = Column(Integer, primary_key=True)


engine = create_engine('sqlite:///test.db', echo=False)
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
