CREATE TABLE IF NOT EXISTS tipos_cliente(
							tipo_cliente_id INTEGER PRIMARY KEY,
							tipo_cliente TEXT NOT NULL --Classic, Gold, Black
							);

INSERT INTO tipos_cliente(tipo_cliente)
VALUES ('Classic'), ('Gold'), ('Black');

SELECT *
FROM tipos_cliente;
				
CREATE TABLE  IF NOT EXISTS  cuentas(
							cuenta_id INTEGER PRIMARY KEY,
							tipo_cuenta TEXT NOT NULL --Pesos, Dolares, Corriente	
							);
							
INSERT INTO cuentas(tipo_cuenta)
VALUES ('Caja ahorro en pesos'), ('Caja ahorro en dólares'), ('Cuenta corriente');

SELECT *
FROM cuentas;
							
CREATE TABLE IF NOT EXISTS marcas_tarjeta(
							marca_id INTEGER PRIMARY KEY,
							marca TEXT NOT NULL --Visa, MasterCard, AmericanExpress
							);
							
INSERT INTO marcas_tarjeta(marca)
VALUES ('Visa'), ('MasterCard'), ('American Express');

SELECT *
FROM marcas_tarjeta;

CREATE TABLE IF NOT EXISTS tipo_tarjetas(
								tipo_tarjeta_id INTEGER PRIMARY KEY,
								tipo_tarjeta TEXT NOT NULL--Débito o Crédito				
								);
								
INSERT INTO tipo_tarjetas(tipo_tarjeta)
VALUES ('Débito'), ('Crédito');

SELECT *
FROM tipo_tarjetas;

CREATE TABLE IF NOT EXISTS tarjeta(
								numero TEXT PRIMARY KEY CHECK (length(numero)<=20),
								CVV TEXT CHECK (length(CVV)=3),
								fecha_otorgamiento TEXT NOT NULL,
								fecha_expiracion TEXT NOT NULL,
								tipo_tarjeta_id INTEGER NOT NULL,
								marca_id INTEGER NOT NULL,
								customer_id INTEGER NOT NULL,
								FOREIGN KEY (tipo_tarjeta_id)
								REFERENCES tipo_tarjetas(tipo_tarjeta_id)
								FOREIGN KEY (marca_id) -- 1.3
								REFERENCES marcas_tarjeta(marca_id)
								FOREIGN KEY (customer_id) --1.4
								REFERENCES cliente(customer_id)
								);
--1.5 - Agregar 500 tarjetas de credito
SELECT *
FROM empleado

-- 1.6 - Agregar la entidad direcciones, que puede ser usada por los clientes, empleados y sucursales
CREATE TABLE IF NOT EXISTS direccion(
								direccion_id INTEGER PRIMARY KEY,
								calle TEXT NOT NULL,
								numero TEXT NOT NULL,
								ciudad TEXT NOT NULL,
								provincia TEXT NOT NULL,
								pais TEXT NOT NULL,
								customer_id INTEGER,
								employee_id INTEGER,
								branch_id INTEGER,
								FOREIGN KEY (customer_id)
								REFERENCES cliente(customer_id)
								FOREIGN KEY (employee_id)
								REFERENCES empleado(employee_id)
								FOREIGN KEY (branch_id)
								REFERENCES sucursal(branch_id)
								);
-- 1.7 - Insertar 500 direcciones, asignando del lote inicial a empleados, clientes o sucursal de forma aleatoria. 
SELECT *
FROM direccion

-- EJECUTADO HASTA ACA!!

--Actualiza de empleados, la columna employee_hire_date
--substr(string, donde arranca, largo(opcional))
UPDATE empleado
SET employee_hire_date = substr(employee_hire_date, 7) || "-" || substr(employee_hire_date,4,2) || "-" || substr(employee_hire_date, 1,2); 
							
SELECT employee_hire_date
FROM empleado
LIMIT 10
