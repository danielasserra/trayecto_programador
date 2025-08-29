-- TP 02 --
-- Daniela Serra --

-- Cantidad de alumnos.
SELECT COUNT(*)
FROM `Alumnos` 

-- Máxima nota.
SELECT max(NotaFinal) as NotaMasAlta 
FROM `Alumnos` 
-- Mínima nota.
SELECT min(NotaFinal) as NotaMasBaja 
FROM `Alumnos` 

-- Promedio de notas
SELECT AVG(NotaFinal) as PromedioDeNotas
FROM `Alumnos` 

-- Cantidad de alumnos de género masculino.
SELECT *
FROM `Alumnos` 
WHERE Genero = "Masculino"

-- Promedio de edades de los estudiantes de género Femenino.
SELECT AVG(edad)
FROM `Alumnos` 
WHERE Genero = "Femenino"

-- Maxima edad de los alumnos de género No binario.
SELECT max(edad)
FROM `Alumnos` 
WHERE Genero = "No binario"

-- Seleccionar todos los alumnos con edad entre 20 y 30 años y ordenarlos por apellido en orden alfabético.
SELECT *
FROM `Alumnos` 
WHERE (edad BETWEEN 20 and 30)
ORDER BY apellido

-- Seleccionar todos los alumnos que no sean no binarios cuya nota sea mayor a 4 y ordenarlos por nota de mayor a menor. 
SELECT *
FROM `Alumnos` 
WHERE (Genero = "No binario") and (NotaFinal > 4)
ORDER BY NotaFinal

-- Seleccionar todos los alumnos que no sean mujeres de apellido Gomez y ordenarlos por edad.
SELECT *
FROM `Alumnos` 
WHERE (Genero != "Femenino") and (apellido = "Gomez")
ORDER BY edad

-- Cantidad de alumnos que no son masculinos.
SELECT COUNT (*)
FROM `Alumnos` 
WHERE (Genero != "Masculino") 

-- Seleccionar todos los alumnos y ordenarlos por apellido en forma descendente y edad en forma ascendente.
SELECT *
FROM `Alumnos` 
ORDER BY apellido DESC, edad ASC