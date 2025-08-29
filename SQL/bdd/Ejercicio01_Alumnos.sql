-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 12-06-2025 a las 22:03:16
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Escuela`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Alumnos`
--

CREATE TABLE `Alumnos` (
  `IdAlumno` int(11) NOT NULL,
  `Nombre` varchar(20) DEFAULT NULL,
  `Apellido` varchar(15) DEFAULT NULL,
  `Localidad` varchar(18) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `NotaFinal` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Alumnos`
--

INSERT INTO `Alumnos` (`IdAlumno`, `Nombre`, `Apellido`, `Localidad`, `edad`, `NotaFinal`) VALUES
(1, 'Monica', 'Geller', 'LA', 45, 10),
(2, 'Chandler', 'Bing', 'LA', 50, 7.7),
(3, 'Rachel', 'Green', 'NY', 45, 8.5),
(4, 'Ross', 'Geller', 'NY', 60, 10),
(5, 'Joey', 'Tribbiani', 'NY', 58, 5),
(6, 'Phoebe', 'Buffay', 'NY', 45, 7),
(7, 'Maria', 'Mercedes', 'Mexico', 25, 8),
(8, 'Karina', 'La Princesita', 'Gran Buenos Aires', 40, 6),
(9, 'Principe', 'De Persia', 'Persia', 30, 8.55),
(10, 'Marcelo', 'Tinelli', 'Gran Buenos Aires', 55, 6.55);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Alumnos`
--
ALTER TABLE `Alumnos`
  ADD PRIMARY KEY (`IdAlumno`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Alumnos`
--
ALTER TABLE `Alumnos`
  MODIFY `IdAlumno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
