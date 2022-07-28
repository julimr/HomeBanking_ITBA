SELECT * 
FROM cliente;
------ 2.1
CREATE VIEW v_probl2punto1 AS 
SELECT
	customer_id, branch_id, customer_name, customer_surname, customer_DNI,
	cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int) as edad
FROM cliente
	
------ 2.1.1
SELECT *
FROM v_probl2punto1
WHERE edad > 40
ORDER BY customer_DNI DESC;

------ 2.1.2
SELECT *
FROM v_1
WHERE customer_name = 'Tyler' 
		OR customer_name =  'Anne'
ORDER BY edad ASC;

------ 2.2
INSERT INTO `cliente` (`customer_name`,`customer_surname`,`customer_DNI`,`branch_id`,`dob`)
VALUES
	('Lois','Stout',47730534,80,'1984-07-07'),
	('Hall','Mcconnell',52055464,45,'1968-04-30'),
	('Hilel','Mclean',43625213,77,'1993-03-28'),
	('Jin','Cooley',21207908,96,'1959-08-24'),
	('Gabriel','Harmon',57063950,27,'1976-04-01');

SELECT * 
FROM cliente;

------ 2.3
UPDATE cliente
SET branch_id = 10
WHERE customer_id >= 501 AND customer_id <= 505;
-- verifico que se hayan modificado los campos
SELECT *
FROM cliente
WHERE customer_id >= 501 AND customer_id <= 505;

------ 2.4
DELETE FROM cliente
WHERE customer_name = 'Noel' AND customer_surname = 'David';

------ 2.5
SELECT loan_type as Prestamo_max_importe
FROM prestamo
ORDER BY loan_total DESC
LIMIT 1;


