### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
Postgres is a SQL based database that allows programmers to store, retrieve, and manage data within a structured framework. 

- What is the difference between SQL and PostgreSQL?
SQL is the structured querying language whereas PostgreSQL is an instance and medium where SQL can be written to manage databases.

- In `psql`, how do you connect to a database?
You enter in the command as such `psql -h <hostname> -p <port> -U <yourusername> <yourdatabase_name>

- What is the difference between `HAVING` and `WHERE`?
The 'WHERE' statement is used to filter out rows returned by the query whereas 'HAVING' is used to filter out groups of rows from a specific query.

- What is the difference between an `INNER` and `OUTER` join?
An 'INNER' join will combine two or more tables by a common column whereas 'OUTER' carries the same process but also returns rows that do not have matching values in both tables.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
`LEFT OUTER` join returns rows from the left table even when there are no present matching values in the right table. `RIGHT JOIN` essentially does the same thing but vice versa.

- What is an ORM? What do they do?
Is a programming technique that allows users to manage data, especially via CRUD operations, with databases from an OOP language.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  AJAX requests are utilized to make HTTP requests from a web page without reloading it whereas server-side libraries such as 'requests' are used to make synchronous requests like fetching or sending emails.

- What is CSRF? What is the purpose of the CSRF token?
CSRF is a web attack vulnerability used by cyber criminals to take over someone's account by allowing the victim to carry out an action such as changing a password, updating an email, etc. unknowingly and unwillingly. 

- What is the purpose of `form.hidden_tag()`?
The  `form.hidden_tag()` is utilized from Flask-WTF to generate a hidden input field. It is used to pass hidden data to a server without the user's knowledge. Typically it's meant to store a user's ID or a session token. 
