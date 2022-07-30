--3.1
SELECT *
FROM cuenta
WHERE balance < 0;

--3.2
SELECT customer_name as Nombre, 
				customer_surname as Apellido, 
				cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int) as Edad
FROM cliente
WHERE Apellido  LIKE '%Z%';--Captura los que contienen Z o z. Para capturar los que arrancan con Z seria 'Z%'

--3.3
SELECT customer_name as Nombre, 
				customer_surname as Apellido, 
				cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int) as Edad, 
				sucursal.branch_name AS 'Nombre Sucursal'
FROM cliente
LEFT JOIN sucursal ON sucursal.branch_id = cliente.branch_id
WHERE Nombre LIKE 'Brendan'
ORDER BY sucursal.branch_name; --Aca no específica como, asi que lo dejo ascendente

--3.4
--Este no se si es así. Aca agarra los prestamos mayores a 80000 y tambien los que son prendarios
SELECT loan_total AS 'Importe', loan_type AS 'Tipo Préstamo'
FROM prestamo
WHERE loan_total > 8000000  --Acá es 80.000 más los dos números que representan los centavos
UNION
SELECT loan_total, loan_type
FROM prestamo
WHERE loan_type LIKE 'PRENDARIO'
ORDER BY loan_total DESC;

--3.5
SELECT *
FROM prestamo
WHERE loan_total > (
			SELECT CAST(REPLACE(CAST(ROUND(AVG(loan_total) / count(loan_total),2) AS TEXT), '.', '') AS INT)
			FROM prestamo
			);

--3.6
SELECT COUNT(Edad) as Cantidad
FROM(
			SELECT cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int) as Edad
			FROM cliente
			WHERE Edad < 50
			);

--3.7
SELECT *
FROM cuenta
WHERE balance > 800000 --8.000 más los dos ceros que representan los centavos
LIMIT 5;

--3.8
SELECT *
FROM prestamo
WHERE substr(loan_date, 6,2) LIKE '04' OR  --Abril
			 substr(loan_date, 6,2) LIKE '06' OR   --Junio
			substr(loan_date, 6,2) LIKE '08'          --Agosto
ORDER BY loan_total DESC;

--3.9
SELECT loan_type as 'Tipo Préstamo', SUM(loan_total) AS  loan_total_accu
FROM prestamo
GROUP BY loan_type

