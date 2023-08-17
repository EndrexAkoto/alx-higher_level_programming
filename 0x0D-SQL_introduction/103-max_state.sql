-- Connect to the appropriate database
USE hbtn_0c_0;

-- Display the max temperature of each state ordered by State name
SELECT state, MAX(temp) AS max_temp
FROM temperature_data
GROUP BY state
ORDER BY state;

