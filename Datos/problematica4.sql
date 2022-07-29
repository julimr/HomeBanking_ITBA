--4.1
SELECT COUNT(cliente.branch_id) AS 'Cantidad Clientes', sucursal.branch_name AS 'Sucursal'
FROM cliente
LEFT JOIN sucursal ON sucursal.branch_id = cliente.branch_id
GROUP BY sucursal.branch_name
ORDER BY COUNT(cliente.branch_id) DESC

--4.2
--El que hicimos en clase
SELECT idBranch, qClientes, qEmpleados, round((qClientes * 1.0/qEmpleados * 1.0), 2) as 'Empleados por Cliente'
FROM (
   SELECT sucursal.branch_id as idBranch, count(cliente.customer_id) as qClientes, qEmpleados
   FROM sucursal
   LEFT JOIN cliente
   ON sucursal.branch_id = cliente.branch_id
   LEFT JOIN (
      SELECT sucursal.branch_id as sucursalID, count(empleado.employee_id) as qEmpleados
      FROM sucursal
      LEFT JOIN empleado
      ON sucursal.branch_id = empleado.branch_id
      GROUP BY sucursal.branch_id
   ) as cantidad_Empleados
   ON sucursal.branch_id = cantidad_Empleados.sucursalID
   GROUP BY sucursal.branch_id
) as Division 

-- 4.3
-- verificar si es asi!!!!
SELECT cliente.branch_id as sucursalID, count(tarjetasCredito.customer_id) as CantidadTarjetasCredito
FROM cliente
LEFT JOIN (
		SELECT tarjeta.customer_id
		FROM tarjeta
		WHERE tarjeta.tipo_tarjeta_id = 2
) as tarjetasCredito
ON tarjetasCredito.customer_id = cliente.customer_id
GROUP BY cliente.branch_id


-- 4.4

