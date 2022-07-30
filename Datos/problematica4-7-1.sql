BEGIN TRANSACTION;

UPDATE cuenta
SET balance = balance - 10000
WHERE account_id = 200;

UPDATE cuenta
SET balance = balance + 100000
WHERE account_id = 400;
	-- 4.7.2
INSERT INTO movimientos(numero_cuenta, monto, tipo_operacion, hora)
VALUES (200, 1000, '-', TIME('now'));
	
INSERT INTO movimientos(numero_cuenta, monto, tipo_operacion, hora)
VALUES (400, 1000, '+', TIME('now'));
	
SELECT *
FROM movimientos;

COMMIT;