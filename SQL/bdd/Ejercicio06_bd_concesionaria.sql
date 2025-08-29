-- BDD
-- Ejercicio Concesionaria
-- Daniela Serra

CREATE database bd_concesionaria

CREATE TABLE bd_concesionaria.cliente (
    IdCliente int AUTO_INCREMENT NOT null PRIMARY KEY, 
    nombre varchar (40) not null, 
    apellido varchar(40)not null
);

CREATE TABLE bd_concesionaria.vehiculo (
    IdVehiculo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    marca VARCHAR(40) NOT NULL,
    modelo VARCHAR(40) NOT NULL,
    anio INT NOT NULL,
    IdCliente1 INT NOT NULL,
    FOREIGN KEY (IdCliente1) REFERENCES bd_concesionaria.cliente(IdCliente)
);
