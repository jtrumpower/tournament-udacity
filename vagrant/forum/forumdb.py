#
# Database access functions for the web forum.
# 

import time
import psycopg2
import bleach

## Database connection
def getConnection():
	conn = psycopg2.connect("dbname=forum")
	return conn

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''

    db = getConnection()
    cursor = db.cursor()

    posts = cursor.execute("SELECT content, time from posts order by time desc")
    posts = ({'content': str(row[1]), 'time': str(row[0])} for row in cursor.fetchall())

    db.close()

    # posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
    # posts.sort(key=lambda row: row['time'], reverse=True)
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    #t = time.strftime('%c', time.localtime())
    db = getConnection()
    cursor = db.cursor()

    cursor.execute("INSERT into posts (content) VALUES (%s)", (bleach.clean(content),))

    db.commit()
    db.close()