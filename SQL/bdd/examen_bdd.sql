/*
   EXAMEN 
     SQL
Daniela Serra
*/

-- 1. Nombre y tipo de cada pokémon, ordenado por nombre de entrenador de 
-- manera descendente.
SELECT P.nombre, T.descripcion
FROM Pokemones as P
JOIN Entrenadores as E ON E.id_entrenador = P.id_entrenador
JOIN Tipos as T ON T.id_tipo = P.id_tipo
ORDER BY E.nombre DESC 


-- 2. Calcular el promedio de puntos de defensa por cada tipo de pokémon.
SELECT T.descripcion as pokemon_tipo, AVG(P.puntos_defensa) as promedio_defensa 
FROM Pokemones as P 
JOIN Tipos as T ON T.id_tipo = P.id_tipo
GROUP BY T.descripcion, T.id_tipo

-- 3. Contar la cantidad de pokemones que tiene cada entrenador.
SELECT E.nombre as nombre_entrenador, COUNT(P.id_pokedex) as total_pokemones
FROM Pokemones as P 
JOIN Entrenadores as E ON E.id_entrenador = P.id_entrenador
GROUP BY E.nombre, E.id_entrenador 


-- 4. Cuantas batallas ganó cada pokemon
SELECT P.nombre as nombre_pokemon, COUNT(B.ganador) as batallas_ganadas
FROM Pokemones as P 
JOIN Batallas as B ON P.id_pokedex = B.ganador 
GROUP BY P.nombre
ORDER BY batallas_ganadas DESC

-- 5. El detalle de los entrenadores que tienen pokemones de tipo “Psíquico”.
SELECT E.nombre as nombre_entrenador, COUNT(P.id_pokedex) as cantidad_pokemon_psi, T.descripcion as pokemon_tipo
FROM Pokemones as P 
JOIN Entrenadores as E ON E.id_entrenador = P.id_entrenador
JOIN Tipos as T ON T.id_tipo = P.id_tipo 
WHERE T.descripcion = "Psíquico"
GROUP BY E.nombre


-- 6. Nombre de los distintos entrenadores que ganaron por lo menos una batalla.
SELECT E.nombre as nombre_entrenador, COUNT(B.ganador) as batallas_ganadas 
FROM Entrenadores as E 
JOIN Pokemones as P ON E.id_entrenador = P.id_entrenador
JOIN Batallas as B ON P.id_pokedex = B.ganador
WHERE B.ganador > 0
GROUP BY E.nombre

-- 7. Mostrar todas las batallas en las que participó un pokemon con más de 50 puntos de ataque.
SELECT *
FROM Batallas as B 
JOIN Pokemones as P ON P.id_pokedex = B.ganador 
WHERE puntos_ataque > 50


-- 8. Cantidad de batallas que ganó el entrenador “Ash”
SELECT E.nombre as nombre_entrenador, COUNT(B.ganador) as batallas_ganadas
FROM Batallas as B 
JOIN Pokemones as P ON P.id_pokedex = B.ganador 
JOIN Entrenadores as E ON E.id_entrenador = P.id_entrenador
WHERE E.nombre = "Ash"
GROUP BY E.id_entrenador

-- 9. Nombre del pokémon que ha participado de alguna batalla,  
-- junto con su tipo y el nombre de su entrenador.

-- CORRECTO --

SELECT 
    P.nombre AS nombre_pokemon, 
    T.descripcion AS pokemon_tipo, 
    E.nombre AS nombre_entrenador
FROM Pokemones AS P
JOIN Entrenadores AS E ON E.id_entrenador = P.id_entrenador
JOIN Tipos AS T ON T.id_tipo = P.id_tipo
JOIN Batallas AS B ON P.id_pokedex = B.pokemon_1 OR P.id_pokedex = B.pokemon_2
ORDER BY P.nombre;

SELECT 
    P.nombre AS nombre_pokemon, 
    T.descripcion AS pokemon_tipo, 
    E.nombre AS nombre_entrenador
FROM Pokemones AS P
JOIN Entrenadores AS E ON E.id_entrenador = P.id_entrenador
JOIN Tipos AS T ON T.id_tipo = P.id_tipo
JOIN (
    SELECT pokemon_1 AS id_pokemon FROM Batallas
    UNION
    SELECT pokemon_2 FROM Batallas
) AS B ON P.id_pokedex = B.id_pokemon
ORDER BY P.nombre;


-- INCORRECTO
SELECT P.nombre as nombre_pokemon, T.descripcion as pokemon_tipo, E.nombre as nombre_entrenador
FROM Pokemones as P 
JOIN Entrenadores as E ON E.id_entrenador = P.id_entrenador
JOIN Tipos as T ON T.id_tipo = P.id_tipo
JOIN Batallas as B ON P.id_pokedex = B.pokemon_1 OR P.id_pokedex = B.pokemon_2
WHERE P.id_pokemon = B.pokemon_1 OR P.id_pokemon = B.pokemon_2
ORDER BY P.nombre

-- 10. Detalle de las batallas donde participaron pokemones de tipo “Agua” 
-- junto al nombre de los entrenadores.
SELECT B.id_batalla as batalla_numero, B.tiempo as tiempo_batalla, E.nombre as nombre_entrenador
FROM Pokemones as P 
JOIN Entrenadores as E ON E.id_entrenador = P.id_entrenador
JOIN Tipos as T ON T.id_tipo = P.id_tipo
JOIN Batallas as B ON P.id_pokedex = B.ganador
WHERE T.descripcion = "Agua"
