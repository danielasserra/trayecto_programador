-- CLASE 04 BASE DE DATOS

-- DDL - permite modificar la estructura de una base de datos: DROP, CREATE, ALTER
-- DML - permite manipular los datos con SELECT, UPDATE, DELETE, INSERT

-- ELIMINAR UNA TABLA:
DROP table 'Alumnos'

select nombre, sueldo
from empleados
WHERE fecha_ingreso < 2001/06/23

-- manipular fechas:
-- fecha
select CURRENT_DATE()

-- fecha y hora
select now()
select CURRENT_TIMESTAMP()

-- año del empleado
select YEAR(fecha_nacimiento)
from empleados
where id = 600

-- Calcula la diferencia en días entre el 20 de enero de 2005 y el 1 de enero de 2000.
-- luego divide por 365 para saber cuantos años son
select datediff("2005/01/20", "2000/01/01")/365

-- Calcula la diferencia en años completos entre dos fechas:
select abs(timestampdiff(year, "2005/01/20", "2000/01/01")

-- saber la cantidad de meses que hay entre una fecha y la actualidad
select time(timestampdiff(month, "1987,10,20", CURRENT_DATE())

