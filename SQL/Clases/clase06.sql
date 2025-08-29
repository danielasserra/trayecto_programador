/* data manipulation languaje
SELECT
INSERT
UPDATE : actualizar uno o mas registros
DELETE: borrar uno o más registros dentro de una tabla

*/
-- Insert into NOMBRE DE TABLA (CAMPOS) VALUES (Valores)
Insert into persona (nombre, edad, genero, fecha_nacimiento) 
VALUES ("German Scarafilo", "Masculino", NULL, "1994-10-20")

UPDATE persona 
SET edad = 15
WHERE id = 13

DELETE 
FROM persona
WHERE id = 13

-- DISTINCT : cuales son los diferentes elementos dentro de un conjunto
SELECT 
distinct (genero)
from persona

--GROUP BY: Hacer agrupaciones de datos
SELECT genero
from persona
group by genero


-- contar cuantas personas hay de cada genero y ordenarlo en forma ascendente
SELECT genero COUNT(id) as cantidad
FROM persona
GROUP BY genero
ORDER BY cantidad asc


-- promedio de edad de las personas mayoers de 10 agrupado por genero
SELECT genero avg(edad) as promedio
FROM persona
WHERE edad >= 10
GROUP BY genero

-- having: restriccion sobre el grupo
SELECT genero avg(edad) as promedio
FROM persona
WHERE edad >= 10
GROUP BY genero
HAVING promedio > 10
ORDER BY genero