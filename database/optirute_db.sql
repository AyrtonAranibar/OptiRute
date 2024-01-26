-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-01-2024 a las 14:47:13
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.0.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `optirute_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE IF NOT EXISTS `administrador` (
  `id_administrador` int(10) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(50) NOT NULL,
  `contrasenia` char(102) NOT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `nombre_completo` varchar(50) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id_administrador`),
  UNIQUE KEY `usuario` (`usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`id_administrador`, `usuario`, `contrasenia`, `correo`, `imagen`, `nombre_completo`, `activo`) VALUES
(27, 'sandro_ucsm', 'pbkdf2:sha256:260000$DrPWI5KsDYtRVhFO$76d88e26c9a58317f1b4adc24958eb93c24d70d00db9b7c3e3e72de422c82d80', 'sandro@ucsm.edu.pe', '2022082309ivana-square.jpg', 'Sandro Cabana', 1),
(32, 'ASD', 'pbkdf2:sha256:260000$ijPnkJa7Ack1Thf4$3848a26d9b63d390e535886ddf121a8043c5ed5a05868c6ea6185a3d049a076a', 'ASD@2.COM', '2022110712ivana-square.jpg', 'ASD', 1),
(33, 'ayrton_ucsm', 'pbkdf2:sha256:260000$X6XTpTaS9P4TtJ7a$ad04b82f6e39d288eb45f745856f2e89a1e3a70f784f3e871c3db438c6574e81', '73009589@ucsm.edu.pe', '2022110848bruce-mars.jpg', 'Ayrton Aranibar', 1),
(34, 'ayrton_123', 'pbkdf2:sha256:260000$ssKVJYKXCrx9w1tU$f4b1c95836b2c987f191b9da18a7200170cca3d281d49641138fd26799534edc', 'ayrton@ucsm.edu', '2022131845bruce-mars.jpg', 'Ayrton', 1),
(35, 'sandro', 'pbkdf2:sha256:260000$TlndluugE5e2W21x$9a076d486be1ab712dec371aa85a4696bec001c917619cda0e800df3f3b7f25a', 'sandro@gmail.com', '2022125913drake.jpg', 'Sandro Cabana', 1),
(36, 'usuario_prueba', 'pbkdf2:sha256:260000$1yDoubIWVQN7mItz$5adc3e76963d2a3ed4e486421f30d004e4ef11911202c4a54bdeada13de7cf48', 'usuario_prueba@gmail.com', '2022110308bruce-mars.jpg', 'usuario_prueba', 1),
(37, 'Usuario_dePrueba', 'pbkdf2:sha256:260000$Qws5CdIwYbN4wg4i$c925e615f67ea6605b628bc41c247f1cb842df1307ea1a9dc356e98509f518d2', 'Usuario_dePrueba@gmai.com', '', 'Usuario_dePrueba', 1),
(38, 'Generalljhon', 'pbkdf2:sha256:260000$ERGZ3vJ4xdy0TC9t$95dd1120e078b1ded41e092d186c1f79e55422803fd7098ac9b2c34b761eaa73', '73009589@gmail.com', '2022151504team-2.jpg', 'Ayrton David Aranibar Castillo', 1),
(39, 'Marcelo123', 'pbkdf2:sha256:260000$KslEmSVZMbkQsHQ4$312df8240ab1c4a9b67f2f8b95b6c42a203e2f25a5b34f5013840531fd0caa61', 'marcelo@gamil.com', '', 'MArcelo', 1),
(40, 'crys', 'pbkdf2:sha256:600000$vJBa1ZdXHmypWAPL$1e0f217b864a0779ae16fbd26dd7cee94f939927b14c00070b9ad9ae82e8ab1d', 'crys@gmail.com', '', 'Crys Rey', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE IF NOT EXISTS `cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `longitud` varchar(50) DEFAULT NULL,
  `latitud` varchar(50) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `referencia` varchar(100) DEFAULT NULL,
  `numero` varchar(50) DEFAULT NULL,
  `fecha_creacion` timestamp NULL DEFAULT current_timestamp(),
  `correo` varchar(50) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id`, `nombre`, `longitud`, `latitud`, `direccion`, `referencia`, `numero`, `fecha_creacion`, `correo`, `activo`) VALUES
(1, 'Pepe', '-71.54716074746734', '-16.390746696630075', 'calle s/n     ', 'al frente de ...     ', '+51 123 456 987     ', '2022-12-08 09:45:11', 'correo@gmail.com     ', 0),
(2, 'Pepa', '-71.51987135249001', '-16.373339883440053', 'Avenida las torres ...', 'Cruce con Avenida México', '+51 555 333 444', '2022-12-14 11:48:30', 'correo@gmail.com', 0),
(3, 'Ramiro ', '-71.52593186335099', '-16.40350249187307', 'UNSA', 'Al frente de Heroes anónimos', '+51 555 333 444 ', '2022-12-08 11:56:52', 'correo@gmail.com ', 0),
(4, 'Gabriel', '-71.54454773387678', '-16.372460389586237', '117', '116 ', '+51 555 333 444 ', '2022-12-08 12:14:04', 'correo@gmail.com ', 0),
(5, 'Dany', '-71.51625877371414', '-16.39836809102944', 'Avenida Progreso', 'Palacios', '+51 888 333 222', '2022-12-09 01:02:23', 'Dany@gmail.com', 0),
(6, 'Buena vista ', '-71.54019096249195', '-16.384708432830607', 'Calle alfonso ugarte ', 'Cruce con Leon Velarde ', '+51 555 333 666 ', '2022-12-09 10:51:03', 'buena_vista@bvista.com ', 0),
(7, 'Institución Educativa 40158 El Gran Amauta ', '-71.50704584553354', '-16.375869508240854', ' Av. San Martin ', ' Cruce calle Cajamarca ', '+51 555 333 444  ', '2022-12-09 16:39:07', '40158@gmail.com  ', 1),
(8, 'Fortunata Gutiérrez de Bernedo', '-71.53962089138939', '-16.404359086815646', 'CALLE LA MERCED 513', 'CALLE LA MERCED 513', '+51  777 777 777', '2023-10-12 04:52:35', '', 1),
(9, 'Gilberto Ochoa Galdos', '-71.52289663426855', '-16.408690288881644', 'BANCO DE LA NACION B-8', 'BANCO DE LA NACION B-8', '+51 222 222 222', '2023-10-12 04:56:21', '', 1),
(10, 'Hogar de Abuelitos San Vicente De Paúl', '-71.52798219403057', '-16.400548467394074', 'CALLE SAN CAMILO 514', 'CALLE SAN CAMILO 514', '+51 666  444  666', '2023-10-12 05:04:11', '', 1),
(11, 'I.E. 40143 San Pedro', '-71.53869268672186', '-16.41846084203607', 'PABLO VI ETAPA II', 'PABLO VI ETAPA II', '+51 666  333  222', '2023-10-12 05:19:37', '', 1),
(12, '40001 Luis H. Bouroncle', '-71.52933191234312', '-16.39252239188805', 'CALLE PERAL 710', 'CALLE PERAL 710', '+51 444 222  333', '2023-10-12 06:20:06', '', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entregas`
--

CREATE TABLE IF NOT EXISTS `entregas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT 1,
  `fecha` timestamp NULL DEFAULT current_timestamp(),
  `fecha_entrega` timestamp NULL DEFAULT current_timestamp(),
  `estado` tinyint(1) DEFAULT 1 COMMENT '0:Entregado 1:Por entregar 2:Cancelado',
  `activo` tinyint(4) NOT NULL DEFAULT 1 COMMENT '0:eliminado 1:activo',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `entregas`
--

INSERT INTO `entregas` (`id`, `cliente_id`, `producto_id`, `cantidad`, `fecha`, `fecha_entrega`, `estado`, `activo`) VALUES
(1, 6, 2, 15, '2023-10-02 23:14:03', '2023-10-11 18:13:00', 0, 0),
(2, 4, 1, 1, '2023-10-02 23:14:03', '2023-10-02 23:14:03', 1, 0),
(4, 7, 2, 50, '2023-10-09 06:46:48', '2023-10-11 05:00:00', 2, 0),
(5, 6, 1, 15, '2023-10-09 21:23:14', '2023-10-12 05:00:00', 3, 0),
(6, 3, 1, 50, '2023-10-11 07:31:41', '2023-10-14 23:14:03', 0, 0),
(7, 3, 1, 1, '2023-10-11 07:35:20', '2023-10-13 23:14:03', 0, 0),
(8, 7, 2, 50, '2023-10-11 07:48:02', '2023-10-02 23:14:03', 2, 0),
(9, 5, 2, 30, '2023-10-11 08:04:44', '2023-10-13 10:08:00', 1, 0),
(10, 9, 1, 15, '2023-11-03 00:02:02', '2023-11-02 05:00:00', 1, 1),
(11, 7, 2, 50, '2023-11-03 00:10:37', '2023-11-04 00:10:00', 0, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `peso` float DEFAULT NULL COMMENT 'Peso en kg',
  `descripcion` varchar(150) DEFAULT NULL,
  `precio` float DEFAULT NULL COMMENT 'Precio en dolares',
  `activo` tinyint(4) DEFAULT 1 COMMENT '1:activo 0:inactivo',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `peso`, `descripcion`, `precio`, `activo`) VALUES
(1, 'Mesa', 10, 'Una mesa de madera', 50.5, 1),
(2, 'Silla', 7, 'Silla estándar', 20, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sede`
--

CREATE TABLE IF NOT EXISTS `sede` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_sede` varchar(50) NOT NULL,
  `direccion_sede` varchar(50) DEFAULT NULL,
  `longitud` varchar(30) DEFAULT NULL,
  `latitud` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_sede` (`nombre_sede`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `sede`
--

INSERT INTO `sede` (`id`, `nombre_sede`, `direccion_sede`, `longitud`, `latitud`) VALUES
(1, 'Pepe', 'Calle Sevilla', '-71.54365540685632', '-16.390847948483326');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transportista`
--

CREATE TABLE IF NOT EXISTS `transportista` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `usuario` varchar(50) DEFAULT NULL,
  `contraseña` varchar(500) DEFAULT NULL,
  `numero` varchar(50) DEFAULT NULL,
  `correo` varchar(150) DEFAULT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `transportista`
--

INSERT INTO `transportista` (`id`, `nombre`, `usuario`, `contraseña`, `numero`, `correo`, `imagen`, `activo`) VALUES
(1, '0', 'Julian123', 'pbkdf2:sha256:260000$63SP5A7OMyMH7bHH$dfbc619a11a6fa27ab5d9302cb4e57a69c3a27322d798a2ccf58e686de8978b7', '+51 555 884 633', 'julian@gmail.com', '2022014911dany2.jpg', 0),
(2, '0', 'pablo123', 'pbkdf2:sha256:260000$czC5HFNSBsUFutxt$69cf06bb8234d2fbf47ad3ff6dd8ebd89697372c27eea362015fe0eea0a0540f', '+51 856 321 321', 'pablo@gmail.com', '2022022900dextre.png', 0),
(3, '0', 'pepe123', 'pbkdf2:sha256:260000$yTmiw6nu79oMXsRH$5b75627dbf71c1cb20ffcd8657e38367587d62043610f8029ad509a87a2350f6', '+51 999 333 444', 'pepe@gmail.com', '2022024013dextre.png', 0),
(4, '0', 'pepe2', 'pbkdf2:sha256:260000$6TFXAbmAuS8yv2UL$ca8e3b2aea785ca42cd829ea1be5f4b455118cd76f43eab50402226ac55d0967', 'pepe2', 'pepe2@gmail.com', '2022024101es_cine.PNG', 0),
(5, '0', 'pepe2', 'pbkdf2:sha256:260000$4iEPHe8PPDiQY8mN$43234b0073ee2a9ed5baa9396f2981aa096026c1a3c67c2801dd4d5bf5e8c0dd', 'pepe2', 'pepe2@gmail.com', '2022024146es_cine.PNG', 0),
(6, '0', 'pepe123', 'pbkdf2:sha256:260000$Lbqb7mvUsN72lbUo$cb9999f6449e19416a9edcebc722cdd5dc8d20073e0bff75f34e2f003ae173e5', '+51 999 333 444', 'pepe@gmail.com', '2022024250dextre.png', 0),
(7, '0', 'pepe123', 'pbkdf2:sha256:260000$UiRB9KEx1Bprv2Ga$8af1b3a6d7d2100c2efd25c1b4f8ea46ab573ff81630fe97b2c2f95d8bb850f1', '+51 999 333 444', 'pepe@gmail.com', '2022024509dextre.png', 0),
(8, '0', 'Pepe', 'pbkdf2:sha256:260000$IZZqyv1GOSBSi2GA$7c48c30d519202064b248b002079c8ebbf2e5943fe4d36004ca5315ed262aa64', 'Pepe', 'Pepe', '2022024701despues.jpg', 0),
(9, '0', 'cocina123', 'pbkdf2:sha256:260000$UuIm2ayn9fXelS19$8503bd7c6d269646949e803a5788126bbfaad08f68b59ad707f8e11203a0a564', '+51 999 333 444', 'enrique@gmail.com', '2022025447dany2.jpg', 0),
(10, '123', '123', 'pbkdf2:sha256:260000$slLzaEF4e6f5J3D5$792b2dde4d5b1319306ccab4be3e8030e9bad889adee953613ccba228c9a7c33', '123', '123', '2022025638dany2.jpg', 0),
(11, '0', 'mathias123', 'pbkdf2:sha256:260000$9t2ArhGYlfbp3LFN$aa645565c93d89e1c329747c12bf946c4383c14705371f08b3bd7930881b95f6', '+51 888 333 222', 'mathias@gmail.com', '2022025733dany_con_plata.PNG', 0),
(12, 'Mathias', 'mathias123', 'pbkdf2:sha256:260000$8DxUfSqnhzKDjyqv$32cef79a297f8e65aa465a2cdab2608aff75618e4cbb7a5bdd5b679ca5e3357b', '+51 555 333 666', 'mathias@gmail.com', '2022025858yerson.jpg', 0),
(13, 'Mario', 'MarioMartinez12', 'pbkdf2:sha256:600000$izlxDvtDgxAjA1fv$90f24fc6ef16ed9220370be67f47d6785c9908d2bfc14c932170c136cda7fed4', '+51 000 000 000', 'mario@gmail.com', '2023032022hyunwon-jang-bIkRZwv7CZg-unsplash.jpg', 0),
(14, 'Mario1', 'MarioMartinez11', '0', '+51 000 000 001', 'mario@gmail.com1', '2023033136chelotor.jpg', 0),
(15, 'Javier', 'Milei', 'None', '+51 000 000 00', 'mario@gmail.com', '2023233902chelo1414.jfif', 1),
(16, 'Pepe  ', 'Generalljhon', 'pbkdf2:sha256:600000$sCnUsmg9L9WgZ1Jk$82b3edc7d83650f49f7f9ebb091d451706e21f0226e3d5f9ce129dde044e159e', '+51 555 333 444  ', 'enrique@gmail.com  ', '2023030000chelotor.jpg', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculo`
--

CREATE TABLE IF NOT EXISTS `vehiculo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` tinyint(1) DEFAULT 1 COMMENT '0:No disponible 1:disponible 2:En ruta',
  `placa` varchar(50) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT 1,
  `imagen` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `vehiculo`
--

INSERT INTO `vehiculo` (`id`, `estado`, `placa`, `activo`, `imagen`) VALUES
(1, 2, 'F5U - 597    ', 1, '2023231731descarga (1).jpg'),
(2, 1, 'F5U - 603', 0, ''),
(3, 0, 'F5U - 55', 0, ''),
(4, 0, 'F5U - 603 ', 1, '2023183119descarga.jpg');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
