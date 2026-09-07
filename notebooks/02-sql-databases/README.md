# 02 — SQL Databases

SQL is how you ask questions of data once it stops fitting into one clean spreadsheet. Most of this unit is the same small set of moves over and over: pick columns, keep some rows, group them, count them, sort them, and sometimes join one table to another.

This is not every SQL feature. It is the stuff you will actually use.

---

## The basic shape

Most queries follow this order:

```sql
SELECT ...
FROM ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
LIMIT ...
```

You write it in that order, but the database thinks about it more like:

```text
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
```

That explains a lot of weird errors. A name you make in `SELECT` does not exist yet when `WHERE` runs.

---

## Start by looking around

Before writing a real query, check what is actually in the database.

```sql
SELECT name
FROM sqlite_master
WHERE type = 'table';
```

```sql
PRAGMA table_info(tracks);
```

Use those two constantly. Guessing column names is a waste of time.

---

## Get rows back

All columns:

```sql
SELECT *
FROM tracks;
```

Some columns:

```sql
SELECT title, genre, seconds
FROM tracks;
```

Rename a column in the output:

```sql
SELECT title, seconds / 60.0 AS minutes
FROM tracks;
```

Remove duplicates:

```sql
SELECT DISTINCT genre
FROM tracks;
```

---

## Filter rows with `WHERE`

Equals / not equals:

```sql
SELECT *
FROM tracks
WHERE genre = 'Pop';
```

```sql
SELECT *
FROM tracks
WHERE genre != 'Pop';
```

Numeric comparisons:

```sql
SELECT *
FROM tracks
WHERE seconds > 200;
```

Ranges:

```sql
SELECT *
FROM tracks
WHERE seconds BETWEEN 180 AND 240;
```

Sets:

```sql
SELECT *
FROM tracks
WHERE genre IN ('Pop', 'Folk');
```

Text patterns:

```sql
SELECT *
FROM tracks
WHERE title LIKE '%line%';
```

`%` means "any number of characters." `_` means "one character."

Combine conditions:

```sql
SELECT *
FROM tracks
WHERE genre = 'Pop'
  AND seconds > 200;
```

```sql
SELECT *
FROM tracks
WHERE genre = 'Pop'
   OR genre = 'Folk';
```

---

## Sort and limit

Sort ascending:

```sql
SELECT title, seconds
FROM tracks
ORDER BY seconds;
```

Sort descending:

```sql
SELECT title, seconds
FROM tracks
ORDER BY seconds DESC;
```

Top 5:

```sql
SELECT title, seconds
FROM tracks
ORDER BY seconds DESC
LIMIT 5;
```

---

## `NULL` is not zero and not blank

This does **not** work:

```sql
SELECT *
FROM tracks
WHERE genre = NULL;
```

Use:

```sql
SELECT *
FROM tracks
WHERE genre IS NULL;
```

And:

```sql
SELECT *
FROM tracks
WHERE genre IS NOT NULL;
```

If you write `genre != 'Pop'`, rows where `genre` is `NULL` are not kept. If you want them too, say so.

```sql
SELECT *
FROM tracks
WHERE genre != 'Pop'
   OR genre IS NULL;
```

---

## Count, average, sum, min, max

Common aggregate functions:

- `COUNT(*)`
- `COUNT(column)`
- `COUNT(DISTINCT column)`
- `AVG(column)`
- `SUM(column)`
- `MIN(column)`
- `MAX(column)`

Examples:

```sql
SELECT COUNT(*) AS total_tracks
FROM tracks;
```

```sql
SELECT AVG(seconds) AS avg_length
FROM tracks;
```

```sql
SELECT COUNT(DISTINCT user) AS listeners
FROM plays;
```

Important distinction:

- `COUNT(*)` counts rows
- `COUNT(genre)` counts non-null `genre` values
- `COUNT(DISTINCT genre)` counts unique non-null genres

---

## Group rows with `GROUP BY`

Count tracks by genre:

```sql
SELECT genre, COUNT(*) AS n
FROM tracks
GROUP BY genre;
```

