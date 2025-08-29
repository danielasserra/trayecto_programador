-- TP 4
-- DANIELA SERRA

-- nombre y apellido de los alumnos que nacieron antes del 20/10/2014.
select nombre, apellido
from alumnos
where FechaNacimiento < "20/10/2014"

-- nombre y apellido de los alumnos que nacieron después del 20/10/2014.
select nombre, apellido
from alumnos
where FechaNacimiento > "20/10/2014"

-- nombre y apellido de los alumnos que nacieron el 20/10/2014.
select nombre, apellido
from alumnos
where FechaNacimiento = "20/10/2014"

-- nombre y apellido de los alumnos que nacieron entre dos fechas (inclusive).
select nombre, apellido
from alumnos
where FechaNacimiento BETWEEN "2010/10/20" and "2024/10/20"

-- nombre y apellido de los alumnos que nacieron entre dos fechas (exclusivamente).
select nombre, apellido
from alumnos
where FechaNacimiento > "2007/10/20" and FechaNacimiento < "2010/10/20"

-- nombre y apellido de los alumnos que nacieron en 2014.
select nombre, apellido
from alumnos
where YEAR(FechaNacimiento) = 2014

-- nombre y apellido de los alumnos que nacieron en marzo.
select nombre, apellido
from alumnos
where MONTH(FechaNacimiento) = 3

-- todos los datos de los alumnos que tienen más de 23 años.
select *
from alumnos
where edad > 23

-- Investigar cómo actualizar la tabla alumnos, para que cada alumno tenga su edad.
UPDATE Alumnos
SET Edad = TIMESTAMPDIFF(YEAR, FechaNacimiento, CURRENT_DATE());
