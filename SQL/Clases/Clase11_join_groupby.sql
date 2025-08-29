-- CLASE 11
-- 7/8/25

-- BDD EMPRESA
-- seleccionar nombre, apellido y descripcion de las tareas realizadas entre dos fechas
SELECT E.nombre, E.apellido, T.descripcion, ET.fecha --agregamos la fecha para chequear que los datos esten correctos pero no los pide la consulta
FROM Empleados as E 
JOIN empleados_tareas as ET ON E.id_empleados = ET.id_empleados
JOIN tareas as T ON ET.id_tareas = T.id_tareas 
WHERE ET.fecha BETWEEN 2025/07/01 and 2025/07/03

-- total de puntos acumulados por cada empleado
SELECT SUM(T.puntos) as puntos_totales, E.apellido, E.nombre 
FROM Empleados as E
JOIN empleados_tareas as ET ON E.id_empleados = ET.id_empleados
JOIN tareas as T ON ET.id_tareas = T. id_tareas
GROUP BY E.id_empleados
ORDER BY puntos_totales DESC

-- mostrar localidades donde al menos 2 empleados realizaron tareas entre el 1 y el 5
-- de julio de 2025, y donde el promedio de puntos por tarea por empleado
-- supere los 15pts

SELECT L.descripcion
FROM empleados_tareas as ET
JOIN empleados as E ON ET.id_empleados = E.id_empleados
JOIN localidades as L ON L.id_localidad = E.localidad 
JOIN tareas as T ON T.id_tareas = ET.id_tareas
WHERE ET.fecha BETWEEN 20250701 and 20250705
GROUP BY L.id_localidad
having COUNT(E.id_empleados) >= 2 and AVG(T.puntos) > 15
