-- Connect to the appropriate database
USE hbtn_0c_0;
-- Display the top 3 cities' temperatures during July and August
SELECT city, AVG(temp) AS avg_temp
FROM temperature_data
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

