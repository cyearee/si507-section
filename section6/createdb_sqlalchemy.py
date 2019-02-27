# what do we import?
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
import sqlalchemy as db
import json

#### from db.py - basically setting up connection to database and building the base to translate all ORM-speak to SQL commands behind-the-scenes ####

Base = declarative_base() # Set up base

session = scoped_session(sessionmaker()) 

engine = create_engine('sqlite:///twitter_sqlalchemy.sqlite', echo=False) # You might also have a config file, for example, that holds the string that is the db name. For now we'll just put it here.

# Now, bind the engine to the metadata of the Base class so that the declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
session.configure(bind=engine)

def init_db():
    # Drop all tables in the engine if needed for initialization. This is equivalent to "Delete Table" statements in raw SQL.
    # We'll leave this commented out initially, but if you wanted to drop everythign and 'reset' it every time, you might uncomment this.
    # Base.metadata.drop_all(engine)

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    # But, this won't overwrite existing tables -- it will simply create new ones if necessary.
    Base.metadata.create_all(engine)
    return engine

#### end db.py ####

#### creating the classes that will be translated to entities/tables ####

class Tweeter(Base):
    __tablename__ = 'tweeter' # special variable useful for referencing in other/later code
    # Here we define columns for the table
    # Notice that each column is also basically a class variable
    tweeter_id = Column(Integer, primary_key=True, autoincrement=True) # autoincrements by default
    tweeter_name = Column(String(250), nullable=False) # The way we write types in SQLAlchemy is different from SQLite specifically -- and more like Python!

# what about the Tweet class?

class Tweet(Base):
	__tablename__ = 'tweet'
	tweet_id = Column(Integer,primary_key=True)
	tweeter_id = Column(Integer,ForeignKey('tweeter.tweeter_id'))
	content = Column(String(280))
	num_replies = Column(Integer)
	num_likes = Column(Integer)
	num_retweets = Column(Integer)
	tweeter = relationship('Tweeter')

#### end entities ####

#### FINALLY let's insert some data by creating instances ####

init_db()

# from before - loading json data
file = open('tweety.json','r')
listodicts = json.loads(file.read())
file.close()
unique_tweeters = []
for d in listodicts:
    if d['tweeter'] not in unique_tweeters:
        unique_tweeters.append(d['tweeter'])
    #     tweeter_row = Tweeter(tweeter_name=d['tweeter'])
    #     session.add(tweeter_row)
    #     tweet_row = Tweet(tweet_id=d['id'],tweeter=tweeter_row,content=d['content'],num_replies=d['replies'],num_likes=d['likes'],num_retweets=d['retweets'])
    #     session.add(tweet_row)
    # else:
    #     tweeter_row = Tweeter(tweeter_name=d['tweeter'])
    #     tweet_row = Tweet(tweet_id=d['id'],tweeter=tweeter_row,content=d['content'],num_replies=d['replies'],num_likes=d['likes'],num_retweets=d['retweets'])
    #     session.add(tweet_row)

# create and add instances of tweeters
for item in unique_tweeters:
    row = Tweeter(tweeter_name=item)
    session.add(row)
    session.commit()

for item in listodicts:
	# another = Tweeter(tweeter_name=item['tweeter'])
	# session.add(another)
	# session.flush()
	row = Tweet(tweet_id=item['id'],tweeter_id=session.query(Tweeter.tweeter_id).filter(Tweeter.tweeter_name==item['tweeter']),content=item['content'],num_replies=item['replies'],num_likes=item['likes'],num_retweets=item['retweets'])
	session.add(row)
session.commit()