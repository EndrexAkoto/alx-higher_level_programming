-- Connect to the appropriate database
USE hbtn_0c_0;

-- Calculate the average temperature in Fahrenheit for each city
SELECT city, AVG(temp) AS avg_temp
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;

