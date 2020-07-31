-- user presence
SELECT xlogin, workplace, datetime(date_time, 'unixepoch', 'localtime') dt
FROM seat s
WHERE xlogin LIKE 'ama%'
ORDER BY date_time DESC;

-- User seat by day and seat

SELECT DISTINCT xlogin, workplace, strftime('%Y-%m-%d', date_time, 'unixepoch', 'localtime') dt
FROM seat s
WHERE xlogin LIKE 'kba%'
ORDER BY date_time DESC;

SELECT DISTINCT xlogin
FROM seat
ORDER BY xlogin;

--
SELECT datetime((SELECT date_time FROM seat), 'unixepoch', 'localtime');

-- Example
SELECT workplace, xlogin, strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') date_time
FROM seat
ORDER BY date_time DESC;

-- Presences
-- from
-- t0
-- xlogin
-- ?? Today
SELECT COUNT(*)
FROM (
         SELECT workplace, xlogin
         FROM seat
         WHERE date(date_time) >= date('now', '-1 days')
     );

-- Working
SELECT workplace, xlogin, dt date_time
FROM (
         SELECT *, strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') dt FROM seat
     )
WHERE dt >= date('now', '-0 day')
  AND dt < date('now', '+1 day');

SELECT datetime(1595970000.886688, 'unixepoch');

SELECT workplace, strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') dt
FROM seat
WHERE datetime(date_time, 'unixepoch') >= date('now', '-1 days')
  AND datetime(date_time, 'unixepoch') < date('now', '+1 days')
  AND xlogin LIKE 'ama%';

-- From/to

SELECT workplace, xlogin, strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') dt
FROM seat
WHERE strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') >= '2020-07-31 00-00-00'
  AND strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') < '2020-07-31 23-00-00'
  AND xlogin LIKE '%ama%'
ORDER BY date_time;

SELECT workplace, strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') date_time
FROM seat
WHERE strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') >= '2020-07-31 00-00-00'
  AND strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') < '2020-07-31 23-00-00'
  AND xlogin LIKE '%ama%'
ORDER BY date_time;
