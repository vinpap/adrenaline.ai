-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: vincent-adrenaline-ai.mysql.database.azure.com    Database: adrenaline.ai
-- ------------------------------------------------------
-- Server version	8.0.36-cluster

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

--
-- Table structure for table `calories_burnt`
--

DROP TABLE IF EXISTS `calories_burnt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calories_burnt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `watch_id` int NOT NULL,
  `record_date` date NOT NULL,
  `calories_burnt` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `calories_burnt_watches_FK` (`watch_id`),
  CONSTRAINT `calories_burnt_watches_FK` FOREIGN KEY (`watch_id`) REFERENCES `watches` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calories_burnt`
--

LOCK TABLES `calories_burnt` WRITE;
/*!40000 ALTER TABLE `calories_burnt` DISABLE KEYS */;
INSERT INTO `calories_burnt` VALUES (1,1,'2024-03-20',578),(2,1,'2024-03-26',985),(3,1,'2024-03-25',1002),(4,1,'2024-03-24',971),(5,1,'2024-03-23',425),(6,1,'2024-03-22',499),(7,1,'2024-03-28',324),(8,1,'2024-03-21',324),(9,1,'2024-03-20',657),(10,1,'2024-03-19',333),(11,1,'2024-03-18',900),(12,1,'2024-03-17',1002),(13,1,'2024-03-16',549),(14,1,'2024-03-15',538),(15,1,'2024-03-14',435),(16,1,'2024-03-13',324);
/*!40000 ALTER TABLE `calories_burnt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distance`
--

DROP TABLE IF EXISTS `distance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distance` (
  `id` int NOT NULL AUTO_INCREMENT,
  `watch_id` int NOT NULL,
  `record_date` date NOT NULL,
  `distance` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `distance_watches_FK` (`watch_id`),
  CONSTRAINT `distance_watches_FK` FOREIGN KEY (`watch_id`) REFERENCES `watches` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distance`
--

LOCK TABLES `distance` WRITE;
/*!40000 ALTER TABLE `distance` DISABLE KEYS */;
INSERT INTO `distance` VALUES (1,1,'2024-03-28',2.5),(2,1,'2024-03-27',4.7),(3,1,'2024-03-26',0.2),(4,1,'2024-03-25',0.3),(5,1,'2024-03-24',10.4),(6,1,'2024-03-23',5.9),(7,1,'2024-03-22',3.1),(8,1,'2024-03-21',0.3),(9,1,'2024-03-20',0.3),(10,1,'2024-03-19',6.2),(11,1,'2024-03-18',9.2),(12,1,'2024-03-17',4.7),(13,1,'2024-03-16',2.1),(14,1,'2024-03-15',0.2),(15,1,'2024-03-14',0.3),(16,1,'2024-03-13',0.5);
/*!40000 ALTER TABLE `distance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rest_bpm`
--

DROP TABLE IF EXISTS `rest_bpm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rest_bpm` (
  `id` int NOT NULL AUTO_INCREMENT,
  `watch_id` int NOT NULL,
  `record_date` date NOT NULL,
  `average_rest_bpm` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rest_bpm_watches_FK` (`watch_id`),
  CONSTRAINT `rest_bpm_watches_FK` FOREIGN KEY (`watch_id`) REFERENCES `watches` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rest_bpm`
--

LOCK TABLES `rest_bpm` WRITE;
/*!40000 ALTER TABLE `rest_bpm` DISABLE KEYS */;
/*!40000 ALTER TABLE `rest_bpm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sleep_time`
--

DROP TABLE IF EXISTS `sleep_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sleep_time` (
  `id` int NOT NULL AUTO_INCREMENT,
  `watch_id` int NOT NULL,
  `record_date` date NOT NULL,
  `sleep_time` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sleep_time_watches_FK` (`watch_id`),
  CONSTRAINT `sleep_time_watches_FK` FOREIGN KEY (`watch_id`) REFERENCES `watches` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sleep_time`
--

LOCK TABLES `sleep_time` WRITE;
/*!40000 ALTER TABLE `sleep_time` DISABLE KEYS */;
/*!40000 ALTER TABLE `sleep_time` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `signup_date` date NOT NULL,
  `password_hash` varbinary(100) NOT NULL,
  `salt` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (3,'TEST','TEST','TEST','2024-03-28',_binary 'f36ca7fd84a541cb15baa80ef84875b371f83ffee7c276f1c0d9a968130b8eba','331025b2b093d9db4cfa900cf88338d8d65d56783d752cd2296b0b55dd1051fc');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `watches`
--

DROP TABLE IF EXISTS `watches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `watches` (
  `id` int NOT NULL AUTO_INCREMENT,
  `model` varchar(100) NOT NULL,
  `serial_no` varchar(100) NOT NULL,
  `user_id` int DEFAULT NULL,
  `registration_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `watches_users_FK` (`user_id`),
  CONSTRAINT `watches_users_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `watches`
--

LOCK TABLES `watches` WRITE;
/*!40000 ALTER TABLE `watches` DISABLE KEYS */;
INSERT INTO `watches` VALUES (1,'Garmin','2312323',2,'2024-03-02');
/*!40000 ALTER TABLE `watches` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-27 16:21:59
