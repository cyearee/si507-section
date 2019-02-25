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
# c.execute(create_tweeter_query)

# What about the tweet table?

# create_tweet_query = ''''''
# c.execute(create_tweet_query)

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

conn.commit()
conn.close()