/*-----------/ 
     TP 7
   PARTE 3 
 Veterinaria
     ***
Daniela Serra
/-----------*/

-- Resolver las siguientes consultas:

-- a. Listar todas las atenciones, mostrando el nombre de la mascota, 
-- el motivo de la atención y el nombre del veterinario que la atendió.
SELECT M.nombre as nombre_mascota, A.motivo, V.nombre as nombre_veterinario
FROM Atencion as A 
JOIN Mascota as M ON A.id_mascota = M.id_mascota
JOIN Veterinarios as V ON A.id_veterinario = V.id_veterinario

-- b. Obtener el nombre del dueño y su mascota para todas las atenciones registradas, 
-- junto con la especialidad del veterinario.
SELECT D.nombre as nombre_dueño, M.nombre as nombre_mascota, V.especialidad 
FROM Atencion as A 
JOIN Mascota as M ON A.id_mascota = M.id_mascota
JOIN Veterinarios as V ON A.id_veterinario = V.id_veterinario
JOIN Dueño as D ON M.id_dueño = D.id_dueño

-- c. Listar todas las mascotas con el nombre de su dueño y el nombre del 
-- veterinario que las atendió.
SELECT M.nombre as nombre_mascota, D.nombre as nombre_dueño, V.nombre as nombre_veterinario
FROM Mascota as M 
JOIN Dueño as D ON M.id_dueño = D. id_dueño
JOIN Atencion as A ON M.id_mascota = A.id_mascota
JOIN Veterinarios as V ON A.id_veterinario = V.id_veterinario

-- d. Obtener el nombre de las mascotas, su tipo, y el número total de atenciones 
-- que han recibido de un veterinario específico.
SELECT M.nombre as nombre_mascota, tipo, V.nombre, COUNT(id_atencion) as total_atenciones
FROM Mascota as M 
JOIN Dueño as D ON M.id_dueño = D.id_dueño
JOIN Atencion as A ON M.id_mascota = A.id_mascota
JOIN Veterinarios as V on A.id_veterinario = V.id_veterinario
GROUP BY M.nombre, M.tipo, V.nombre

-- e. Listar los nombres de los dueños y las fechas en que sus mascotas fueron 
--atendidas por un veterinario especializado en 'Cirugía'.
SELECT D.nombre as nombre_dueño, A.fecha as fecha_atencion
FROM Mascota as M 
JOIN Dueño as D ON M.id_dueño = D.id_dueño
JOIN Atencion as A ON M.id_mascota = A.id_mascota
JOIN Veterinarios as V ON A.id_veterinario = V.id_veterinario
Where V.especialidad = "Cirugía"


-- f. Obtener el nombre de las mascotas, su tipo, y el nombre del veterinario 
-- que las ha atendido más veces.
SELECT M.nombre as nombre_mascota, tipo, V.nombre as nombre_veterinario, A.cantidad_atenciones
FROM Mascota as M 
JOIN (
  -- contar la cantidad de atenciones que recibió cada mascota por veterinario
  SELECT id_mascota, id_veterinario, COUNT(id_atencion) as cantidad_atenciones
  FROM Atencion
  GROUP BY id_mascota, id_veterinario
) as A ON M.id_mascota = A.id_mascota
JOIN Veterinarios as V ON A.id_veterinario = V.id_veterinario
JOIN (
  -- Subconsulta para obtener la máxima cantidad de atenciones por mascota
  SELECT id_mascota, MAX(cantidad_atenciones) as max_atenciones
  FROM (
    -- se repite el primer join
    SELECT id_mascota, id_veterinario, COUNT(id_atencion) as cantidad_atenciones
    FROM Atencion
    GROUP BY id_mascota, id_veterinario
  ) sub
  GROUP BY id_mascota
) maxA ON A.id_mascota = maxA.id_mascota AND A.cantidad_atenciones = maxA.max_atenciones
ORDER BY M.nombre;


-- g. Listar los dueños y las especialidades de los veterinarios que han atendido 
-- a sus mascotas.
SELECT D.nombre as nombre_dueño, V.especialidad
FROM Dueño as D 
JOIN Mascota as M ON D.id_dueño = M.id_dueño
JOIN Atencion as A ON M.id_mascota = A.id_mascota
JOIN Veterinarios as V ON A.id_veterinario = V.id_veterinario


-- h. Listar los nombres de los veterinarios y el número total de atenciones 
-- que han realizado.
SELECT V.nombre, COUNT(A.id_atencion) as cantidad_atenciones
FROM Veterinarios as V 
JOIN Atencion as A ON V.id_veterinario = A.id_veterinario
GROUP BY V.id_veterinario, V.nombre -- evitar confusion si hay dos con el mismo nombre


-- i. Obtener el nombre de las mascotas atendidas por veterinarios con 
-- más de 10 años de experiencia.
SELECT M.nombre
FROM Mascota as M 
JOIN Atencion as A ON M.id_mascota = A.id_mascota
JOIN Veterinarios as V ON A.id_veterinario = V.id_veterinario
WHERE experiencia > 10



-- j. Listar los nombres de los dueños que han tenido al menos una consulta 
-- con un veterinario especializado en 'Dermatología'.
SELECT DISTINCT D.nombre
FROM Dueño as D 
JOIN Mascota as M ON D.id_dueño = M.id_dueño
JOIN Atencion as A ON M.id_mascota = A.id_mascota
JOIN Veterinarios as V ON A.id_veterinario = V.id_veterinario
WHERE V.especialidad = "Dermatología"


-- k. Obtener el nombre de los veterinarios y la fecha de la última atención 
-- que realizaron.
SELECT V.nombre as Veterinario, A.ultima_atencion
FROM Veterinarios as V 
JOIN (
  SELECT id_veterinario, MAX(fecha) as ultima_atencion
  FROM Atencion 
  GROUP BY id_veterinario
) as A ON V.id_veterinario = A.id_veterinario


-- l. Listar las mascotas, sus dueños y los veterinarios que las han atendido, 
-- ordenando por el nombre del dueño.
SELECT M.nombre as nombre_mascota, D.nombre as nombre_dueño, V.nombre as nombre_veterinario


-- m. Listar las mascotas que han sido atendidas por veterinarios con especialidad 
-- en 'Neurología'.
SELECT DISTINCT M.nombre
FROM Mascota as M
JOIN Atencion as A ON M.id_mascota = A.id_mascota
JOIN Veterinarios as V ON A.id_veterinario = V.id_veterinario
WHERE V.especialidad = "Neurologia"

-- n. Obtener la cantidad de atenciones realizadas por cada veterinario 
-- en el mes de julio de 2024.
SELECT V.nombre as nombre_veterinario, COUNT(A.id_atencion) as cantidad_atenciones
FROM Veterinarios as V
JOIN Atencion as A ON V.id_veterinario = A.id_veterinario
WHERE fecha BETWEEN "2024/07/01" and "2024/07/31"
GROUP BY V.nombre


-- ñ. Listar las especialidades de los veterinarios que han atendido 
-- mascotas de tipo 'Perro'.
SELECT DISTINCT V.nombre as nombre_veterinario, V.especialidad
FROM Veterinarios as V 
JOIN Atencion as A ON V.id_veterinario = V.id_veterinario
JOIN Mascota as M ON A.id_mascota = M.id_mascota
WHERE M.tipo = "Perro"