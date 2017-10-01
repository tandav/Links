# ORM
- orm is antipttern
- [HN Search powered by Algolia](https://hn.algolia.com/?query=ORM&sort=byPopularity&prefix=false&page=0&dateRange=all&type=story)
- [ORM is an anti pattern · brettwooldridge/SansOrm Wiki](https://github.com/brettwooldridge/SansOrm/wiki/ORM-is-an-anti-pattern)
- [Object-relational impedance mismatch - Wikipedia](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch)

---

- Instead of using relational stores and ORM for everything, think more carefully about your design
- If your data is object in nature, then use object stores ("NoSQL"). They'll be much faster than a relational database.
- If your data is relational in nature, the overhead of a relational database is worth it.

---


## JDBC vs Hibernate
- JDBC - более low lev. Нужно все вручную делать. 
- Hibernate - hi-lev (easier, simpler, faster to start). JPA=guidelines, Hibernate implements JPA guidelines
