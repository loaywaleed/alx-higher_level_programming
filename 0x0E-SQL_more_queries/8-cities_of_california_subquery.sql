-- Script that lists all cities of California
SELECT ID, NAME
FROM CITIES
WHERE state_id IN
	(SELECT id FROM states 
		WHERE name = "California")
ORDER  BY ID;
