/*-----------/ 
     TP 7
   PARTE 2 
 Veterinaria
     ***
Daniela Serra
/-----------*/


-- Resolver las siguientes consultas:

-- a. Listar todas las atenciones con el nombre de la mascota y la fecha de atención.

SELECT A.id_atencion, M.nombre as nombre_mascota, A.fecha
FROM Atencion as A
JOIN Mascota as M ON A.id_mascota = M.id_mascota


-- b. Obtener el nombre del dueño y su mascota para todas las atenciones registradas.
SELECT A.id_atencion, D.nombre as nombre_dueño, M.nombre as nombre_mascota
FROM Atencion as A
JOIN Mascota as M ON A.id_mascota = M.id_mascota
JOIN Dueño as D ON M.id_dueño = D.id_dueño
ORDER BY A.id_atencion --no es necesario, pero el listado estaba desordenado


-- c. Listar todas las mascotas con el nombre de su dueño 
-- que hayan recibido al menos una atención.
SELECT DISTINCT M.nombre as nombre_mascota, D.nombre as nombre_dueño -- para que se muestre una sola vez cada mascota
FROM Mascota as M
JOIN Dueño as D ON M.id_dueño = D.id_dueño
JOIN Atencion as A ON M.id_mascota = A.id_mascota
WHERE A.id_atencion is not NULL

-- d. Obtener el nombre de las mascotas, su tipo y el motivo de su última atención.
SELECT M.nombre as nombre_mascota, M.tipo, A.motivo
FROM Mascota as M
JOIN Atencion as A ON M.id_mascota = A.id_mascota
WHERE A.fecha = (
  SELECT MAX(A.fecha)
  FROM Atencion as A
  WHERE A.id_mascota = M.id_mascota
)

-- Listar los nombres de los dueños y las fechas en que sus mascotas fueron atendidas, 
-- ordenados por fecha.
SELECT D.nombre, A.fecha
FROM Dueño as D 
JOIN Mascota as M ON D.id_dueño = M.id_dueño
JOIN (
  SELECT id_mascota, MAX(fecha) as fecha
  FROM Atencion
  GROUP BY id_mascota
) AS A ON A.id_mascota = M.id_mascota
ORDER BY A.fecha


-- Obtener el nombre de las mascotas, su tipo y el número total de atenciones 
-- que han recibido.
SELECT M.nombre, M.tipo, COUNT(A.id_atencion) as total_atenciones
FROM Mascota as M 
JOIN Atencion as A ON M.id_mascota = A.id_mascota
GROUP BY M.nombre, M.tipo
ORDER BY total_atenciones DESC


-- Listar los dueños cuyos mascotas han recibido atenciones con un motivo que 
-- incluya la palabra 'Consulta'.
SELECT D.nombre 
FROM Dueño as D 
JOIN Mascota as M ON D.id_dueño = M.id_dueño
JOIN Atencion as A ON M.id_mascota = A.id_mascota
WHERE A.motivo LIKE "%Consulta%"
GROUP BY D.nombre 


-- Obtener la cantidad de atenciones por tipo de mascota.
SELECT M.tipo, COUNT(A.id_atencion) as cantidad_atenciones
FROM Mascota as M 
JOIN Atencion as A ON M.id_mascota = A.id_mascota
GROUP BY M.tipo
ORDER BY cantidad_atenciones DESC


-- Listar las mascotas que han sido atendidas más de una vez, 
-- mostrando el nombre de la mascota y el nombre del dueño.
SELECT M.nombre, D.nombre
FROM Mascota as M
JOIN Dueño as D ON D.id_dueño = M.id_dueño
JOIN Atencion as A ON M.id_mascota = A.id_mascota
GROUP BY M.id_mascota, M.nombre, D.nombre
HAVING COUNT(A.id_atencion) >= 2


-- Listar los nombres de los dueños y el total de atenciones que han 
-- recibido sus mascotas.
SELECT D.nombre as nombre_dueño, COUNT(A.id_atencion) as total_atenciones
FROM Dueño as D 
JOIN Mascota as M ON D.id_dueño = M.id_dueño
JOIN Atencion as A ON M.id_mascota = A.id_mascota
GROUP BY D.id_dueño, D.nombre 