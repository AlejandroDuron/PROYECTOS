

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

drop database if exists `SIGER`;

CREATE DATABASE IF NOT EXISTS `SIGER` ;
USE `SIGER`;

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(250) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fecha_registro` date NOT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES 
(1,'Ignaz Poupard','88266 Warrior Crossing','1(602)485-8247','ipoupard0@usa.gov','2024-07-01'),
(2,'Luz Tousey','6396 Crest Line Alley','86(440)752-0275','ltousey1@earthlink.net','2024-04-18'),
(3,'Godfrey Gude','83 Coolidge Road','380(739)119-9901','ggude2@virginia.edu','2024-10-18'),
(4,'Gustave OHannay','103 Charing Cross Junction','86(673)729-6147','gohannay3@trellian.com','2024-10-30'),
(5,'Xenos Audley','2928 Prairieview Court','62(354)284-3683','xaudley4@hhs.gov','2024-12-21'),
(6,'Emanuel Bevan','0110 Westerfield Parkway','93(650)478-3818','ebevan5@java.com','2025-02-05'),
(7,'Nomi Allsup','52477 Farragut Crossing','420(129)536-5189','nallsup6@dell.com','2024-10-10'),
(8,'Harmon Carp','9 Bayside Drive','420(826)136-8718','hcarp7@tumblr.com','2024-05-15'),
(9,'Craggy Hammon','7 Arrowood Court','967(404)240-2316','chammon8@lulu.com','2025-01-05'),
(10,'Anica Godfray','268 Fulton Trail','380(599)153-9958','agodfray9@xing.com','2024-11-11');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deduccion_fiscal`
--

