-- select cities in california from database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California';
