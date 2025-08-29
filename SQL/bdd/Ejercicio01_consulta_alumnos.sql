-- Daniela Serra
-- Ejercicio 02
-- Dado el DataSet Escuela del ejercicio 01, realizar las siguientes consultas:

-- Todos los datos de todos los alumnos.
SELECT * 
FROM `Alumnos`

-- Todos los datos de los alumnos con apellido Gomez
SELECT  Apellido "Gomez" 
FROM `Alumnos`

-- Apellido y nombre de los alumnos cuya edad está entre 15 y 39 inclusive.
SELECT  Apellido, Nombre
FROM `Alumnos`
WHERE edad BETWEEN 15 and 39

-- Apellido del alumno de Id 9 
SELECT  Apellido
FROM `Alumnos`
WHERE IdAlumno = 9

-- Todos los datos de los alumnos cuyo Id estè entre 5 y 11, y cuyo apellido sea Gomez o Perez
SELECT  Apellido
FROM `Alumnos`
WHERE (IdAlumno BETWEEN 5 AND 11) AND (Apellido = "Gomez" OR Apellido = "Perez")

-- Apellido, nombre y nota de los alumnos con nota mayor a 5.
SELECT  Apellido, Nombre, NotaFinal
FROM `Alumnos`
WHERE NotaFinal > 5

-- Guardar todas las consultas en un script.


