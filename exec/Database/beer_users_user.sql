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
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) DEFAULT NULL,
  `first_name` varchar(150) DEFAULT NULL,
  `last_name` varchar(150) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `userID` varchar(20) DEFAULT NULL,
  `nickname` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `profilePhotoPath` varchar(505) DEFAULT NULL,
  `gender` tinyint(1) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `logitude` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nickname` (`nickname`),
  UNIQUE KEY `userID` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,NULL,0,'','','','',0,1,'2021-09-29 14:08:09.247877','a','123','1','3acc67ee978c11eb93d00242ac110004.gif',0,NULL,37.6356482,126.9262758),(3,NULL,0,'','','','',0,1,'2021-09-30 01:49:24.654765','b','b','1','',0,NULL,37.6356258,126.9262993),(4,NULL,0,'','','','',0,1,'2021-09-30 05:58:05.811407','c','c','1',NULL,0,NULL,12,126.94328),(5,NULL,0,'','','','',0,1,'2021-10-01 00:53:56.581246','testid','테스트아이디','votmdnjem','',0,NULL,35.1535295,126.7954147),(6,NULL,0,'','','','',0,1,'2021-10-01 01:00:48.256609','testid45','테스트아이디45','votmdnjem',NULL,0,NULL,37.56446,126.95329),(7,NULL,0,'','','','',0,1,'2021-10-01 02:21:26.648051','testid24','테스트아이디24','votmdnjem',NULL,0,NULL,NULL,NULL),(8,NULL,0,'','','','',0,1,'2021-10-01 05:27:13.886791','olivedrab13','대호13','eogh1313','',0,NULL,37.6242176,126.9202944),(9,NULL,0,'','','','',0,1,'2021-10-02 11:05:31.906083','bambamq','밤갈시니어','votmdnjem',NULL,0,NULL,NULL,NULL),(10,NULL,0,'','','','',0,1,'2021-10-02 11:23:18.597400','asdfas','asdfas','asdfasdf',NULL,0,NULL,NULL,NULL),(11,NULL,0,'','','','',0,1,'2021-10-04 07:38:36.273550','a@a.com','aa','123',NULL,0,NULL,NULL,NULL),(12,NULL,0,'','','','',0,1,'2021-10-04 09:25:47.596568','qwer','qwer','qwerqwer','',0,NULL,35.1417401,126.9433485),(13,NULL,0,'','','','',0,1,'2021-10-04 09:27:22.195392','asdf','asdf','asdfasdf','',0,NULL,35.1804,126.9012),(14,NULL,0,'','','','',0,1,'2021-10-04 16:25:24.808246','qqq','qqq','q',NULL,0,NULL,NULL,NULL),(15,NULL,0,'','','','',0,1,'2021-10-05 02:27:46.191835','f','f','1',NULL,0,NULL,37.63037897930876,126.92946758780627),(16,NULL,0,'','','','',0,1,'2021-10-05 02:29:07.135416','g','g','1',NULL,0,NULL,37.63116940960347,126.92550175851177),(17,NULL,0,'','','','',0,1,'2021-10-05 13:21:31.997989','aa','aaa','1','profiles/2021/10/05/beemo.jpeg',0,NULL,NULL,NULL),(20,NULL,0,'','','','',0,1,'2021-10-06 03:09:21.744562','dd','dd','1','',0,NULL,37.634392755960825,126.92212241053306),(21,NULL,0,'','','','',0,1,'2021-10-06 03:10:41.226946','bb','bb','1','',0,20,NULL,NULL),(22,NULL,0,'','','','',0,1,'2021-10-06 03:11:41.357927','ff','ff','1','',0,30,37.63169365266138,126.92819751006849),(23,NULL,0,'','','','',0,1,'2021-10-06 03:12:54.504294','nn','nn','1','',0,30,NULL,NULL),(24,NULL,0,'','','','',0,1,'2021-10-06 03:15:34.708130','hh','hh','1','',0,20,37.635189030952034,126.92746906411506),(25,NULL,0,'','','','',0,1,'2021-10-06 05:33:02.378265','fa','fa','1','',0,20,37.636178468929955,126.92483964283373),(26,NULL,0,'','','','',0,1,'2021-10-06 07:22:37.225138','e','e','1','',0,20,37.632663178119465,126.92260003487858),(27,NULL,0,'','','','',0,1,'2021-10-06 07:24:52.499982','q','q','1','',1,60,37.6356312,126.9262804),(28,NULL,0,'','','','',0,1,'2021-10-07 02:49:32.245471','example','예시','votmdnjem','',1,20,NULL,NULL),(29,NULL,0,'','','','',0,1,'2021-10-07 02:51:59.326808','show','show','1','',0,20,NULL,NULL),(30,NULL,0,'','','','',0,1,'2021-10-07 05:20:45.429396','gh9047','성루비 화이팅','1234','',0,NULL,NULL,NULL),(31,NULL,0,'','','','',0,1,'2021-10-07 05:27:57.546520','ssafyssafy','싸피좋아','@azsx369258','',0,NULL,NULL,NULL),(32,NULL,0,'','','','',0,1,'2021-10-07 09:42:35.450321','testid333','테스트아이디333','votmdnjem','',1,20,NULL,NULL),(33,NULL,0,'','','','',0,1,'2021-10-07 14:57:20.488293','testidv','테스트dv','votmdnjem','',1,20,35.1535295,126.7954147),(34,NULL,0,'','','','',0,1,'2021-10-07 15:27:05.094121','qwer1234','qwer1234','1234','',1,NULL,37.7242467,127.0507572);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
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
