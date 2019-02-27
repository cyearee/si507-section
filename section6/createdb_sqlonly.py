# What do we need to import?
import json
import sqlite3 as db

sqlite_file = 'twitter_sqlite3.sqlite'
conn = db.connect(sqlite_file)
c = conn.cursor()
# What do the above lines do?

# SQL queries to create entities/attributes
create_tweeter_query = '''CREATE TABLE tweeter(
  tweeter_id INTEGER PRIMARY KEY AUTOINCREMENT,
  tweeter_name TEXT)
  '''

# Now to execute the create_query...
c.execute(create_tweeter_query)

# What about the tweet table?

create_tweet_query = '''CREATE TABLE tweet(
	tweet_id INTEGER PRIMARY KEY NOT NULL,
	tweeter_id INTEGER,
	content TEXT,
	num_replies INTEGER,
	num_likes INTEGER,
	num_retweets INTEGER,
	CONSTRAINT fk_tweeter FOREIGN KEY (tweeter_id) REFERENCES tweeter(tweeter_id))'''
c.execute(create_tweet_query)

# access the data from the json file
file = open('tweety.json','r')
listodicts = json.loads(file.read())
file.close()
unique_tweeters = []
for d in listodicts:
	if d['tweeter'] not in unique_tweeters:
		unique_tweeters.append(d['tweeter'])
# print(unique_tweeters[0])

# insert data
for item in unique_tweeters:
	c.execute('''
		INSERT INTO tweeter(tweeter_name) 
		VALUES (?);
		''', (item,))

for t in listodicts:
	insertion = (t['id'],t['tweeter'],t['content'],t['replies'],t['likes'],t['retweets'])
	c.execute('''
		INSERT INTO tweet 
		VALUES(?,(SELECT tweeter_id FROM tweeter WHERE tweeter_name=?),?,?,?,?);''',insertion)

conn.commit() # don't forget to commit! otherwise you won't see any changes :p
conn.close()