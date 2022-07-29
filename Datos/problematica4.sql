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
-- verificar si es asi!!!!
SELECT cliente.branch_id as sucursalID, count(prestamos.customer_id) as CantidadPrestamos
FROM cliente
LEFT JOIN (
	SELECT prestamo.customer_id, count(prestamo.customer_id) as cantidadPrestamos
	FROM prestamo
	GROUP BY prestamo.customer_id
) as prestamos
ON prestamos.customer_id = cliente.customer_id
GROUP BY cliente.branch_id

-- 4.5
CREATE TABLE  IF NOT EXISTS auditoria_cuenta(
							old_id INTEGER,
							new_id INTEGER PRIMARY KEY,
							old_balance INTEGER NOT NULL,
							new_balance INTEGER NOT NULL,
							old_iban TEXT NOT NULL,
							new_iban TEXT NOT NULL,
							old_type INTEGER NOT NULL,
							new_type INTEGER NOT NULL,
							user_action TEXT NOT NULL,
							created_at TEXT NOT NULL	
							);
-- 4.5.1					
CREATE TRIGGER IF NOT EXISTS post_actualizacion_cuentas 
   AFTER UPDATE 
   ON cuenta
		WHEN old.balance <> new.balance 
			OR old.iban <> new.iban
				OR  old.tipo_cuenta <> new.tipo_cuenta
BEGIN
	INSERT INTO auditoria_cuenta(
		old_id, new_id, old_balance, new_balance, old_iban, new_iban, old_type,
		new_type, user_action, created_at )
	VALUES (
		old.account_id, new.account_id, old.balance, new.balance, old.iban, new.iban, old.tipo_cuenta,
		new.tipo_cuenta, 'UPDATE', DATETIME('now')
		);
END;

-- 4.5.2
UPDATE cuenta
SET balance = balance - 100
WHERE account_id >= 10 AND account_id <= 14;
-- verifico que se crearon los campos en la tabla nueva
SELECT *
FROM auditoria_cuenta

-- 4.6
CREATE INDEX clientes_por_DNI
ON cliente(customer_DNI);

-- verifico que la consulta usa el indice creado
EXPLAIN QUERY PLAN
SELECT cliente.customer_DNI, cliente.customer_name
FROM cliente
WHERE customer_DNI = 50011089

-- 4.7