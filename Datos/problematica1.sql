CREATE TABLE IF NOT EXISTS tipos_cliente(
							tipo_cliente_id INTEGER PRIMARY KEY,
							tipo_cliente TEXT NOT NULL --Classic, Gold, Black
							)
							
CREATE TABLE  IF NOT EXISTS  cuentas(
							cuenta_id INTEGER PRIMARY KEY,
							tipo_cuenta TEXT NOT NULL --Pesos, Dolares, Corriente	
							)
							
CREATE TABLE IF NOT EXISTS marcas_tarjeta(
							marca_id INTEGER PRIMARY KEY,
							marca TEXT NOT NULL --Visa, MasterCard, AmericanExpress
							)

CREATE TABLE IF NOT EXISTS tarjeta(
								numero INTEGER PRIMARY KEY CHECK (length(numero)<=20),
								CVV INTEGER CHECK (length(numero)=3),
								fecha_otorgamiento TEXT NOT NULL,
								fecha_expiracion TEXT NOT NULL,
								tipo_tarjeta_id INTEGER NOT NULL
								FOREIGN KEY (tipo_tarjeta_id)
								REFERENCES tipo_tarjeta(tipo_tarjeta_id)
								)

CREATE TABLE IF NOT EXISTS tipo_tarjeta(
								tipo_tarjeta_id INTEGER PRIMARY KEY
								tipo_tarjeta TEXT NOT NULL--Débito o Crédito				
								)