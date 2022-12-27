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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-09-27 13:06:02.825812'),(2,'contenttypes','0002_remove_content_type_name','2021-09-27 13:06:03.040768'),(3,'auth','0001_initial','2021-09-27 13:06:03.784366'),(4,'auth','0002_alter_permission_name_max_length','2021-09-27 13:06:03.908401'),(5,'auth','0003_alter_user_email_max_length','2021-09-27 13:06:03.935748'),(6,'auth','0004_alter_user_username_opts','2021-09-27 13:06:03.962423'),(7,'auth','0005_alter_user_last_login_null','2021-09-27 13:06:03.989479'),(8,'auth','0006_require_contenttypes_0002','2021-09-27 13:06:04.014169'),(9,'auth','0007_alter_validators_add_error_messages','2021-09-27 13:06:04.042017'),(10,'auth','0008_alter_user_username_max_length','2021-09-27 13:06:04.069513'),(11,'auth','0009_alter_user_last_name_max_length','2021-09-27 13:06:04.100183'),(12,'auth','0010_alter_group_name_max_length','2021-09-27 13:06:04.146535'),(13,'auth','0011_update_proxy_permissions','2021-09-27 13:06:04.198338'),(14,'auth','0012_alter_user_first_name_max_length','2021-09-27 13:06:04.224902'),(15,'users','0001_initial','2021-09-27 13:06:05.149290'),(16,'admin','0001_initial','2021-09-27 13:06:05.568847'),(17,'admin','0002_logentry_remove_auto_add','2021-09-27 13:06:05.612814'),(18,'admin','0003_logentry_add_action_flag_choices','2021-09-27 13:06:05.657338'),(19,'beers','0001_initial','2021-09-27 13:06:06.380230'),(20,'boards','0001_initial','2021-09-27 13:06:06.685127'),(21,'boards','0002_board_user','2021-09-27 13:06:06.868526'),(22,'feeds','0001_initial','2021-09-27 13:06:07.100626'),(23,'feeds','0002_initial','2021-09-27 13:06:07.545336'),(24,'sessions','0001_initial','2021-09-27 13:06:07.721349'),(25,'users','0002_user_types','2021-09-28 01:30:29.669082'),(26,'boards','0003_remove_board_title','2021-09-28 08:24:46.380038'),(27,'feeds','0003_comment_created_at','2021-09-28 16:29:02.064636'),(28,'beers','0002_alter_beer_beer_type','2021-09-29 07:41:04.368597'),(29,'friends','0001_initial','2021-09-30 01:24:39.240314'),(30,'beers','0002_like','2021-09-30 02:22:52.715507'),(31,'beers','0003_beer_like_users','2021-09-30 02:32:24.954594'),(32,'beers','0004_alter_beer_like_users','2021-09-30 02:41:38.684378'),(33,'users','0002_auto_20211001_0236','2021-09-30 17:37:02.793951'),(34,'boards','0004_auto_20211001_1413','2021-10-01 05:13:34.440639'),(35,'users','0003_alter_user_add_friends','2021-10-01 05:13:34.496641'),(36,'users','0003_auto_20211003_0521','2021-10-02 20:21:14.921186'),(37,'users','0004_merge_20211005_1226','2021-10-05 03:26:22.735662'),(38,'feeds','0002_alter_feed_feedphotopath','2021-10-05 03:35:12.156267'),(39,'users','0005_alter_user_profilephotopath','2021-10-05 03:35:12.202229'),(40,'chat','0001_initial','2021-10-06 06:42:41.504551'),(41,'boards','0005_alter_board_beer','2021-10-07 01:51:41.397305'),(42,'chat','0002_delete_message','2021-10-07 04:39:22.404275');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
