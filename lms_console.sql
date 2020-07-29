-- user presence
SELECT xlogin, workplace, datetime(date_time, 'unixepoch', 'localtime') dt
FROM seat s
WHERE xlogin LIKE 'ama%'
ORDER BY date_time DESC;

-- User seat by day and seat

SELECT DISTINCT xlogin, workplace, strftime('%Y-%m-%d', date_time, 'unixepoch', 'localtime') dt
FROM seat s
WHERE xlogin LIKE 'iss%'
ORDER BY date_time DESC;

SELECT DISTINCT xlogin FROM seat ORDER BY xlogin;

--
SELECT datetime((SELECT date_time FROM seat), 'unixepoch', 'localtime');

-- Example
SELECT workplace, xlogin, strftime('%Y-%m-%d %H-%M-%S', date_time, 'unixepoch', 'localtime') date_time
FROM seat
ORDER BY date_time DESC;
