-- Ejercicio A: Seleccionar todos los campos con todos los datos de la tabla Persona --
SELECT * FROM `persona`

-- Ejercicio B: Visualizar nombre y fecha de nacimiento de todas las personas --
SELECT nombre, fecha_nacimiento FROM persona

-- agregar edad --
SELECT nombre, fecha_nacimiento, edad FROM persona;

-- nombre y edada de poersonas +25--
SELECT nombre, edad
FROM `persona` 
WHERE edad = 25

-- nombre y fecha de personas entre 22 y 29 años --
SELECT nombre, edad
FROM `persona` 
WHERE edad >= 22 AND edad <= 29

SELECT nombre, edad
FROM `persona` 
WHERE edad BETWEEN 22 and 29

-- nombre y fecha de personas entre 22 y 29 años o nombre "axel"--

SELECT nombre, edad
FROM `persona` 
WHERE (edad >= 22 AND edad <= 29) or nombre = "axel"


SELECT nombre, edad
FROM `persona` 
WHERE edad = 22 or nombre = "ana"


SELECT nombre, edad
FROM `persona` 
WHERE edad = 22 or NOT nombre = "ana"

SELECT p.nombre, p.fecha_nacimiento, p.edad
FROM `persona` as P 
ORDER BY p.edad


SELECT p.nombre, p.fecha_nacimiento, p.edad
FROM `persona` as P 
ORDER BY p.edad DESC