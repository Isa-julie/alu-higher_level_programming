-- Select all cities in California from the database hbtn_0d_usa.
USE hbtn_0d_usa;

SELECT name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
