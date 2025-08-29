/*
Clase 11
Daniela Serra

-----
TP VETERINARIA
Parte 1
-----

Mascota:
Id_mascota - int PK
nombre - varchar
genero - varchar
esta_vacunada - varchar
tipo - varchar
edad - entero
id_dueño - int FK


Dueño:
id_dueño - int PK
nombre - varchar
genero - varchar
edad - int


Atencion:
id_atencion PK
motivo - varchar
fecha - date
id_mascota FK


Veterinario:
id_veterinario - int PK
nombre - varchar
especialidad - varchar
experiencia - int


Atención (modificado):
id_atencion - int PK
id_mascota - int FK
fecha - date
motivo - varchar
id_veterinario - int FK


CREAR TABLA VET y ponerle datos
luego establecer relación y cargar a mano los veterinarios o 
borrar y volver a cargar la tabla atención
------------------------------------

Examen:
3 o 4 tablas.
Debemos generar los datos: hacer captura del DER que arma el motor y 
pasarselo a chatgpt para pedirle datos.


*/