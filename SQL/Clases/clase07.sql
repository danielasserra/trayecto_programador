-- CLASE 07

-- AGREGAR COLUMNA
-- modificar estructura de tabla se usa ALTER
--tiene que permitir null porque la tabla ya tiene datos y si no, va a generar conflicto
ALTER TABLE Alumnos 
ADD COLUMN Genero varchar(1) null

-- completar el campo género con F para los ID impares y M para los pares
UPDATE Alumnos
SET Genero = "M"
WHERE IdAlumno%2=0

UPDATE Alumnos
SET Genero = "F"
WHERE IdAlumno%2!=0

--completar el campo género con F para los nombres terminados en a
UPDATE Alumnos
SET Genero = "F"
WHERE Nombre Like "%a" or Nombre Like "%y"

-- cambiar el nombre en varios ID
UPDATE Alumnos
SET Nombre = "Juan"
WHERE IdAlumno in (1, 5, 8, 20)

