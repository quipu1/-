-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: j5c205.p.ssafy.io    Database: beer
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `beers_beer_types`
--

DROP TABLE IF EXISTS `beers_beer_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beers_beer_types` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `beer_id` bigint NOT NULL,
  `type_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `beers_beer_types_beer_id_type_id_7f8ff995_uniq` (`beer_id`,`type_id`),
  KEY `beers_beer_types_type_id_9498c126_fk_beers_type_id` (`type_id`),
  CONSTRAINT `beers_beer_types_beer_id_89fe640e_fk_beers_beer_id` FOREIGN KEY (`beer_id`) REFERENCES `beers_beer` (`id`),
  CONSTRAINT `beers_beer_types_type_id_9498c126_fk_beers_type_id` FOREIGN KEY (`type_id`) REFERENCES `beers_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beers_beer_types`
--

LOCK TABLES `beers_beer_types` WRITE;
/*!40000 ALTER TABLE `beers_beer_types` DISABLE KEYS */;
INSERT INTO `beers_beer_types` VALUES (1,1,6),(2,2,3),(3,3,2),(4,4,3),(5,5,10),(6,6,3),(7,7,6),(8,8,1),(9,9,7),(10,10,1),(11,11,11),(12,12,7),(13,13,1),(14,14,6),(15,15,4),(16,16,4),(17,17,7),(18,18,7),(19,19,5),(20,20,5),(21,21,3),(22,22,5),(23,23,5),(24,24,8),(25,25,7),(26,26,6),(27,27,10),(28,28,10),(29,29,5),(30,30,3),(31,31,3),(32,32,3),(33,33,5),(34,34,5),(35,35,7),(36,36,10),(37,37,5),(38,38,10),(39,39,5),(40,40,5),(41,41,10),(42,42,5),(43,43,5),(44,44,5),(45,45,5),(46,46,5),(47,47,5),(48,48,1),(49,49,5),(50,50,5),(51,51,5),(52,52,5),(53,53,5),(54,54,10),(55,55,8),(56,56,7),(57,57,5),(58,58,7),(59,59,9),(60,60,3),(61,61,1),(62,62,5),(63,63,7),(64,64,5),(65,65,10),(66,66,6),(67,67,6),(68,68,5),(69,69,10),(70,70,7),(71,71,10),(72,72,10),(73,73,6),(74,74,1),(75,75,6),(76,76,1),(77,77,5),(78,78,5),(79,79,8),(80,80,5),(81,81,5),(82,82,7),(83,83,8),(84,84,1),(85,85,1),(86,86,5),(87,87,5),(88,88,10),(89,89,5),(90,90,5),(91,91,6),(92,92,5),(93,93,5),(94,94,5),(95,95,5),(96,96,6),(97,97,5),(98,98,5),(99,99,5),(100,100,6),(101,101,5),(102,102,5),(103,103,5),(104,104,5),(105,105,6),(106,106,8),(107,107,5),(108,108,5),(109,109,5),(110,110,9),(111,111,7),(112,112,5),(113,113,5),(114,114,9),(115,115,6),(116,116,10),(117,117,5),(118,118,3);
/*!40000 ALTER TABLE `beers_beer_types` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-08  1:34:27
