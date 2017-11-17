
"""
Database API codes for DB News.
"""

import psycopg2

def get_most_popular_articles(number):
    """Return title and number views of the most popular articles from news log ordered from the
     highest views."""
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    query = """SELECT title, COUNT(log.path) as views
        FROM articles
        LEFT JOIN log ON path LIKE '%'||slug
        GROUP BY title
        ORDER BY views DESC
        LIMIT {}""".format(number)
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    print(rows)
    return rows

def get_most_popular_authors(number):
    """Return author name and number of views of the most popular authors from news log ordered from
     highest views."""
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    query = """SELECT name, COUNT(log.path) as views
        FROM authors
        LEFT JOIN articles ON author = authors.id
        LEFT JOIN log ON path LIKE '%'||slug
        GROUP BY name
        ORDER BY views DESC
        LIMIT {}""".format(number)
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    print(rows)
    return rows

def get_days_with_error_rate(error_rate):
    """Return the date and the error rate of the day with the most error ordered from the highest
    error rate."""
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    query = """
    SELECT to_char(day,'DD Mon YYYY') as day, errorrate from (
        SELECT  date_trunc('day',time) as day, 
                ROUND( 100 * SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END)::numeric/COUNT(*),2) as errorrate
        FROM log GROUP BY day ORDER BY day
    ) as statistics
    WHERE errorrate > {}
    """.format(error_rate)
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    print(rows)
    return rows

