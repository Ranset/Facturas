-- --------------------------------------------------------
-- Host:                         C:\_Almacen\Develop\Facturas\Facturas\facturas.db
-- Server version:               3.44.0
-- Server OS:                    
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table facturas.Detalles_facturas
CREATE TABLE IF NOT EXISTS Detalles_facturas (id INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT UNIQUE NOT NULL, factura_id INTEGER REFERENCES Facturas (id), Producto_id INTEGER REFERENCES Productos (id), Cantidad INTEGER, Precio_venta NUMERIC);

-- Dumping data for table facturas.Detalles_facturas: 33 rows
DELETE FROM "Detalles_facturas";
/*!40000 ALTER TABLE "Detalles_facturas" DISABLE KEYS */;
INSERT INTO "Detalles_facturas" ("id", "factura_id", "Producto_id", "Cantidad", "Precio_venta") VALUES
	(1, 1, 1, 2, 48415),
	(2, 1, 9, 10, 7187.5),
	(3, 1, 4, 3, 26306.25),
	(4, 2, 6, 4, 22331.25),
	(5, 2, 10, 1, 31625),
	(6, 3, 2, 1, 975),
	(7, 3, 3, 2, 462.5),
	(8, 3, 5, 3, 82.5),
	(9, 4, 7, 1, 118.75),
	(10, 4, 14, 2, 220),
	(11, 5, 1, 5, 120675),
	(12, 5, 8, 3, 117300),
	(13, 6, 2, 3, 1097250),
	(14, 6, 11, 2, 167250),
	(15, 6, 13, 1, 120750),
	(16, 7, 3, 4, 925),
	(17, 7, 4, 4, 227.5),
	(18, 7, 5, 4, 110),
	(19, 8, 9, 20, 71875),
	(20, 8, 4, 5, 43843.75),
	(21, 9, 6, 3, 145.31),
	(22, 9, 15, 2, 105),
	(23, 10, 12, 4, 310),
	(24, 10, 7, 2, 237.5),
	(25, 11, 13, 2, 483000),
	(26, 11, 15, 4, 96600),
	(27, 12, 2, 2, 1950),
	(28, 12, 14, 3, 330),
	(29, 12, 8, 5, 425),
	(30, 13, 1, 10, 241075),
	(31, 13, 11, 3, 250875),
	(32, 14, 5, 10, 275),
	(33, 14, 9, 20, 312.5);
/*!40000 ALTER TABLE "Detalles_facturas" ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
