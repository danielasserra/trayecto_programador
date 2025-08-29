/*----------------/ 
    Ejercicio 8
      PARTE 3 
    Biblioteca
       ***
   Daniela Serra
/----------------*/

-- Listar el título y género de todos los libros que estén disponibles.
SELECT titulo, genero
FROM Libro 

-- Listar el nombre y nacionalidad de todos los autores nacidos después de 1980.
SELECT nombre, nacionalidad 
FROM Autor

-- Seleccionar todos los libros de género "Fantasía".
SELECT titulo 
FROM Libro 
WHERE genero = "fantasia"

-- Calcular el promedio de páginas de todos los libros.
SELECT AVG(paginas)
FROM Libro 

-- Calcular el promedio de páginas de los libros de género "Novela".
SELECT AVG(paginas)
FROM Libro
WHERE genero = "Novela"

-- Contar cuántos libros hay por género.
SELECT genero, COUNT(*) as cantidad_libros
FROM Libro
GROUP BY genero

-- Listar cada libro con el nombre y nacionalidad de su autor, 
-- ordenados por el nombre del autor.
SELECT L.titulo, A.nombre, A.nacionalidad
FROM Autor as A
JOIN Libro as L ON A.id_autor = L.id_autor
ORDER BY A.nombre

-- Calcular el promedio de páginas de los libros escritos por autores argentinos.
SELECT AVG(L.paginas)
FROM Libro as L
JOIN Autor as A ON A.id_autor = L.id_autor
WHERE A.nacionalidad = "Argentina"

-- Listar título y páginas de los libros de género "Historia" 
-- cuyo autor se llame "María López".
SELECT L.titulo, L.paginas
FROM Libro as L 
JOIN Autor as A ON A.id_autor = L.id_autor
WHERE A.nombre = "Maria López"

-----------------------------------------------

-- PARTE 2

-- Listar todos los préstamos con el título del libro y la fecha de préstamo.
SELECT L.titulo, P.fecha_prestamo
FROM Prestamo as P 
JOIN Libro as L ON L.id_libro = P.id_libro

-- Obtener el nombre del autor y su libro para todos los préstamos registrados.
SELECT A.nombre, L.titulo
FROM Autor as A 
JOIN Libro as L ON A.id_autor = L.id_autor
JOIN Prestamo as P ON L.id_libro = P.id_libro

-- Listar todos los libros con su autor que hayan sido prestados al menos una vez.
SELECT DISTINCT L.titulo, A.nombre 
FROM Libro as L 
JOIN Autor as A ON A.id_autor = L.id_autor
JOIN Prestamo as P ON L.id_libro = P.id_libro

-- Obtener el título de los libros, su género y la fecha de su último préstamo.
SELECT L.titulo, L.genero, MAX(P.fecha_prestamo) as ultimo_prestamo
FROM Libro AS L 
JOIN Prestamo as P ON L.id_libro = P.id_libro
GROUP BY L.id_libro, L.titulo, L.genero


-- Listar los títulos de los libros y las fechas en que fueron prestados, 
-- ordenados por fecha.
SELECT L.titulo as Libro, P.fecha_prestamo
FROM Libro as L 
JOIN Prestamo as P ON L.id_libro = P.id_libro
ORDER BY P.fecha_prestamo


-- Obtener el título de los libros, su género y el número total de 
-- veces que han sido prestados.
SELECT L.titulo, L.genero, COUNT(P.fecha_prestamo) as veces_prestado
FROM Libro as L 
JOIN Prestamo as P ON L.id_libro = P.id_libro
GROUP BY L.id_libro, L.titulo, L.genero 

-- Listar los autores cuyos libros hayan sido prestados con una fecha de 
-- devolución posterior a 30 días desde el préstamo.
SELECT A.nombre AS Autor_Libro
FROM Autor as A 
JOIN Libro as L ON A.id_autor = L.id_autor
JOIN Prestamo as P ON L.id_libro = P.id_libro 
WHERE DATEDIFF(P.fecha_devolucion, P.fecha_prestamo) > 30

-- Obtener la cantidad de préstamos por género de libro.
SELECT L.genero, COUNT(id_prestamo) as Cantidad_prestamos
FROM Libro as L 
JOIN Prestamo as P ON L.id_libro = P.id_libro
GROUP BY L.genero

-- Listar los libros que hayan sido prestados más de 2 veces, 
-- mostrando título y nombre del autor.
SELECT L.titulo, A.nombre as nombre_autor
FROM Libro as L 
JOIN Prestamo as P ON L.id_libro = P.id_libro
JOIN Autor as A ON A.id_autor = L.id_autor
GROUP BY L.titulo, A.nombre 
HAVING COUNT(P.id_libro) > 2

