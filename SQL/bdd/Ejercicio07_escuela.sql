-- BDD
-- Ejercicio Escuela
-- Daniela Serra


CREATE TABLE Escuela.Materia (
    IdMateria int AUTO_INCREMENT NOT null PRIMARY KEY, 
    Nombre varchar (40) not null, 
    Profesor varchar(40)not null
);

CREATE TABLE Escuela.Inscripciones (
    IdInscripciones INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    IdAlumnos1 INT NOT NULL,
    FOREIGN KEY (IdAlumnos1) REFERENCES Escuela.Alumnos(IdAlumno),
    IdMaterias1 INT NOT NULL,
    FOREIGN KEY (IdMaterias1) REFERENCES Escuela.Materias(IdMateria)
);

-- Para inscribir alumnos
INSERT INTO Inscripciones (IdAlumnos1, IdMaterias1)
VALUES (1,1) -- alumno 1 se anotò a materia 1