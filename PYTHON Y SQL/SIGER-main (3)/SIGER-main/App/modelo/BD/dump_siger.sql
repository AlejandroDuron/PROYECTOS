-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: siger
-- ------------------------------------------------------
-- Server version	11.8.2-MariaDB

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

-- Create database
CREATE DATABASE IF NOT EXISTS siger;
USE siger;

--
-- Table structure for table `clientes`
--

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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Juan Pérez','Calle Principal 123, Ciudad','555-1234','juan.perez@email.com','2024-01-15'),(2,'María García','Avenida Central 456, Ciudad','555-5678','maria.garcia@email.com','2024-02-20'),(3,'Carlos López','Boulevard Norte 789, Ciudad','555-9012','carlos.lopez@email.com','2024-03-10'),(4,'Ana Martínez','Calle Sur 321, Ciudad','555-3456','ana.martinez@email.com','2024-04-05'),(5,'Luis Rodríguez','Avenida Este 654, Ciudad','555-7890','luis.rodriguez@email.com','2024-05-12'),(6,'Juan Pérez','Calle Principal 123, Ciudad','555-1234','juan.perez@email.com','2024-01-15'),(7,'María García','Avenida Central 456, Ciudad','555-5678','maria.garcia@email.com','2024-02-20'),(8,'Carlos López','Boulevard Norte 789, Ciudad','555-9012','carlos.lopez@email.com','2024-03-10'),(9,'Ana Martínez','Calle Sur 321, Ciudad','555-3456','ana.martinez@email.com','2024-04-05'),(10,'Luis Rodríguez','Avenida Este 654, Ciudad','555-7890','luis.rodriguez@email.com','2024-05-12');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deduccion_fiscal`
--

DROP TABLE IF EXISTS `deduccion_fiscal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deduccion_fiscal` (
  `id_deduccion` int(11) NOT NULL AUTO_INCREMENT,
  `id_factura` int(11) DEFAULT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `monto_deduccion` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_deduccion`),
  KEY `id_factura` (`id_factura`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `deduccion_fiscal_ibfk_1` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id_factura`),
  CONSTRAINT `deduccion_fiscal_ibfk_2` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deduccion_fiscal`
--

LOCK TABLES `deduccion_fiscal` WRITE;
/*!40000 ALTER TABLE `deduccion_fiscal` DISABLE KEYS */;
INSERT INTO `deduccion_fiscal` VALUES (2,2,2,22.55),(3,4,1,35.03),(4,6,5,4.58),(5,7,3,20.00),(6,9,4,90.00),(7,10,5,6.54);
/*!40000 ALTER TABLE `deduccion_fiscal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_factura`
--

DROP TABLE IF EXISTS `detalle_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_factura` (
  `id_detalle` int(11) NOT NULL AUTO_INCREMENT,
  `id_factura` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `id_factura` (`id_factura`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `detalle_factura_ibfk_1` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id_factura`),
  CONSTRAINT `detalle_factura_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_factura`
--

LOCK TABLES `detalle_factura` WRITE;
/*!40000 ALTER TABLE `detalle_factura` DISABLE KEYS */;
INSERT INTO `detalle_factura` VALUES (3,2,3,2,90.00),(4,2,4,4,60.00),(5,2,5,1,80.00),(6,3,3,3,135.00),(7,4,5,1,80.00),(8,5,1,2,2400.00);
/*!40000 ALTER TABLE `detalle_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_servicio`
--

DROP TABLE IF EXISTS `detalle_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_servicio` (
  `id_detalle_servicio` int(11) NOT NULL AUTO_INCREMENT,
  `id_factura` int(11) NOT NULL,
  `id_servicio` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_detalle_servicio`),
  KEY `id_factura` (`id_factura`),
  KEY `id_servicio` (`id_servicio`),
  CONSTRAINT `detalle_servicio_ibfk_1` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id_factura`) ON DELETE CASCADE,
  CONSTRAINT `detalle_servicio_ibfk_2` FOREIGN KEY (`id_servicio`) REFERENCES `servicios_profesionales` (`id_servicio`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_servicio`
--

LOCK TABLES `detalle_servicio` WRITE;
/*!40000 ALTER TABLE `detalle_servicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_servicio` ENABLE KEYS */;
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
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES (2,2,'2024-06-02','Pagada',225.50),(3,3,'2024-06-03','Pendiente',89.99),(4,1,'2024-06-05','Pagada',350.25),(5,4,'2024-06-08','Cancelada',120.00),(6,5,'2024-06-10','Pagada',45.80),(7,3,'2024-06-12','Pagada',199.99),(8,2,'2024-06-15','Pendiente',78.30),(9,4,'2024-06-18','Pagada',899.99),(10,5,'2024-06-20','Pagada',65.40);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `importadores`
--

DROP TABLE IF EXISTS `importadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `importadores` (
  `id_importador` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_importador` varchar(100) DEFAULT NULL,
  `contacto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_importador`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `importadores`
--

