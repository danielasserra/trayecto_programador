-- Clase 08
-- Daniela Serra

/* Draw.io Bosquejo para visualizar la info antes de crear la tabla de datos
 N = muchos
 1 = unico (en este caso, carrera)
 N1 muchos estudian esa carrera

Clave Foranea = FK . No es clave principal en esta tabla, es PK en otra tabla.
De esta forma se vinculan las tablas.
Ej.
Tabla de alumnos + tabla de carreras
IdAlumno, todos los datos (nombre, localidad, etc) agregar IdCarrera para unirlo a esa tabla

-- MYSQL --
PASO A PASO
1. CREAR LA SEGUNDA TABLA (carreras) 
*/

CREATE TABLE Carreras (
    IdCarrera INT AUTO_INCREMENT PRIMARY KEY,
    nombre_carrera VARCHAR(40) NOT NULL
);

-- 2. agregar una columna a la tabla existente
ALTER TABLE Alumnos
ADD COLUMN IdCarrera1 INT,
ADD FOREIGN KEY (IdCarrera1) REFERENCES Carreras(IdCarrera);

/* clave foranea (pk de otra tabla): coma FOREIGN KEY(IdCarrera1) REFERENCES (NOMBRE DE TABLA: Carreras(IdCarrera))
ASI LO PASO LA PROFE:
MOdificar una tabla para agregar 1 campo y hacer ese campo clave foranea:
alter table nombre_tabla add column nombre_campo int,
add FOREIGN KEY (nombre_FK_en_tabla_actual) REFERENCES Nombre_Tabla_donde_esPK (PK_en tabla original)*/

ALTER TABLE Carreras
ADD COLUMN duracion INT,
ADD COLUMN jefe_carrera VARCHAR(100);

INSERT INTO Carreras (nombre_carrera, duracion, jefe_carrera) 
VALUES ("Desarrollo", 2, "Juan Perez");

UPDATE Alumnos
SET IdCarrera1 = 1
WHERE IdCarrera1 IS NULL;


/*
N:M = relacion de muchos a muchos. Ej: Alumnos, materias. 
Puede haber muchos alumnos en una materia y a la vez, puede haber varias materias en un alumno
*/ 