Average length by genre:

```sql
SELECT genre, AVG(seconds) AS avg_seconds
FROM tracks
GROUP BY genre
ORDER BY avg_seconds DESC;
```

Rule: if a column is in `SELECT` and it is not wrapped in an aggregate function, it usually needs to be in `GROUP BY`.

---

## `HAVING` is for groups

Use `WHERE` before grouping. Use `HAVING` after grouping.

This is the pattern:

```sql
SELECT track_id, COUNT(*) AS plays
FROM plays
GROUP BY track_id
HAVING COUNT(*) >= 2;
```

If the condition uses `COUNT`, `AVG`, `SUM`, or another aggregate, it usually belongs in `HAVING`, not `WHERE`.

---

## Join tables

The real point of a database is that related facts live in different tables.

Inner join:

```sql
SELECT t.title, a.name
FROM tracks AS t
JOIN artists AS a
  ON t.artist_id = a.artist_id;
```

That keeps only rows where the match exists in both tables.

Left join:

```sql
SELECT t.title, a.name
FROM tracks AS t
LEFT JOIN artists AS a
  ON t.artist_id = a.artist_id;
```

That keeps every row from the left table even if the match is missing.

Common pattern: count plays by artist.

```sql
SELECT a.name, COUNT(*) AS plays
FROM plays AS p
JOIN tracks AS t
  ON p.track_id = t.track_id
JOIN artists AS a
  ON t.artist_id = a.artist_id
GROUP BY a.name
ORDER BY plays DESC;
```

---

## Aliases make queries readable

Temporary shorter names:

```sql
SELECT t.title, a.name
FROM tracks AS t
JOIN artists AS a
  ON t.artist_id = a.artist_id;
```

Temporary output names:

```sql
SELECT AVG(seconds) AS avg_seconds
FROM tracks;
```

Use aliases when the full names make the query harder to read, not because SQL said you had to.

---

## `CASE WHEN` for categories

Build a label inside a query:

```sql
SELECT title,
       CASE
         WHEN seconds < 180 THEN 'short'
         WHEN seconds <= 240 THEN 'medium'
         ELSE 'long'
       END AS length_bucket
FROM tracks;
```

This is useful when the raw column is not in the shape you want to report.

---

## Handy patterns

Top values:

```sql
SELECT title, seconds
FROM tracks
ORDER BY seconds DESC
LIMIT 3;
```

How many rows per group:

```sql
SELECT genre, COUNT(*) AS n
FROM tracks
GROUP BY genre
ORDER BY n DESC;
```

Unique values in a column:

```sql
SELECT DISTINCT genre
FROM tracks
ORDER BY genre;
```

Find missing values:

```sql
SELECT *
FROM tracks
WHERE genre IS NULL;
```

Rows with no match after a left join:

```sql
SELECT t.*
FROM tracks AS t
LEFT JOIN artists AS a
  ON t.artist_id = a.artist_id
WHERE a.artist_id IS NULL;
```

Count unique people instead of total events:

```sql
SELECT COUNT(DISTINCT user)
FROM plays;
```

---

## Mistakes you will make once

- `=` with `NULL` instead of `IS NULL`
- putting an aggregate condition in `WHERE` instead of `HAVING`
- forgetting that `COUNT(column)` ignores nulls
- sorting ascending when you meant `DESC`
- joining on the wrong key
- writing a query before checking the actual column names

If the result looks wrong, simplify the query and test one piece at a time.

---

## SQLite notes

These notebooks use SQLite, which is a little forgiving and a little weird:

- text matching with `LIKE` is often case-insensitive for plain ASCII
- dates are often stored as text unless you convert them yourself
- `LIMIT` works the way you expect
- `PRAGMA table_info(...)` is your friend

---

## One good workflow

1. Check the tables.
2. Check the columns.
3. Write the smallest possible `SELECT`.
4. Add `WHERE`.
5. Add `GROUP BY` only if you need summary numbers.
6. Add `ORDER BY` and `LIMIT` last.

If a query stops making sense, strip it back to the last version that worked.
