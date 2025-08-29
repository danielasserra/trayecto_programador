/*-----------/ 
     TP 7
   PARTE 1 
 Veterinaria
     ***
Daniela Serra
/-----------*/

-- Resolver las siguientes consultas de selección:

-- a. Seleccionar el nombre y género de todas las mascotas que estén vacunadas. 

SELECT nombre, genero
FROM Mascota
WHERE esta_vacunada = "si"


-- b. Seleccionar el nombre y edad de todos los dueños de género femenino.

SELECT nombre, edad
FROM Dueño
WHERE genero = "femenino"


-- c. Seleccionar todas las mascotas de tipo Perro.
SELECT *
FROM Mascota
WHERE tipo = "Perro"


-- d. El promedio de edad de todos los dueños.
SELECT AVG(edad) as promedio_edad
FROM Dueño


-- e. El promedio de edad de las mascotas que estén vacunadas cuyo género sea masculino.
SELECT AVG (edad) as promedio_edad_mascota
FROM Mascota
WHERE esta_vacunada = "si" and genero = "masculino"


-- f. Cantidad de mascotas de tipo perro
SELECT COUNT(*) as cantidad_perros
FROM Mascota
WHERE tipo = "Perro"


-- g. Listar cada mascota con el nombre y edad de su dueño, 
-- ordenado por el nombre del dueño de la A a la Z.
SELECT D.nombre as nombre_dueño, D.edad as edad_dueño, M.*
FROM Dueño as D
JOIN Mascota as M ON D.id_dueño = M.id_dueño
ORDER BY D.nombre ASC


-- h. Promedio de edad de las mascotas de dueños de género femenino.
SELECT AVG(edad) as promedio_edad_dueños
FROM Dueño
WHERE genero = "femenino"


-- i. Listar nombre y edad de los gatos que estén vacunados cuyo dueño se llame Jose.
SELECT M.nombre, M.edad
FROM Mascota as M
JOIN Dueño as D ON M.id_dueño = D.id_dueño
WHERE tipo = "gato" and esta_vacunada = "si" and D.nombre = "Jose"


-- j. Obtener la cantidad de mascotas por tipo.
SELECT M.tipo, COUNT(M.tipo) as cantidad
FROM Mascota as M
GROUP BY M.tipo
Order BY cantidad ASC


-- k. Obtener el promedio de edades de mascotas por tipo.
SELECT M.tipo, AVG(M.edad) as promedio_edad
FROM Mascota as M
GROUP BY M.tipo

-- l. Contar cuántas mascotas tiene cada dueño.
SELECT D.nombre, COUNT(M.id_dueño) as cantidad_mascotas
FROM Mascota as M
JOIN Dueño as D ON M.id_dueño = D.id_dueño
GROUP BY D.nombre