DROP TABLE IF EXISTS `deduccion_fiscal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deduccion_fiscal` (
  `ID_deduccion` int(11) NOT NULL AUTO_INCREMENT,
  `ID_factura` int(11) DEFAULT NULL,
  `ID_cliente` int(11) DEFAULT NULL,
  `Monto_deduccion` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID_deduccion`),
  KEY `ID_factura` (`ID_factura`),
  KEY `ID_cliente` (`ID_cliente`),
  CONSTRAINT `deduccion_fiscal_ibfk_1` FOREIGN KEY (`ID_factura`) REFERENCES `factura` (`id_factura`),
  CONSTRAINT `deduccion_fiscal_ibfk_2` FOREIGN KEY (`ID_cliente`) REFERENCES `clientes` (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deduccion_fiscal`
--

LOCK TABLES `deduccion_fiscal` WRITE;
/*!40000 ALTER TABLE `deduccion_fiscal` DISABLE KEYS */;
INSERT INTO `deduccion_fiscal` VALUES 
(1,1,1,2.44),
(2,2,2,55.08),
(3,3,3,1695.00),
(4,4,4,678.00),
(5,5,5,5650.00),
(6,6,6,1186.50),
(7,7,7,50.85),
(8,8,8,3390.00),
(9,9,9,13560.00),
(10,10,10,283.06);
/*!40000 ALTER TABLE `deduccion_fiscal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_factura`
--

DROP TABLE IF EXISTS `detalle_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_factura` (
  `ID_detalle` int(11) NOT NULL AUTO_INCREMENT,
  `ID_factura` int(11) DEFAULT NULL,
  `ID_producto` int(11) DEFAULT NULL,
  `Cantidad` int(11) DEFAULT NULL,
  `Subtotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID_detalle`),
  KEY `ID_factura` (`ID_factura`),
  KEY `ID_producto` (`ID_producto`),
  CONSTRAINT `detalle_factura_ibfk_1` FOREIGN KEY (`ID_factura`) REFERENCES `factura` (`id_factura`),
  CONSTRAINT `detalle_factura_ibfk_2` FOREIGN KEY (`ID_producto`) REFERENCES `productos` (`ID_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_factura`
--

LOCK TABLES `detalle_factura` WRITE;
/*!40000 ALTER TABLE `detalle_factura` DISABLE KEYS */;
INSERT INTO `detalle_factura` VALUES 
(1,1,1,2,2.16),
(2,2,2,5,48.75),
(3,3,3,6,1500.00),
(4,4,4,3,600.00),
(5,5,5,1,5000.00),
(6,6,6,7,1050.00),
(7,7,7,3,45.00),
(8,8,8,2,3000.00),
(9,9,9,4,12000.00),
(10,10,10,1,250.50);
/*!40000 ALTER TABLE `detalle_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `id_factura` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) DEFAULT NULL,
  `fecha_factura` date DEFAULT NULL,
  `estado_factura` varchar(20) NOT NULL,
  `monto` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_factura`),
  KEY `Factura_Clientes_FK` (`id_cliente`),
  CONSTRAINT `Factura_Clientes_FK` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES 
(1,1,'2024-11-19','Anulada',2.16),
(2,2,'2024-05-26','Pagada',48.75),
(3,3,'2025-02-21','Pendiente por pagar',1500.00),
(4,4,'2024-06-09','Pendiente por pagar',600.00),
(5,5,'2024-12-11','Pagada',5000.00),
(6,6,'2025-03-01','Anulada',1050.00),
(7,7,'2024-07-19','Pendiente por pagar',45.00),
(8,8,'2024-06-11','Anulada',3000.00),
(9,9,'2024-08-18','Pendiente por pagar',12000.00),
(10,10,'2024-04-11','Anulada',250.50);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `importadores`
--

DROP TABLE IF EXISTS `importadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `importadores` (
  `ID_importador` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_importador` varchar(100) DEFAULT NULL,
  `Contacto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_importador`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `importadores`
--

LOCK TABLES `importadores` WRITE;
/*!40000 ALTER TABLE `importadores` DISABLE KEYS */;
INSERT INTO `importadores` VALUES 
(1,'CEICA EL SALVADOR','22888994'),
(2,'ORBITEC EL SALVADOR','22897645'),
(3,'PRESTELECTRO','22546775'),
(4,'SEESA','22228178'),
(5,'Prielectro','22134567'),
(6,'Elektro EL SALVADOR','22543678'),
(7,'Importadora Premium El Salvador','22220087'),
(8,'Schneider Electric','22546568'),
(9,'Importadora Universal','22212323'),
(10,'Distribuidora Tamira','22643989');
/*!40000 ALTER TABLE `importadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `info_clientes`
--

DROP TABLE IF EXISTS `info_clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info_clientes` (
  `ID_cliente` int(11) NOT NULL,
  `Preferencias_envio` varchar(255) DEFAULT NULL,
  `Historial_compras` text DEFAULT NULL,
  PRIMARY KEY (`ID_cliente`),
  CONSTRAINT `info_clientes_ibfk_1` FOREIGN KEY (`ID_cliente`) REFERENCES `clientes` (`id_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info_clientes`
--

LOCK TABLES `info_clientes` WRITE;
/*!40000 ALTER TABLE `info_clientes` DISABLE KEYS */;
INSERT INTO `info_clientes` VALUES 
(1,'Delivery','Implementos de conexión'),
(2,'Delivery','Implementos de conexión'),
(3,'Retiro Sucursal','Implementos de conexión'),
(4,'Delivery','Mantenimiento'),
(5,'Delivery','Mantenimiento'),
(6,'Delivery','Implementos de conexión'),
(7,'Delivery','Implementos aislantes'),
(8,'Delivery','Implementos de conexión'),
(9,'Delivery','Mantenimiento'),
(10,'Retirro Sucursal','Implementos aislantes');
/*!40000 ALTER TABLE `info_clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `ID_producto` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_producto` varchar(100) DEFAULT NULL,
  `Precio` decimal(10,2) DEFAULT NULL,
  `Descripcion` text DEFAULT NULL,
  `ID_proveedor` int(11) DEFAULT NULL,
  `ID_importador` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_producto`),
  KEY `ID_proveedor` (`ID_proveedor`),
  KEY `Productos_Importadores_FK` (`ID_importador`),
  CONSTRAINT `Productos_Importadores_FK` FOREIGN KEY (`ID_importador`) REFERENCES `importadores` (`ID_importador`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`ID_proveedor`) REFERENCES `proveedores` (`ID_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES 
(1,'Interruptor Sencillo Eagle 15 AMP-120V',1.08,'Interruptor eléctrico de uso residencial o comercial, diseñado para controlar el encendido y apagado de luces u otros dispositivos eléctricos.​',1,1),
(2,'Conector NEMA Eagle 20A, 125V, 2P-3W ',9.75,'Conector eléctrico industrial, diseñado para conexiones seguras y duraderas.',2,2),
(3,'Transformador de corriente',250.00,'Estos interruptores protegen las instalaciones eléctricas de sobrecargas o cortocircuitos. Se utilizan en sistemas de distribución de media tensión para garantizar la seguridad y el control del flujo eléctrico.',3,3),
(4,'Interruptores automáticos de media tensión',200.00,'Cables diseñados para soportar altas temperaturas y garantizar un flujo eléctrico seguro en aplicaciones industriales y residenciales.',4,4),
(5,'Transformador de potencia',5000.00,'Es un equipo esencial para la distribución eléctrica en subestaciones, utilizado para transformar el voltaje en sistemas de alta potencia.',5,5),
(6,'Tableros eléctricos de distribución',150.00,'Dispositivos utilizados para distribuir la electricidad de manera segura en instalaciones comerciales e industriales. Incluye interruptores, fusibles, medidores y otras herramientas.',6,6),
(7,'Fusibles de alta capacidad',15.00,' Los fusibles se utilizan para proteger los equipos eléctricos contra sobrecargas de corriente. Son una opción común en sistemas industriales y eléctricos residenciales.',7,7),
(8,'Generadores eléctricos industriales',1500.00,' Dispositivos de generación de electricidad utilizados en fábricas, hospitales y grandes instalaciones que requieren un suministro de energía constante y fiable.',8,8),
(9,'Sistemas de energía solar fotovoltaica',3000.00,'Paneles solares y otros componentes necesarios para captar la energía del sol y convertirla en electricidad. Es una opción renovable popular para empresas y hogares que buscan reducir costos de energía.',9,9),
(10,'Medidores de energía digital',250.50,'Dispositivos utilizados para medir el consumo eléctrico en instalaciones industriales y comerciales. Los medidores digitales proporcionan datos precisos y son fáciles de leer.',10,10);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `ID_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_proveedor` varchar(100) DEFAULT NULL,
  `Contacto` varchar(100) DEFAULT NULL,
  `Telefono` varchar(20) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES 
(1,'Nombre Proveedor 1','0000-0000','0000-0000','proveedor1@gmail.com'),
(2,'Nombre Proveedor 2','1000-1000','1000-1000','proveedor2@gmail.com'),
(3,'Nombre Proveedor 3','1100-1100','1100-1100','proveedor3@gmail.com'),
(4,'Nombre Proveedor 4','1110-1110','1110-1110','proveedor4@gmail.com'),
(5,'Nombre Proveedor 5','1111-1111','1111-1111','proveedor5@gmail.com'),
(6,'Nombre Proveedor 6','0111-0111','0111-0111','proveedor6@edu.sv'),
(7,'Nombre Proveedor 7','0011-0011','0011-0011','proveedor7@gmail.com'),
(8,'Nombre Proveedor 8','0001-0001','0001-0001','proveedor8@yahoo.com'),
(9,'Nombre Proveedor 9','10000-1000','10000-1000','proveedor9@gmail.com'),
(10,'Nombre Proveedor 10','11100-0011','11100-0011','proveedor10@outlookcom');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicios_profesionales`
--

DROP TABLE IF EXISTS `servicios_profesionales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicios_profesionales` (
  `ID_servicio` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_servicio` varchar(100) DEFAULT NULL,
  `Precio` decimal(10,2) DEFAULT NULL,
  `ID_proveedor` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_servicio`),
  KEY `ID_proveedor` (`ID_proveedor`),
  CONSTRAINT `servicios_profesionales_ibfk_1` FOREIGN KEY (`ID_proveedor`) REFERENCES `proveedores` (`ID_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios_profesionales`
--

LOCK TABLES `servicios_profesionales` WRITE;
/*!40000 ALTER TABLE `servicios_profesionales` DISABLE KEYS */;
INSERT INTO `servicios_profesionales` VALUES
 (1,'Nombre Servicio 1',100.02,1),
 (2,'Nombre Servicio 2',1229.12,2),
 (3,'Nombre Servicio 3',400.22,3),
 (4,'Nombre Servicio 4',107.21,4),
 (5,'Nombre Servicio 5',900.21,5),
 (6,'Nombre Servicio 6',3333.33,6),
 (7,'Nombre Servicio 7',1234.21,7),(
  8,'Nombre Servicio 8',987.21,8),
  (9,'Nombre Servicio 9',999.99,9),
  (10,'Nombre Servicio 10',4122.12,10);
/*!40000 ALTER TABLE `servicios_profesionales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'siger'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-28 20:15:35