-- Listar los autores y el total de préstamos que han recibido sus libros.
SELECT A.nombre as nombre_autor, COUNT(P.id_libro) as total_prestamos
FROM Libro as L 
JOIN Prestamo as P ON L.id_libro = P.id_libro
JOIN Autor as A ON A.id_autor = L.id_autor
GROUP BY A.nombre

----------------------------
-- PARTE 3

-- Listar todos los préstamos, mostrando el título del libro, la fecha 
-- y el nombre del bibliotecario que lo gestionó.
SELECT L.titulo as titulo_libro, P.fecha_prestamo as fecha_prestamo, B.nombre as nombre_bibliotecario
FROM Libro as L 
JOIN Prestamo as P ON L.id_libro = P.id_libro
JOIN Bibliotecario as B ON B.id_bibliotecario = P.id_bibliotecario


-- Obtener el nombre del autor, su libro y la especialidad del bibliotecario 
-- en cada préstamo.
SELECT A.nombre, L.titulo, B.especialidad
FROM Autor as A 
JOIN Libro as L ON A.id_autor = L.id_autor
JOIN Prestamo as P ON L.id_libro = P.id_libro
JOIN Bibliotecario as B ON B.id_bibliotecario = P.id_bibliotecario

-- Listar todos los libros con su autor y el bibliotecario que los prestó.
SELECT L.titulo as titulo_libro, A.nombre as Autor_Libro, B.nombre as nombre_bibliotecario
FROM Libro as L 
JOIN Autor as A ON A.id_autor = L.id_autor
JOIN Prestamo as P ON L.id_libro = P.id_libro
JOIN Bibliotecario as B ON B.id_bibliotecario = P.id_bibliotecario 

-- Obtener el título de los libros, su género y el número total de 
-- préstamos realizados por un bibliotecario específico.
SELECT L.titulo as titulo_libro, L.genero, COUNT(id_prestamo) as Cantidad_prestamos
FROM Libro as L 
JOIN Autor as A ON A.id_autor = L.id_autor
JOIN Prestamo as P ON L.id_libro = P.id_libro
JOIN Bibliotecario as B ON B.id_bibliotecario = P.id_bibliotecario 
GROUP BY B.nombre, L.titulo, L.genero 
ORDER BY B.nombre

-- Listar los autores y las fechas en que sus libros fueron prestados por 
-- bibliotecarios especializados en "Juvenil".
SELECT A.nombre, P.fecha_prestamo
FROM Autor as A 
JOIN Libro as L ON A.id_autor = L.id_autor
JOIN Prestamo as P ON L.id_libro = P.id_libro
JOIN Bibliotecario as B ON B.id_bibliotecario = P.id_bibliotecario
WHERE B.especialidad = "Juvenil"

-- Obtener el título de los libros, su género y el bibliotecario que más 
-- veces los ha prestado.

SELECT P.id_bibliotecario, P.id_libro, COUNT(P.id_prestamo)
FROM Prestamo as P 
GROUP BY id_bibliotecario, P.id_libro

SELECT L.titulo as titulo_libro, L.genero, COUNT(Max_bibliotecario)
FROM Autor as A 
JOIN Libro as L ON A.id_autor = L.id_autor
JOIN Prestamo as P ON L.id_libro = P.id_libro
JOIN Bibliotecario as B ON B.id_bibliotecario = P.id_bibliotecario
WHERE B.id_bibliotecario = (
  SELECT P.id_libro, MAX(P.id_bibliotecario) as Max_bibliotecario
  FROM Prestamo as P 
)

Listar los autores y las especialidades de los bibliotecarios que han gestionado préstamos de sus libros.

Listar los bibliotecarios y el número total de préstamos que han realizado.

Obtener el título de los libros prestados por bibliotecarios con más de 15 años de experiencia.

Listar los autores que han tenido al menos un préstamo gestionado por un bibliotecario especializado en "Infantil".

Obtener el nombre de los bibliotecarios y la fecha del último préstamo que realizaron.

Listar los libros, sus autores y los bibliotecarios que los han prestado, ordenados por nombre del autor.

Listar los libros gestionados por bibliotecarios con especialidad en "Adultos".

Obtener la cantidad de préstamos realizados por cada bibliotecario en el mes de septiembre de 2024.

Listar las especialidades de los bibliotecarios que han gestionado préstamos de libros de género "Fantasía".


