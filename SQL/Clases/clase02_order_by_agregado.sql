-- Clase 2
-- order by, fn agregado


--  ORDER BY --

-- Ordenar alfabéticamente a-z
Select *
From alumnos
Order BY apellido

--Ordenar alfabéticamente z-a
Select *
From alumnos
Order BY apellido DESC

-- Ordenar apellido alfabéticamente z-a, nombre a-z
Select *
From alumnos
Order BY apellido DESC, nombre ASC

------------------------------------------------------------

-- FUNCIONES DE AGREGADO
-- count (cuento cuantos son)
-- max
-- min
-- AVG


-- COUNT --

Select COUNT(*)
From alumnos

-- puedo renombrar una tabla:
Select COUNT(id)
From empleados as E -- alias para la tabla

-- puedo poner alias a las columnas
Select COUNT(E.id) as Cantidad

Select COUNT(id)
From empleados as E
WHERE E.id > 10



-- MAX --

-- salario maximo
SELECT max (E.salario) as Cantidad
From empleados as E



-- Min --

-- salario maximo
SELECT min (E.salario) as Cantidad
From empleados as E



-- AVG --

-- AVG average, promedio
SELECT sum (E.salario)/count(E.salario) as Cantidad
From empleados as E

-- Es lo mismo que:
SELECT AVG(E.salario) as Cantidad
From empleados as E


-- borrar info de tabla
delete from alumnos