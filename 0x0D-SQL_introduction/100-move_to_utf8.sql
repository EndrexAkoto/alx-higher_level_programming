-- Connect to the appropriate database
USE hbtn_0c_0;

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
  id int(11) DEFAULT NULL,
  name varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table to utf8mb4 collate utf8mb4_unicode_ci
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the specific field to utf8mb4 collate utf8mb4_unicode_ci
ALTER TABLE first_table
MODIFY COLUMN name varchar(256)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Confirm the changes
SHOW CREATE TABLE first_table;
