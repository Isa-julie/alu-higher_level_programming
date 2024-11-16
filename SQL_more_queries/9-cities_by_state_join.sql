-- List all cities and their associated states in the database hbtn_0d_usa.
USE hbtn_0d_usa;
SELECT
    cities.id AS city_id,
    cities.name AS city_name,
    (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
