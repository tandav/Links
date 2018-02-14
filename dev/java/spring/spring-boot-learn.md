# Learning Spring Boot
`by reading Spring Boot in Action`

---

Spring Boot automation is by:
- starter dependencies
- automatic configuration

---

starter deps: add to pom / also can select in initialzr

---

some learning-app:
- Spring MVC to handle web requests
- Thymeleaf to define web views (i'll use React)
- Spring Data JPA to persist the reading selections to a database. For now, that database will be an embedded H2 database.
    - I need MySQL

---

- `@SpringBootApplication` `==`:
    - `@Configuration`
    - `@ComponentScan`
    - `@EnableAutoConfiguration`

---

use spring boot maven plugin and and parent starter

`mvn spring-boot:run`

able to package the project as an executable uber-JAR. This includes packing all of the application’s dependencies within the JAR and adding a manifest to the JAR with entries that make it possible to run the application with `java -jar`.


notice that the Maven build in listing 2.4 has “spring-boot-starter-parent” as a parent. By rooting the project in the parent starter, the build can take advantage of Maven dependency management to inherit dependency versions for several commonly used libraries so that you don’t have to explicitly specify the versions when declaring dependencies. Notice that none of the `<dependency>` entries in this pom.xml file specify any versions.

---

## starter dependencies
Spring Boot starter dependencies offer a bit of build-time magic for Spring Boot applications.

- w/o starter dependencies you have to worry about:
    - What kind of dependencies would you add to your build without Spring Boot? 
    - Which Spring dependencies do you need to support Spring MVC? 
    - Do you remember the group and artifact IDs for Thymeleaf? 
    - Which ver- sion of Spring Data JPA should you use? 
    - Are all of these compatible?

A starter dependency is essentially a Maven POM that defines transitive dependencies on other libraries that together provide support for some functionality.

there are list of all avalible starters

you can selectively override transitive dependency versions, exclude transitive dependencies, and certainly specify dependencies for libraries not covered by Spring Boot starters.

---

## automatic configuration
checks what's dependencies are on classpath do some magic configuration. Auto-configuration's purpose is to keep you from having to explicitly write configuration unless absolutely necessary.

- объявляешь enteties @Entity
- делаешь repo / хранилище / DB /
    - нужно просто объявить интерфейс который еще extends JpaRepository / crudRepository
    - `<Book, Long> <the domain type that the repository will work with, and the type of its ID property>`
    - имплементить не надо все само через spring-boot-magic
    - кроме стандартных крудовских / jpa / (18 штук) можно добавить кастомные методы которые юзать будешь, eg `findByReader()`
        - Spring Data JPA also allows you to define other query methods by simply declaring their method signature. In the case of CustomerRepository, this is shown with a findByLastName() method.
        - [Getting Started · Accessing Data with JPA](https://spring.io/guides/gs/accessing-data-jpa/)
- create web interface (controllers / url / requests handlers)
    - короче описываются всякие фишечки `Controller` / `RequestMapping`
    - если че вернуться почитать `Spring Boot in Action page 40`
- описываются Thymeleaf-templates


### How auto-configuration work?
When you add Spring Boot to your application, there’s a JAR file named `spring-boot-autoconfigure` that contains several configuration classes. 

Every one of these configuration classes is available on the application’s classpath and has the opportunity to contribute to the configuration of your application.

There’s configuration for Thymeleaf,
configuration for Spring Data JPA,
configuration for Spring MVC,
and configuration for dozens of other things you might or might not want to take advantage of in your Spring application.

---

- description of conditional configuration
- how to write your own conditions in Spring

---

Good overview / explanation on example:

Why spring boot is following configuration decisions made by the conditionals in auto-configuration
- Because H2 is on the classpath: ... configuration is ...
- Because Hibernate Entity Manager is on the classpath (transitively via Spring Data JPA) ...
- Because Spring Data JPA is on the classpath ...
... 
(read full explanation in book)

---

## Chapter 2 Summary
Spring applications. Starter dependencies help you focus on the type of functionality your application needs rather than on the specific libraries and versions that provide that functionality. 

Meanwhile, auto-configuration frees you from the boilerplate configuration that is common among Spring applications without Spring Boot.

---

## Chapter 3 Customizing configuration
Most of the time, the auto-configured beans are exactly what you want and there’s no need to override them. But there are some cases where auto-configuration isn’t good enough 

e.g. applying security to your app. 

Security is not one-size-fits-all, and there are decisions around application security that Spring Boot has no business making for you. Although Spring Boot provides some basic auto-configuration for security to override.

---
