"""
A report tool for news log
"""

from newsdb import get_most_popular_articles, get_most_popular_authors



if __name__ == '__main__':
    get_most_popular_articles(2)
    get_most_popular_authors(4)