LOCK TABLES `importadores` WRITE;
/*!40000 ALTER TABLE `importadores` DISABLE KEYS */;
INSERT INTO `importadores` VALUES (1,'Importaciones Globales','Roberto Mendoza'),(3,'Distribuidora Internacional','Sr. Miguel Ángel Díaz'),(4,'Comercio Exterior S.A.','Sra. Patricia Navarro');
/*!40000 ALTER TABLE `importadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `info_clientes`
--

DROP TABLE IF EXISTS `info_clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info_clientes` (
  `id_cliente` int(11) NOT NULL,
  `preferencias_envio` varchar(255) DEFAULT NULL,
  `historial_compras` text DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  CONSTRAINT `info_clientes_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info_clientes`
--

LOCK TABLES `info_clientes` WRITE;
/*!40000 ALTER TABLE `info_clientes` DISABLE KEYS */;
INSERT INTO `info_clientes` VALUES (1,'Entrega en domicilio','Compra frecuente de herramientas'),(2,'Recoge en tienda','Principalmente materiales de construcción'),(3,'Entrega express','Variedad de productos tecnológicos y suministros'),(4,'Entrega estándar','Productos de alto valor'),(5,'Recoge en tienda','Pequeñas cantidades de diversos productos');
/*!40000 ALTER TABLE `info_clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mantenimientos`
--

DROP TABLE IF EXISTS `mantenimientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mantenimientos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) NOT NULL,
  `fecha_programada` date NOT NULL,
  `direccion` text NOT NULL,
  `encargado` varchar(100) NOT NULL,
  `completado` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `fk_cliente` (`id_cliente`),
  CONSTRAINT `fk_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mantenimientos`
--

LOCK TABLES `mantenimientos` WRITE;
/*!40000 ALTER TABLE `mantenimientos` DISABLE KEYS */;
INSERT INTO `mantenimientos` VALUES (1,1,'2024-08-15','Calle Principal 123, Ciudad','Carlos López',0),(2,1,'2024-02-10','Calle Principal 123, Ciudad','María García',1),(3,2,'2024-09-20','Avenida Central 456, Ciudad','Pedro Sánchez',0),(4,2,'2024-12-05','Avenida Central 456, Ciudad','Ana Martínez',0),(5,3,'2024-07-30','Boulevard Norte 789, Ciudad','Luis Rodríguez',0),(6,3,'2024-01-15','Boulevard Norte 789, Ciudad','Juan Pérez',1),(7,4,'2024-10-05','Calle Sur 321, Ciudad','Roberto Mendoza',0),(8,4,'2024-03-22','Calle Sur 321, Ciudad','Laura Fernández',1),(9,5,'2024-11-12','Avenida Este 654, Ciudad','Sofía Ramírez',0),(10,5,'2024-04-18','Avenida Este 654, Ciudad','Jorge Mendoza',1);
/*!40000 ALTER TABLE `mantenimientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_producto` varchar(100) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `id_proveedor` int(11) DEFAULT NULL,
  `id_importador` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `id_proveedor` (`id_proveedor`),
  KEY `id_importador` (`id_importador`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores` (`id_proveedor`),
  CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`id_importador`) REFERENCES `importadores` (`id_importador`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Laptop EliteBook',1200.00,'Laptop empresarial de alto rendimiento',1,1),(3,'Teclado inalámbrico',45.00,'Teclado ergonómico inalámbrico',1,NULL),(4,'Mouse óptico',15.00,'Mouse con cable de alta precisión',3,3),(5,'Disco SSD 500GB',80.00,'Disco de estado sólido de alta velocidad',2,1);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `id_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_proveedor` varchar(100) DEFAULT NULL,
  `contacto` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES (1,'Suministros Industriales S.A.','Roberto Jiménez','555-1111','ventas@suministros.com'),(2,'Materiales de Construcción Ltda.','Laura Fernández','555-2222','contacto@materiales.com'),(3,'Equipos Tecnológicos S.A.','Pedro Sánchez','555-3333','info@equipostec.com'),(4,'Insumos Médicos Internacional','Dra. Sofía Ramírez','555-4444','ventas@insumosmed.com'),(5,'Productos Químicos Unidos','Ing. Jorge Mendoza','555-5555','pqunidos@quimicos.com');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'administrador'),(2,'usuario'),(3,'ventas'),(4,'inventario');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicios_profesionales`
--

DROP TABLE IF EXISTS `servicios_profesionales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicios_profesionales` (
  `id_servicio` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_servicio` varchar(100) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `id_proveedor` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_servicio`),
  KEY `id_proveedor` (`id_proveedor`),
  CONSTRAINT `servicios_profesionales_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores` (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios_profesionales`
--

LOCK TABLES `servicios_profesionales` WRITE;
/*!40000 ALTER TABLE `servicios_profesionales` DISABLE KEYS */;
INSERT INTO `servicios_profesionales` VALUES (1,'Instalación de software',150.00,1),(2,'Mantenimiento preventivo',200.00,2),(3,'Reparación de hardware',120.00,3),(4,'Capacitación técnica',180.00,1),(5,'Consultoría IT',250.00,2);
/*!40000 ALTER TABLE `servicios_profesionales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin1','1234','prueba@gmail.com',1),(2,'usuario1','12345','prueba1@gmail.com',2),(3,'ventas','$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi','ventas@siger.com',3),(4,'inventario','$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi','inventario@siger.com',4);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
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

-- Dump completed on 2025-07-18 21:29:11
