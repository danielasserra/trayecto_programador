/* 
Clase 08
Daniela Serra

--- ¿Qué es una entidad? ----
Datos a manejar y cómo se relacionan esos datos
Diagrama que nos permita establecer 
cuáles son los datos que tengo que modelar y 
cuáles son las relaciones que existen entre esos datos


¿Como representamos una entidad?
Con cuadrado

La entidad puede tener atributos (caracteristicas de una tabla):
Se representan con óvalos
Ej. sobre alumnos: edad, fecha de nacimiento, etc

-- Las relaciones --
Las representamos a traves de un rombo
Tienen un nombre y nos permiten unir de forma logica dos tablas

-- Cardinalidad --
cuantos elementos de una entidad puedo relacionar con cuantos elementos de otra entidad
Ej. Alumnos - Localidades
1 alumno tiene una localidad
pero una localidad puede tener muchos alumnos
Relacion de uno a muchos


-- Clave primaria --
Subrayado y en negrita

-- Atributo derivable --
Atributos que se pueden calcular como la edad. Se hace un cálculo con otro atributo


-- TABLA INTERMEDIA
las relaciones de muchos a muchos llevan una tabla intermedia.
Ej. Alumnos - Cursos 
un alumno se puede inscribir a muchos cursos y un curso puede tener muchos alumnos
los datos se empiezan a repetir
deriva en tabla de inscripciones: id_alumno, id_curso, fecha_inscripcion
Cuando encuentre una relacion de muchos a muchos, tienen que salir campos: codigo inscripcion y fecha inscripcion

