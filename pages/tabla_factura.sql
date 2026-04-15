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

-- Dumping structure for table facturas.Facturas
CREATE TABLE IF NOT EXISTS Facturas (id INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT UNIQUE NOT NULL, numero_factura TEXT NOT NULL UNIQUE, tipo INTEGER REFERENCES Tipos (id), Vendedor INTEGER REFERENCES Vendedores (id), Cliente INTEGER REFERENCES Clientes (id), Fecha TEXT, Moneda TEXT REFERENCES Tasas (Divisa), tasa_cambio NUMERIC, metodo_pago INTEGER REFERENCES Metodos_pagos (id), porciento_cta_fiscal INTEGER, Estado INTEGER REFERENCES Estados (id), "total" REAL NULL);

-- Dumping data for table facturas.Facturas: 14 rows
DELETE FROM "Facturas";
/*!40000 ALTER TABLE "Facturas" DISABLE KEYS */;
INSERT INTO "Facturas" ("id", "numero_factura", "tipo", "Vendedor", "Cliente", "Fecha", "Moneda", "tasa_cambio", "metodo_pago", "porciento_cta_fiscal", "Estado", "total") VALUES
	(1, '260001', 1, 1, 1, '10/01/2025', 'CUP', 460, 1, 25, 3, 10.0),
	(2, '260002', 1, 1, 3, '15/01/2025', '2', 460, 2, 25, 2, 10.0),
	(3, '260003', 1, 2, 4, '20/01/2025', 'USD', 1, 1, 25, 3, 10.0),
	(4, '260004', 1, 1, 6, '25/01/2025', 'MLC', 1.29, 3, 25, 1, 10.0),
	(5, '260005', 1, 2, 2, '28/01/2025', 'CUP', 460, 1, 25, 5, 10.0),
	(6, '260006', 2, 1, 1, '05/02/2025', 'CUP', 460, 1, 25, 4, 10.0),
	(7, '260007', 2, 2, 2, '10/02/2025', 'USD', 1, 1, 25, 4, 10.0),
	(8, '260008', 2, 1, 5, '14/02/2025', 'CUP', 460, 2, 25, 3, 10.0),
	(9, '260009', 2, 2, 3, '18/02/2025', 'USD', 1, 1, 25, 2, 10.0),
	(10, '260010', 2, 1, 4, '22/02/2025', 'MLC', 1.29, 3, 25, 5, 10.0),
	(11, '260011', 2, 1, 6, '01/03/2025', 'CUP', 460, 1, 25, 1, 10.0),
	(12, '260012', 2, 2, 1, '05/03/2025', 'USD', 1, 4, 25, 3, 10.0),
	(13, '260013', 2, 1, 2, '12/03/2025', 'CUP', 460, 1, 25, 4, 10.0),
	(14, '260014', 2, 2, 5, '20/03/2025', 'USD', 1, 2, 25, 2, 10.0);
/*!40000 ALTER TABLE "Facturas" ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
