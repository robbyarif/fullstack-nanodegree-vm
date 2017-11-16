
"""
 "Database code" for the DB Forum.
"""

import datetime
import psycopg2

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
    """Return all posts from the 'database', most recent first."""
    conn = psycopg2.connect("dbname=forum")
    cur = conn.cursor()
    cur.execute("""SELECT content, time FROM posts ORDER BY time DESC""")
    rows = cur.fetchall()
    return rows

def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    conn = psycopg2.connect("dbname=forum")
    cur = conn.cursor()
    cur.execute("""INSERT INTO posts VALUES ('%s', DEFAULT) """ % (content))
    conn.commit()
    # POSTS.append((content, datetime.datetime.now()))
