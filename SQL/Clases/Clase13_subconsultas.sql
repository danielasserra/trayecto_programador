-- CLASE 11
-- 14/8/25
-- SUBCONSULTAS

-- OPERADOR IN --
-- Quiero obtener todos los datos de la tabla Empleados 
-- que coincida con alguno de estos apellidso: 
SELECT *
FROM Empleados
WHERE E.apellido = "Garcia" or E.apellido = "Lopez" or E.apellido = "Rodriguez"
-- ES LO MISMO QUE
WHERE E.apellido IN ("Garcia", "Lopez", "Rodriguez")

-- Listar los empleados con sueldo mayor al promedio
SELECT E.nombre, E.sueldo
FROM Empleados as E
-- WHERE E.sueldo > AVG(E.sueldo)
-- Como no puedo usar AVG en where, hago subconsulta
WHERE E.sueldo >= (
    SELECT AVG(E.sueldo)
    FROM Empleados as E
)

-- Empleados que viven en localidades con más de 50.000 habitantes
SELECT E.nombre, E.apellido
FROM Empleados as E 
WHERE E.id_localidad IN
    (SELECT L.id_localidad
    FROM Localidades as L 
    WHERE L.cantidad_habitantes > 50000
    );

SELECT E.nombre, E.apellido
FROM Empleados as E 
JOIN Localidades as L ON L.id_localidad = E.id_localidad
WHERE L.cantidad_habitantes > 50000

-- Empleados que tienen un sueldo mayor al promedio de su localidad.
-- Calcular el promedio de sueldo de cada localidad y luego buscar 
-- empleados que tengan un sueldo mayor a ese promedio

SELECT E.nombre, E.apellido, E.sueldo, L.descripcion
FROM Empleados as E 
JOIN Localidades as L ON L.id_localidad = E.id_localidad
WHERE E.sueldo > (
    SELECT AVG(E.sueldo)
    FROM Empleado as E
    WHERE L.id_localidad = E.id_localidad);

-- Cantidad de tareas realizadas por cada empleado 
-- mostrando solo los que hicieron mas de 5

SELECT E.nombre, E.apellido, COUNT(ET.id_tareas) as cantidad_tareas
FROM Empleados as E 
JOIN empleados_tareas as ET ON E.id_empleados = ET.id_empleados
GROUP BY E.id_empleados
having COUNT(ET.id_tareas) > 5

/* vistas: consultas del servidor que se guardan
 son para altos niveles
Restrinjo info al usuario

vistas derivadas: Puedo tomar una subconsulta y crear una tabla para consultar. 
La tabla se crea y se destruye en el momento

La subconsulta no va  aestar en el WHERE, va a estar en el FROM
*/
SELECT sub.id_empleado, sub.total_tareas
FROM (
    SELECT ET.id_empleado, COUNT(*) as total_tareas
    FROM empleados_tareas as ET 
    GROUP BY ET.id_empleado
) as sub -- A LAS VISTAS SE LES DA UN NOMBRE PARA FUTURAS REFERENCIAS
JOIN Empleado as E ON sub.id_empleado = E.id_empleado
WHERE sub.total_tareas > 5

-- Empleados que hicieron la tarea con mayor cantidad de puntos
SELECT E.nombre, E.apellido
FROM Empleados as E
WHERE E.id_empleado IN (
    SELECT ET.id_empleado
    FROM empleados_tareas ET
    JOIN Tareas as T on T.id_tareas = ET.id_tareas
    WHERE T.puntos = (
        SELECT MAX (T.puntos)
        FROM Tareas )
)

-- Obtener el nombre de las mascotas, su tipo, y el nombre del veterinario que 
-- las ha atendido más veces.
SELECT M.nombre as nombre_mascota, M.tipo, V.nombre as nombre_veterinario
FROM Mascota as M
JOIN Veterinarios as V 
JOIN (
    SELECT A.id_mascota, A.id veterinario, COUNT(A.id_atencion) as cantidad_atenciones 
    FROM Atencion as A 
    GROUP BY A.id_mascota, A.id_veterinario
) as A ON A.id_mascota = V.id_mascota
WHERE MAX(A.id_veterinario)