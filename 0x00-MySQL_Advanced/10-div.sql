-- a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
-- You must create a function
-- The function SafeDiv takes 2 arguments:
-- And returns a / b or 0 if b == 0

DELIMITER //

DROP FUNCTION IF EXISTS SafeDive;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	RETURN (IF (b = 0, 0, a / b));
END //

DELIMITER ;
