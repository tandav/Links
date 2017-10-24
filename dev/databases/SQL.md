# SQL
- SQL interview questions
- SQL joins, all about it (7 from pic + natural, theta, semi)
    - [When to use SQL natural join instead of join .. on? - Stack Overflow](https://stackoverflow.com/questions/10510952/when-to-use-sql-natural-join-instead-of-join-on)
    - [sql - is NATURAL JOIN any better than SELECT FROM WHERE in terms of performance? - Stack Overflow](https://stackoverflow.com/questions/3063107/is-natural-join-any-better-than-select-from-where-in-terms-of-performance): `highly recommended against NATURAL JOIN in production...just use INNER JOIN and specify the columns.`
    - left join vs left outer join (they're equal `OUTER` is optional)
- [SQL for Web Nerds](http://philip.greenspun.com/sql/)
- [sql - Inner join vs Where - Stack Overflow](https://stackoverflow.com/questions/121631/inner-join-vs-where)
- sql cheat sheet | quick sql tutorial
    - [SQL (Structured Query Language) in one page : SQL.SU](http://www.cheat-sheets.org/sites/sql.su/)
- sql exercises | sql exercises and answers
- varchar vs text
- awesome sql
- [Почему SQL одерживает верх над NoSQL, и к чему это приведет в будущем / Блог компании Alconost / Хабрахабр](https://habrahabr.ru/company/alconost/blog/340372/)
- [SQL vs NoSQL - HN Search](https://hn.algolia.com/?query=sql%20vs%20nosql&sort=byPopularity&prefix&page=0&dateRange=all&type=story)
- [Курс молодого бойца PostgreSQL / Хабрахабр](https://habrahabr.ru/post/340460/)

## Joins
- `JOIN` is the same as `INNER JOIN` use last one for readability
- `LEFT JOIN` is the same as `LEFT OUTER JOIN` 
    - [tsql - LEFT JOIN vs. LEFT OUTER JOIN in SQL Server - Stack Overflow](https://stackoverflow.com/questions/406294/left-join-vs-left-outer-join-in-sql-server)
- you can always use `LEFT JOIN`. If you need `RIGHT` just change the tables order.
- cross join (`SELECT * FROM student_grades, students`) - all different combinations


## Deep
- [Why Uber Engineering Switched from Postgres to MySQL | Hacker News](https://news.ycombinator.com/item?id=12166585)
- postgresql vs oracle
- [PostgreSQL command line cheatsheet](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)
- [My simply MySQL Command Line Cheatsheet](https://gist.github.com/hofmannsven/9164408)
- [Useful PostgreSQL Queries and Commands](https://gist.github.com/rgreenjr/3637525)
- oracle sql performance tips
- sql query tuning
- oracle tuning
- [query optimiz - HN Search](https://hn.algolia.com/?query=query%20optimiz&sort=byPopularity&prefix&page=0&dateRange=all&type=story)
