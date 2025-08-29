

/*
---- Crear relaciones en phpmyadmin ---

Seleccionar campo y marcar como índice
Luego ir a “mas” “diseñador"
*/

-----------------------------------------------------------------


-- por cada empleado busco su localidad
-- de todos los empleados busco en la tabla de localidades, la que coincide
-- y la muestro en los resultados
-- TRAER DATOS DE EMPLEADOS CON DESCRIPCION DE LA LOCALIDAD
select E.apellido, E.nombre, L.descripción AS LOCALIDAD
from empleados as E, localidad as L --va a recorrer las dos tablas
where L.id_localidad = E.id_localidad --tiene q hacer el match entre una cosa y la otra



/* 
-------------------------
--------- JOIN ----------
-------------------------

Reemplaza el from, porque la consulta termina siendo dificil de leer e interpretar. 
Además, mejora la eficiencia de la consulta

Indica qué tablas quiero consultar. Xej. Tabla empleados con tabla localidades
EJ:
*/

select E.apellido, E.nombre, L.descripción AS LOCALIDAD
from empleados -- sobre la tabla que quiero hacer la consulta (quiero un listado de empleados)
JOIN E, localidad as L -- tabla secundaria
ON L.id_localidad = E.id_localidad --- clave primaria contra clave foranea 

----------------------------------------------------------------------------

-- Listado de todos los empleados que vivan en San Martin --

select E.apellido, E.nombre, L.descripcion AS LOCALIDAD
from empleados as E, localidades as L 
where L.id_localidad = E.id_localidad AND L.descripcion = "Lanus"


select E.apellido, E.nombre, L.descripcion AS LOCALIDAD
from empleados as E
JOIN localidades as L 
ON L.id_localidad = E.id_localidad
WHERE L.descripcion = "Lanus"



----------------------------------------------------------------------------

select E.apellido, E.nombre, L.descripcion AS LOCALIDAD, E.sueldo
from empleados as E
JOIN localidades as L 
ON L.id_localidad = E.id_localidad
WHERE L.descripcion = "Lanus" and E.sueldo <= 150000
ORDER BY E.sueldo ASC

-----------------------------------------------------------------------------

/* Cuantas tareas realizó cada empleado */

SELECT E.nombre, E.apellido, count(*)
FROM empleados_tareas as ET 
JOIN empleados as E ON ET.id_empleado = E.id_empleado
GROUP BY E.id_empleado