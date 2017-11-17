#!usr/bin/python


"""
A reporting tool that prints out reports (in plain text) based on the data
in the database.
"""

import psycopg2


def get_most_popular_articles():
    """Return three most popular articles from news log."""
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    query = """SELECT title, COUNT(log.path) as views
        FROM articles
        LEFT JOIN log ON path LIKE '%'||slug
        GROUP BY title
        ORDER BY views DESC
        LIMIT 3"""
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_most_popular_authors():
    """Return author name and number of views of the most popular authors from
    news log ordered from highest views."""
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    query = """
    SELECT name, COUNT(log.path) as views
        FROM authors
        LEFT JOIN articles ON author = authors.id
        LEFT JOIN log ON path LIKE '%'||slug
        GROUP BY name
        ORDER BY views DESC"""
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_days_with_error_rate():
    """Return the date and the error rate of the day with the most error
    ordered from the highest error rate."""
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    query = """
    SELECT to_char(day,'DD Mon YYYY') as day, errorrate from (
        SELECT  date_trunc('day',time) as day,
                ROUND( 100 *
                    SUM(CASE WHEN status = '404 NOT FOUND'
                    THEN 1 ELSE 0 END)::numeric
                    / COUNT(*), 2) as errorrate
        FROM log GROUP BY day ORDER BY day
    ) as statistics
    WHERE errorrate > 1"""
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':

    print("Three Most Popular Articles of All Time")
    articles = get_most_popular_articles()
    for article in articles:
        print("- ""{}"" - {} views".format(article[0], article[1]))

    print("\nMost Popular Article Authors of All Time")
    authors = get_most_popular_authors()
    for author in authors:
        print("- {} - {} views".format(author[0], author[1]))

    print("\nDays with Error Rate More Than 1%")
    days = get_days_with_error_rate()
    for day in days:
        print("- {} - {}% errors".format(day[0], day[1]))
