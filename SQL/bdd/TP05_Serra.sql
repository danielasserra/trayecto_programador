-- TP 5
-- Daniela Serra

-- Agregar mínimo 5 alumnos, teniendo en cuenta los campos nulos y las distintas 
-- formas de insertar campos.

INSERT INTO Alumnos (Nombre, Apellido, Localidad, NotaFinal, Genero, FechaNacimiento, Edad)
VALUES 
("Maria", "Mercedes", "Mexico", 9, "No Binario", "1987-11-14", 37),
("Marcelo", "Tinelli", "Olivos", 6, "Masculino", "1967-09-19", 57),
("Marcelo", "Polino", "El Palomar", 9, "No Binario", "1979-01-04", 49),
("Marcela", "Tauro", "CABA", 8, "Femenino", "1995-11-14", 30),
("Claudia", "Villafañe", "Docsud", 10, "No Binario", "2008-07-09", 16);

-- Actualizar: 
-- La edad a 15 años de los alumnos que hayan nacido entre 1999 y 2006.
UPDATE Alumnos
SET edad = 15
WHERE year(FechaNacimiento) >= 1999 and year(FechaNacimiento) <= 2006

-- La fecha de nacimiento a 20-10-1999 de los alumnos que se llaman Juan.
UPDATE Alumnos
SET FechaNacimiento = 1999-10-20
WHERE Nombre = "Juan"

-- Sumar a la edad el 20% de la misma, cuando el apellido sea Gutierrez y 
-- la edad sea mayor o igual a 25.
UPDATE Alumnos
SET Edad = Edad + (Edad * 0.2)
WHERE Apellido = "Gutierrez" and Edad >= 25

-- Borrar: 
-- Los alumnos que se apelliden Gomez, cuya edad esté entre 25 y 39 años.
DELETE 
FROM Alumnos
WHERE Apellido = "Gomez" and Edad BETWEEN 25 and 39;

-- Los alumnos que hayan nacido entre el 22-10-1999 y el 01-11-2005
DELETE 
FROM Alumnos
WHERE FechaNacimiento BETWEEN "1999-10-22" and "2005-11-01";

-- Los alumnos que hayan nacido entre el año 2009 y 2011
DELETE 
FROM Alumnos
WHERE year(FechaNacimiento) BETWEEN 2009 and 2011;

-- Promedio de edades de los distintos géneros.
SELECT Genero, avg(Edad) as promedio
FROM Alumnos
GROUP BY Genero

-- Cantidad de alumnos de los distintos géneros, cuya nota está entre 5 y 8. 
-- Ordenar por cantidad de alumnos.
SELECT Genero, COUNT(IdAlumno) as cantidad
FROM Alumnos
WHERE NotaFinal BETWEEN 5 and 8
GROUP BY Genero
ORDER BY cantidad

-- Nota máxima de cada género, siempre y cuando la nota supere los 7 puntos.
SELECT Genero, MAX(NotaFinal) AS NotaMaxima
FROM Alumnos
WHERE NotaFinal > 7
GROUP BY Genero;
