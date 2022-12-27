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
-- Table structure for table `feeds_comment`
--

DROP TABLE IF EXISTS `feeds_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feeds_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` varchar(255) NOT NULL,
  `feed_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `created_at` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `feeds_comment_feed_id_0e00600a_fk_feeds_feed_id` (`feed_id`),
  KEY `feeds_comment_user_id_ee021013_fk_users_user_id` (`user_id`),
  CONSTRAINT `feeds_comment_feed_id_0e00600a_fk_feeds_feed_id` FOREIGN KEY (`feed_id`) REFERENCES `feeds_feed` (`id`),
  CONSTRAINT `feeds_comment_user_id_ee021013_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feeds_comment`
--

LOCK TABLES `feeds_comment` WRITE;
/*!40000 ALTER TABLE `feeds_comment` DISABLE KEYS */;
INSERT INTO `feeds_comment` VALUES (3,'1번 댓',1,62,'2021-09-29'),(4,'2번 comment',1,62,'2021-09-29'),(5,'3번 comment',1,62,'2021-09-29'),(7,'5번 comment',1,1,'2021-09-29'),(8,'asdf',1,1,'2021-09-29'),(9,'dfdfasdf',1,1,'2021-09-29'),(10,'asdfadsf',1,1,'2021-09-29'),(12,'asdf',1,1,'2021-09-29'),(13,'슈퍼 티모는 어디있음?',6,1,'2021-09-30'),(14,'dddd',1,5,'2021-10-01'),(15,'ㅁㄴㅇㄹ',13,16,'2021-10-05'),(16,'ㄴㅇㄹ',13,16,'2021-10-05'),(19,'n,',21,1,'2021-10-07'),(21,'댓글이 안달려요',24,31,'2021-10-07'),(22,'오 다시 달리네?',24,31,'2021-10-07'),(23,'닉네임은 싸피좋아인데 닉네임이 안뜨고 아이디가 뜨네요',24,31,'2021-10-07');
/*!40000 ALTER TABLE `feeds_comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-08  1:34:26
