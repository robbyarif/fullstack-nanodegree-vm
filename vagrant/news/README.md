News Log Analysis Project
=============
A reporting tool that prints out reports (in plain text) based on the data in the database. This tool will report:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Prerequisite
This project is based on [Udacity Fullstack Nanodegree VM](https://github.com/udacity/fullstack-nanodegree-vm.git) using Python and PostgreSQL.

Sample data can be downloaded [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Then run
```
 psql -d news -f newsdata.sql
```

## How to Use
- Open terminal
- Run `python news.py`
- A report will be printed in console

For example
```
$ python news.py
$ Most Popular Three Articles of All Time
$ 
```

## License
The MIT License (MIT)
[MIT License](https://opensource.org/licenses/MIT)
