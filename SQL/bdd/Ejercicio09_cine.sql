/*----------------/ 
    Ejercicio 9
       Cine
      ******
   Daniela Serra
/----------------*/

-- 1. Título y género de cada película, ordenados por nombre de cliente de manera 
-- descendente.
SELECT P.titulo, G.descripcion
FROM Peliculas as P 
JOIN Genero as G ON G.id_genero = P.id_genero
JOIN Reservas as R ON R.id_pelicula = P.id_pelicula
JOIN Clientes as C ON C.id_cliente = R.id_cliente
ORDER BY C.nombre DESC

-- 2. Calcular el promedio de duración de las películas por cada género.
SELECT AVG(P.duracion) as duracion_promedio, G.descripcion as genero
FROM Peliculas as P 
JOIN Genero as G ON G.id_genero = P.id_genero
GROUP BY G.descripcion


-- 3. Contar la cantidad de películas reservadas por cada cliente.
SELECT C.nombre, COUNT(R.id_reserva) as cantidad_reservas
FROM Reservas as R
JOIN Clientes as C ON C.id_cliente = R.id_cliente
GROUP BY C.nombre

-- 4. Cuántas reservas confirmadas tiene cada película.
SELECT P.titulo as titulo_pelicula, COUNT(R.id_reserva) as reservas_confirmadas
FROM Peliculas as P 
JOIN Reservas as R ON R.id_pelicula = P.id_pelicula
WHERE R.estado = "confirmada"
GROUP BY P.titulo


-- 5. El detalle de los clientes que hicieron reservas de películas del 
-- género “Comedia”.
SELECT * 
FROM Clientes as C 
JOIN Peliculas as P ON 
JOIN Genero as G ON G.id_genero = P.id_genero

JOIN Reservas as R ON R.id_pelicula = P.id_pelicula

WHERE G.descripcion = "Comedia"


-- 6. Nombres de los distintos clientes que realizaron al menos una reserva.
SELECT DISTINCT C.nombre as reserva_cliente
FROM clientes as C
JOIN Reservas as R ON R.id_cliente = C.id_cliente

-- 7. Mostrar todas las reservas que correspondan a películas con 
-- duración mayor a 120 minutos.
SELECT R.id_reserva as reserva_numero, P.titulo as titulo_pelicula, C.nombre AS cliente, R.fecha_reserva
FROM Reservas as R 
JOIN Peliculas as P on P.id_pelicula = R.id_pelicula
WHERE P.duracion >= 120


-- 8. Cantidad de reservas confirmadas realizadas por el cliente “María Pérez” 
-- si existe.
SELECT COUNT(R.id_reserva) as reservas_confirmadas, C.nombre as nombre_cliente
FROM Reservas as R
JOIN Clientes as C on C.id_cliente = R.id_cliente
WHERE C.nombre = "Maria Perez" and R.estado = "Confirmada"
GROUP BY C.nombre


-- 9. Título de la película reservada junto con su género y 
-- el nombre del cliente que la reservó.
SELECT P.titulo, G.descripcion, C.nombre as nombre_cliente
FROM Peliculas as P 
JOIN Genero as G ON G.id_genero = P.id_genero
JOIN Reservas as R ON R.id_pelicula = P.id_pelicula
JOIN Clientes as C ON C.id_cliente = R.id_cliente


-- 10. Detalle de las reservas donde participaron películas del género 
-- “Acción” junto con el nombre de los clientes.
SELECT P.titulo, R.fecha, R.cantidad_entradas, R.estado, C.nombre as nombre_cliente
FROM Peliculas as P 
JOIN Genero as G ON G.id_genero = P.id_genero
JOIN Reservas as R ON R.id_pelicula = P.id_pelicula
JOIN Clientes as C ON C.id_cliente = R.id_cliente
WHERE G.descripcion = "Accion"

