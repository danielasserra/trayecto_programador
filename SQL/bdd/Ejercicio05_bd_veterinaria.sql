-- BDD
-- Ejercicio Veterinaria
-- Daniela Serra

-- Crear la tabla Mascotas en BDD Veterinaria 
CREATE TABLE Mascotas 
(
    -- nombre del campo, tipo de campo, propiedades: auto incremental, null
    IdMascota int AUTO_INCREMENT,
    Nombre varchar(20) NOT NULL,
    Especie varchar(15) NOT NULL,
    Raza varchar(20) NOT NULL,
    Edad int NULL,
    Peso float NULL,
    FechaNacimiento date NOT NULL,
    primary key(IdMascota),
)

-- agregar 10 datos a la tabla

INSERT INTO Veterinaria (Nombre, Especie, Raza, Edad, Peso, FechaNacimiento) VALUES
('Luna', 'Perro', 'Labrador', 5, 24.5, '2019-05-12'),
('Simba', 'Gato', 'Siamés', 3, 4.3, '2021-08-20'),
('Rocky', 'Perro', 'Bulldog', 6, 22.0, '2018-03-10'),
('Milo', 'Gato', 'Maine Coon', 2, 6.1, '2022-02-14'),
('Nala', 'Conejo', 'Holland Lop', 1, 1.5, '2023-04-01'),
('Toby', 'Perro', 'Beagle', 7, 13.2, '2017-06-25'),
('Mía', 'Gato', 'Persa', 4, 5.0, '2020-09-30'),
('Kira', 'Hámster', 'Sirio', NULL, 0.15, '2024-01-10'),
('Boby', 'Perro', 'Golden Retriever', 8, 29.4, '2016-12-03'),
('Lola', 'Gato', 'Bengalí', 3, NULL, '2021-10-22');

-- Nombre y especie de las mascotas cuya edad esté entre 2 y 10 años inclusive, y que pesen menos de 20 kg.
SELECT Nombre, Especie 
FROM Mascotas
WHERE (Edad between 2 and 10) and (Peso < 20)

-- Raza y peso de la mascota con IdMascota = 7, si su peso es mayor a 5 kg.
SELECT Raza, Peso
FROM Mascotas
WHERE (IdMascota = 7) and Peso > 5

-- Todos los datos de las mascotas cuyo IdMascota esté entre 3 y 8 y cuya raza sea 
-- 'Caniche' o 'Labrador', ordenadas por peso descendente.
SELECT *
FROM Mascotas
WHERE (IdMascota between 3 and 8) and (Raza = "Caniche" or Raza = "Labrador")
ORDER BY Peso DESC

-- Nombre, especie y peso de las mascotas con peso mayor a 10 kg o que tengan más 
-- de 8 años.
SELECT Nombre, Especie, Peso
FROM Mascotas
WHERE Peso > 10 or Edad > 8

-- Nombre y especie de mascotas cuyo nombre empiece con 'B' o 'L'.
SELECT Nombre, Especie
FROM Mascotas
WHERE Nombre like "B%" or Nombre like "L%"

-- Nombre, especie y edad de mascotas que no tengan peso registrado (peso es NULL).
SELECT Nombre, Especie, Edad
FROM Mascotas
WHERE Peso is NULL

-- Nombre y especie de las mascotas que nacieron antes del 15/08/2020 
-- y pesan más de 7 kg.
SELECT Nombre, Especie
FROM Mascotas
WHERE (FechaNacimiento < "20200815") and (Peso > 7)

-- Nombre y especie de las mascotas que nacieron en julio 
-- (independientemente del año).
SELECT Nombre, Especie
FROM Mascotas
WHERE month(FechaNacimiento) = 7

-- Nombre y especie de las mascotas que nacieron entre dos fechas 
-- (exclusivamente) — 01/01/2018 y 31/12/2020.
SELECT Nombre, Especie
FROM Mascotas
WHERE FechaNacimiento between "20180101" and "20201231"

-- Agregar el campo sexo y asignar “Macho” a los registro de id par y 
-- “Hembra” a los registros de id impar
ALTER TABLE Mascotas
ADD Sexo varchar(10) NULL

UPDATE Mascotas
SET Sexo = "Macho"
WHERE IdMascota%2!=0

UPDATE Mascotas
SET Sexo = "Hembra"
WHERE IdMascota%2=0

-- Asignar la raza  “Mestizo” a los perros que pesen entre 10 y 15 kg
UPDATE Mascotas
SET Raza = "Mestizo"
WHERE (Especie = "Perro") and (Peso BETWEEN 10 and 15)

-- Asignar la especie “Gato” a los animales que pesen menos de 5.5 kg
UPDATE Mascotas
SET Especie = "Gato"
WHERE Peso < 5.5

-- Aumentar la edad en 2 años a los animales que hayan nacido antes del 2020
UPDATE Mascotas
SET Edad = Edad + 2
WHERE year(FechaNacimiento) < 2020

-- Mostrar el promedio de edad agrupado por especie redondeando
SELECT Especie, ROUND(AVG(Edad),2) as PromedioEdad
From Mascotas
GROUP BY Especie

-- Mostrar el promedio de peso redondeado a 2 decimales agrupado por especie 
-- siempre que el peso sea menor a 15 kg
SELECT Especie, ROUND(AVG(Peso),2) as PromedioPeso
FROM Mascotas
WHERE Peso < 15
GROUP BY Especie

-- Indicar cuántas mascotas hay de cada raza cuya edad esté entre 2 y 8 años. 
-- Mostrar los resultados ordenados de mayor a menor cantidad.
SELECT Raza, COUNT(IdMascota) AS Cantidad
FROM Mascotas
WHERE Edad BETWEEN 2 AND 8
GROUP BY Raza
ORDER BY Cantidad DESC;

-- Calcular el promedio de edad de las gatas hembra
SELECT Especie, Sexo, AVG(Edad) AS PromedioEdad
FROM Mascotas
WHERE Especie = 'Gato' AND Sexo = 'Hembra' AND Edad IS NOT NULL;

-- Eliminar a todos los perros que tengan más de 15 años
DELETE
FROM Mascotas
WHERE Especie = "Perro" AND Edad > 15

-- Eliminar a los gatos que pesen más de 5 kg y hayan nacido antes del 2020
DELETE
FROM Mascotas
WHERE Especie = "Gato" AND Peso > 5 AND year(FechaNacimiento) < 2020

-- Eliminar las mascotas nacidas entre abril y junio de 2022, sin importar el día
DELETE 
FROM Mascotas
WHERE FechaNacimiento BETWEEN '2022-04-01' AND '2022-06-30';

-- Eliminar todas las mascotas cuyo nombre comience con “X” o “Z”, sin importar la especie ni la raza.
DELETE
FROM Mascotas
WHERE nombre like "x%" or NOMBRE like "z%"

-- Mostrar cuantas mascotas hay por especie, solo mostrar las especies que 
-- contabilicen más de 3 mascotas
SELECT Especie, COUNT(IdMascota) as Cantidad
FROM Mascotas
GROUP BY Especie
HAVING Cantidad > 3

-- Mostrar el promedio de peso por raza pero únicamente de las razas cuyo 
-- promedio pese más de 10 kg
SELECT Raza, ROUND(AVG(Peso),2)
FROM Mascotas
GROUP BY Raza
HAVING AVG(PESO) > 10