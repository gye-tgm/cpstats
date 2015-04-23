from sqlalchemy import create_engine

# todo: we can also enter another URL for postgresql 
# todo: change sqlite to psql sometime
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 

Base = declarative_base()

# We are going to define our own classes and map those to tables. We get
# supported by a system also known as Declarative. 

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)

  def __repr__(self):
    return 'User<%s, %s>' % (self.id, self.name)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
# There is also an option to set the engine later on with
# .configure(bind=engine). 
# With Base.metadata.create_all(engine) we can create the database. 
# This Session "object" servers as a custom made factory with we can create
# other sesion objects like session = Session()

session = Session()
tourist = User(name='Gennady')
session.add(tourist)

# at this point the instance is pending. there must be a flush for the permanent
# persistance, however, if we query for the database now, the flush also occurs. 

user = session.query(User).filter_by(name='Gennady').first()
print(user)
print(user is tourist)
# returns True

# get session.new (which users are pending?)
# get session.dirty (something has changed?) 
# they get empty if we do session.commit()
# we cann rollback a session with session.rollback()

for name in session.query(User.name).order_by(User.name):
  print(name)

# we can also user filters (no, not the instagramm filters)
# for EQUALS, NOT EQUALS, LIKE, IN, NOT IN, IS NULL, IS NOT NULL
# AND, OR, MATCH, ...

# From a query object
# .all() returns a list
# .first() applies a limit of one and returns the first object
# .one() fully fetches all rows: if there is not exactly one result returned
# then it raises an error like MultipleResultsFound or NoResultFound. Apparently
# convenient.

# We can use literal strings by calling text().
# This can include text("id<224") which just means that it should accept all
# rows fulfilling the id<224 condition. 
# One can actually write full raw SQL queries with text().
# One can also use prepared statements with from_statement()

# Use .count() the get the count as an integer. 
# Basically this tutorial gets your alive through the FT Matura. 
# http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html#building-a-relationship

# Association http://docs.sqlalchemy.org/en/latest/_modules/examples/association/basic_association.html
