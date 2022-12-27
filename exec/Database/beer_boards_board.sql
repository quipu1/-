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
-- Table structure for table `boards_board`
--

DROP TABLE IF EXISTS `boards_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boards_board` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `score` int NOT NULL,
  `beer_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `nickname` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `boards_board_beer_id_b7a4e03a_fk_beers_beer_id` (`beer_id`),
  KEY `boards_board_user_id_f4eecbbe_fk_users_user_id` (`user_id`),
  CONSTRAINT `boards_board_beer_id_b7a4e03a_fk_beers_beer_id` FOREIGN KEY (`beer_id`) REFERENCES `beers_beer` (`id`),
  CONSTRAINT `boards_board_user_id_f4eecbbe_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boards_board`
--

LOCK TABLES `boards_board` WRITE;
/*!40000 ALTER TABLE `boards_board` DISABLE KEYS */;
INSERT INTO `boards_board` VALUES (32,'1234','2021-10-01 05:13:47.382831',3,1,12,'qwer'),(35,'이수현테스트.','2021-10-04 10:20:14.892146',5,1,5,'테스트아이디'),(36,'1234','2021-10-04 10:40:34.992950',5,7,12,'qwer'),(39,'ddd','2021-10-05 03:45:20.023870',1,8,5,'테스트아이디'),(40,'ssss','2021-10-05 03:45:24.356975',4,8,5,'테스트아이디'),(41,'ㅁㄴㅇㄹ','2021-10-05 10:53:07.116702',3,3,12,'qwer'),(42,'123','2021-10-05 13:06:21.933325',1,116,1,'123'),(43,'asdf','2021-10-05 13:48:28.950954',1,13,17,'aaa'),(44,'sdaf','2021-10-05 19:30:52.565395',2,70,17,'aaa'),(46,'asdfasdf','2021-10-06 01:45:16.190278',5,77,12,'qwer'),(47,'qwerqwer','2021-10-06 01:45:39.090586',1,70,12,'qwer'),(49,'ㅇㅇㅇ','2021-10-06 02:23:07.745118',4,48,12,'qwer'),(50,'qwer','2021-10-06 02:23:58.078746',5,116,12,'qwer'),(51,'','2021-10-06 07:40:19.928780',5,82,27,'q'),(52,'','2021-10-06 07:40:19.954821',5,75,27,'q'),(53,'','2021-10-06 07:40:20.013779',5,78,27,'q'),(62,'살려줘','2021-10-06 14:48:16.386815',4,83,12,'qwer'),(63,'제주도','2021-10-06 20:50:37.079014',4,76,3,'b'),(64,'','2021-10-07 02:52:22.064326',5,1,28,'예시'),(65,'','2021-10-07 02:52:22.108212',5,75,28,'예시'),(66,'','2021-10-07 02:59:52.402945',5,1,29,'show'),(67,'','2021-10-07 02:59:52.492068',5,78,29,'show'),(68,'맛있어요','2021-10-07 03:00:35.555911',5,82,29,'show'),(69,'하이네켄 좋아요','2021-10-07 03:01:05.164953',5,110,29,'show'),(70,'버드와이저','2021-10-07 03:02:27.571312',5,24,29,'show'),(71,'애플','2021-10-07 03:03:17.720411',5,38,29,'show'),(72,'맛없어요','2021-10-07 03:03:46.741731',1,105,29,'show'),(73,'맛없어요','2021-10-07 03:04:45.313845',1,104,29,'show'),(74,'ipa 좋아요','2021-10-07 03:06:10.415238',5,6,29,'show'),(76,'맛있어요','2021-10-07 03:06:51.976973',5,51,29,'show'),(77,'.','2021-10-07 03:07:14.539238',4,79,29,'show'),(78,'벡스','2021-10-07 03:07:28.550141',3,57,29,'show'),(79,'드라우ㅡㅌ','2021-10-07 03:07:45.640226',3,15,29,'show'),(80,'','2021-10-07 05:21:18.073155',5,82,30,'성루비 화이팅'),(81,'','2021-10-07 05:21:18.078224',5,6,30,'성루비 화이팅'),(82,'','2021-10-07 05:28:24.290756',5,15,31,'싸피좋아'),(83,'','2021-10-07 05:28:24.306800',5,114,31,'싸피좋아'),(84,'너무 좋아요 또 시킬께요','2021-10-07 05:28:46.772321',5,32,31,'싸피좋아'),(85,'','2021-10-07 09:43:01.837267',5,82,32,'테스트아이디333'),(86,'','2021-10-07 09:43:01.884148',5,1,32,'테스트아이디333'),(87,'이거 괜찮은듯','2021-10-07 09:43:21.536789',5,8,32,'테스트아이디333'),(104,'ㅁㄴㅇㄹ','2021-10-07 12:55:50.674278',1,60,1,'123'),(107,'ㅁㄴㅇ','2021-10-07 13:07:33.975043',1,1,1,'123'),(108,'','2021-10-07 15:03:15.533629',5,3,33,'테스트dv'),(110,'개별루.','2021-10-07 15:26:54.837608',1,1,33,'테스트dv'),(111,'','2021-10-07 15:27:52.678567',5,78,34,'qwer1234');
/*!40000 ALTER TABLE `boards_board` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-08  1:34:25
