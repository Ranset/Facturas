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

-- Dumping structure for table facturas.Clientes
CREATE TABLE IF NOT EXISTS Clientes (id INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT NOT NULL UNIQUE, Nombre TEXT NOT NULL, NIT TEXT, REEUP TEXT, ONIE TEXT, Domicilio TEXT, nro_cta_CUP TEXT, nro_cta_MLC TEXT, Telefono TEXT, email TEXT);

-- Dumping data for table facturas.Clientes: 6 rows
DELETE FROM "Clientes";
/*!40000 ALTER TABLE "Clientes" DISABLE KEYS */;
INSERT INTO "Clientes" ("id", "Nombre", "NIT", "REEUP", "ONIE", "Domicilio", "nro_cta_CUP", "nro_cta_MLC", "Telefono", "email") VALUES
	(1, 'Empresa de Suministros Integrales y Cooperación Económica', '23456789012', 'REEUP-00123', 'ONIE-44501', 'Calle Obispo #360, Habana Vieja. La Habana, Cuba. C.P. 10100.', '1234567890123456', '1234567890123457', '+5372345678', 'suministros@esice.cu'),
	(2, 'Importadora Comercial del Caribe S.A.', '34567890123', 'REEUP-00456', 'ONIE-44502', 'Ave. Rancho Boyeros #1250, Cerro. La Habana, Cuba. C.P. 10600.', '2345678901234567', '2345678901234568', '+5378901234', 'contacto@iccsa.cu'),
	(3, 'Distribuciones López y Asociados', '45678901234', NULL, NULL, 'Calle 23 #856 e/ 4 y 6, Vedado. La Habana, Cuba. C.P. 10400.', '3456789012345678', NULL, '+5354876543', 'lopez.distribuciones@gmail.com'),
	(4, 'Beta Soluciones Tecnológicas S.A.', '56789012345', 'REEUP-00789', NULL, 'Parque Tecnológico, Local 14, Boyeros. La Habana, Cuba. C.P. 10800.', '4567890123456789', '4567890123456790', '+5372109876', 'info@betasoluciones.cu'),
	(5, 'Pedro Álvarez García', '67890123456', NULL, NULL, 'Calle Martí #45, Guanabacoa. La Habana, Cuba. C.P. 11500.', '5678901234567890', NULL, '+5353112233', 'pedroalvarez@nauta.cu'),
	(6, 'ACME Representaciones Cubanas', '78901234567', 'REEUP-01010', 'ONIE-44503', 'Ave. 1ra #5680, Miramar. La Habana, Cuba. C.P. 11300.', '6789012345678901', '6789012345678902', '+5372334455', 'ventas@acmecuba.cu');
/*!40000 ALTER TABLE "Clientes" ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
