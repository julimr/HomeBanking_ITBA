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



