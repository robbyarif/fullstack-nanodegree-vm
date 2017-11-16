"""
A report tool for news log
"""

from newsdb import (get_most_popular_articles,
                    get_most_popular_authors,
                    get_days_with_error_rate)



if __name__ == '__main__':
    get_most_popular_articles(2)
    get_most_popular_authors(4)
    get_days_with_error_rate(0.01)
