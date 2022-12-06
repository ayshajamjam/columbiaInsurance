
-- Trigger Example

INSERT INTO Appointments
VALUES (15, '2021-01-01', '11:00:00', 'I have a problem with my eyesight');

INSERT INTO Schedules
VALUES('1669143079', '110112', 15, 'aj2604');

-- Query 1: Return all conditions treated by doctor with npi = 1669143079 (array)

SELECT D.conditions_treated
FROM doctors D
WHERE D.npi = '1669143079';


-- Query 2: Query by about text

SELECT to_tsvector(D.about) @@ to_tsquery('certified')
FROM doctors D
WHERE D.npi = '1326343625';