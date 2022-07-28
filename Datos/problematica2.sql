SELECT * 
FROM cliente;
-- 2.1
CREATE VIEW v_1 AS 
SELECT
	customer_id, branch_id, customer_name, customer_surname, customer_DNI,
	cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int) as edad
FROM cliente
	
-- 2.1.1
SELECT *
FROM v_1
WHERE edad > 40
ORDER BY customer_DNI DESC;
-- 2.1.2
SELECT *
FROM v_1
WHERE customer_name = 'Tyler' 
		OR customer_name =  'Anne'
ORDER BY edad ASC;

