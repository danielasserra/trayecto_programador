-- borrar tabla
drop TABLE Alumnos

-- crear tabla
CREATE TABLE Alumnos
(
    -- nombre del campo, tipo de campo, propiedades: auto incremental, null
    IdAlumno int AUTO_INCREMENT,
    Nombre varchar(20) NOT NULL,
    Apellido varchar(20) NOT NULL,
    Localidad varchar(30) NOT NULL,
    Edad int NULL,
    NotaFinal float NULL,
    PRIMARY KEY (IdAlumno) -- primary key (nombre del campo)
)

-- modificar estructura de tabla
ALTER TABLE Alumnos ADD column fecha_nacimiento after Apellido

-- cambiar fecha de nac de un alumno
update Alumnos 
SET fecha_nacimiento = "2014-10-20" 
WHERE IdAlumno = 8

-- agregar edad a partir de fecha de nac
update Alumnos
set edad = timestampdiff(year(fecha_nacimiento), curdate());

-- mostrar todos los datos de alumnos > 23 años
SELECT * 
FROM escuela.alumnos
WHERE TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) > "23"

-- borrar un registro
delete from alumnos
WHERE IdAlumno = 1

