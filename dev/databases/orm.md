# ORM
- orm is antipttern
- [ORM - HN Search powered by Algolia](https://hn.algolia.com/?query=ORM&sort=byPopularity&prefix=false&page=0&dateRange=all&type=story)
- [The case against ORMs](http://korban.net/posts/postgres/2017-11-02-the-case-against-orms)
- [ORM is an anti pattern · brettwooldridge/SansOrm Wiki](https://github.com/brettwooldridge/SansOrm/wiki/ORM-is-an-anti-pattern)
- [Object-relational impedance mismatch - Wikipedia](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch)
- [Taking a step back from ORMs | Experimental Thoughts](http://thoughts.davisjeff.com/2012/02/26/taking-a-step-back-from-orms/)
- [OrmHate](https://martinfowler.com/bliki/OrmHate.html)
- [Why I hate Hibernate (and ORMs in general) (2015) | Hacker News](https://news.ycombinator.com/item?id=15716860)

---

- Instead of using relational stores and ORM for everything, think more carefully about your design
- If your data is object in nature, then use object stores ("NoSQL"). They'll be much faster than a relational database.
- If your data is relational in nature, the overhead of a relational database is worth it.

---

## JDBC vs Hibernate vs JPA
- JDBC - более low lev. Нужно все вручную делать. 
- Hibernate - hi-lev (easier, simpler, faster to start). JPA=guidelines, Hibernate implements JPA guidelines
- jpa vs jdbc
- [java - JPA or JDBC, how are they different? - Stack Overflow](https://stackoverflow.com/questions/11881548/jpa-or-jdbc-how-are-they-different)
- [java - Hibernate or JPA or JDBC or? - Stack Overflow](https://stackoverflow.com/questions/2560500/hibernate-or-jpa-or-jdbc-or)
