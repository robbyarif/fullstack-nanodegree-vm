
"""
Database API codes for DB News.
"""

import datetime
import psycopg2

def get_most_popular_articles(number):
    """Return all posts from the 'database', most recent first."""
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    print("%s" % str(number))
    query = """SELECT title, COUNT(log.path) as views
        FROM articles
        LEFT JOIN log ON path LIKE '%'||slug
        GROUP BY title
        ORDER BY views DESC
        LIMIT {}""".format(number)
    print (query)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    print(rows)
    return rows

def get_most_popular_authors(number):
    """Add a post to the 'database' with the current timestamp."""
    # conn = psycopg2.connect("dbname=news")
    # cur = conn.cursor()
    # cur.execute("""INSERT INTO posts VALUES (%s) """, (number,))
    # conn.commit()
    # conn.close()
    print('hello world no author listed yet WIP %s' % number)
