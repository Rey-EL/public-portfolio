# SQL Filtering Lab

I used SQL to investigate security events in a simulated employee database. The exercise: write queries that find suspicious login activity and pull the right employee lists for admin work. Part of my Google Cybersecurity Certificate work.

## The queries

Failed logins after business hours. This is the first thing you check when you suspect unauthorized access:

```sql
SELECT * FROM log_in_attempts WHERE login_time > '18:00:00' AND success = 0;
```

All login activity on and around the day of an incident:

```sql
SELECT * FROM log_in_attempts WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';
```

Narrow the search by excluding a whole country:

```sql
SELECT * FROM log_in_attempts WHERE NOT country LIKE 'MEX%';
```

Find Marketing staff in East-building offices for a targeted update:

```sql
SELECT * FROM employees WHERE department = 'Marketing' AND office LIKE 'East-%';
```

Pull everyone in Finance or Sales:

```sql
SELECT * FROM employees WHERE department = 'Finance' OR department = 'Sales';
```

Everyone outside IT, for a phased rollout:

```sql
SELECT * FROM employees WHERE NOT department = 'Information Technology';
```

## What this shows

I can use `WHERE` clauses with `AND`, `OR`, and `NOT` to hunt for threats and answer real admin questions. Same skill, two jobs: find the bad logins, and get the right people list.

One habit worth naming: in production, user input never goes straight into a query string. Parameterized queries exist so input stays data and never becomes code.

## License

MIT License. See [LICENSE.md](LICENSE.md) for details.
