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
-- Table structure for table `feeds_feed`
--

DROP TABLE IF EXISTS `feeds_feed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feeds_feed` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedPhotoPath` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `feeds_feed_user_id_f07992c0_fk_users_user_id` (`user_id`),
  CONSTRAINT `feeds_feed_user_id_f07992c0_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feeds_feed`
--

LOCK TABLES `feeds_feed` WRITE;
/*!40000 ALTER TABLE `feeds_feed` DISABLE KEYS */;
INSERT INTO `feeds_feed` VALUES (1,'1','1번 내용',NULL,1),(2,'2','2번 내용',NULL,1),(3,'3','3번 내용',NULL,1),(6,NULL,'오메가 티모','2021-09-30',1),(7,'null','dsfsdfdf','2021-10-01',5),(8,'','바람의나라','2021-10-05',5),(9,'','ddd','2021-10-05',5),(10,'산타2.JPG','dd','2021-10-05',5),(11,'','복실티모','2021-10-05',16),(12,'','복실티모','2021-10-05',16),(13,'','슈퍼 티모','2021-10-05',16),(15,'feeds/2021/10/05/바생역전.JPG','dfff','2021-10-05',5),(20,'feeds/2021/10/06/예거_피치.jfif','테스트용 게시글','2021-10-06',8),(21,'feeds/2021/10/07/1070845.png','로고?','2021-10-07',8),(22,'feeds/2021/10/07/예거_피치.jfif','테스트용','2021-10-07',8),(23,'feeds/2021/10/07/부천.jfif','구경 잘 하고 갑니당','2021-10-07',30),(24,'feeds/2021/10/07/aaaaaaaaaa.jfif','달다 달아','2021-10-07',31);
/*!40000 ALTER TABLE `feeds_feed` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-08  1:34:30
