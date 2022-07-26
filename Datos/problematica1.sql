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

--Desde aca para abajo no ejecute nada, lo de arriba si

CREATE TABLE IF NOT EXISTS tarjeta(
								numero TEXT PRIMARY KEY CHECK (length(numero)<=20),
								CVV TEXT CHECK (length(numero)=3),
								fecha_otorgamiento TEXT NOT NULL,
								fecha_expiracion TEXT NOT NULL,
								tipo_tarjeta_id INTEGER NOT NULL
								FOREIGN KEY (tipo_tarjeta_id)
								REFERENCES tipo_tarjetas(tipo_tarjeta_id)
								);
--problematica 1.3
--Acá estoy creando una columna marca_id a la tabla de tarjeta y la estoy relacionando con la tabla de marcas_tarjeta
ALTER TABLE tarjeta
    ADD COLUMN marca_id INTEGER NOT NULL,
    ADD FOREIGN KEY (marca_id)
        REFERENCES marcas_tarjeta(marca_id);
		
--problematica 1.4		
--Acá estoy creando una columna customer_id a la tabla de tarjeta y la estoy relacionando con la tabla de cliente
--para que cada tarjeta sepa a que cliente pertenece
ALTER TABLE tarjeta
    ADD COLUMN customer_id INTEGER NOT NULL,
    ADD FOREIGN KEY (customer_id)
        REFERENCES cliente(customer_id);

--Esta tabla puede ser usada por clientes, empleados y sucursales
CREATE TABLE IF NOT EXISTS direccion(
								direccion_id INTEGER PRIMARY KEY,
								direccion_numero TEXT NOT NULL,
								direccion_ciudad TEXT NOT NULL,
								direccion_provincia TEXT NOT NULL,
								direccion_pais TEXT NOT NULL
								--REF
								)