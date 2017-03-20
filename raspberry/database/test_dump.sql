-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (armv7l)
--
-- Host: raspi.com    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu0.16.04.1-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Position to start replication or point-in-time recovery from
--
STOP SLAVE;

CHANGE MASTER TO MASTER_HOST='raspi.com',MASTER_PORT=3306, MASTER_USER='rasp_user', MASTER_PASSWORD='rasp_user',master_log_file='log-bin.000002', MASTER_LOG_POS=12157;

START SLAVE;
--
-- Current Database: `mydb`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `mydb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `mydb`;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `admincol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `badger`
--

DROP TABLE IF EXISTS `badger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `badger` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `qr_id` varchar(45) NOT NULL,
  `body_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`body_id`),
  UNIQUE KEY `qr_id_UNIQUE` (`qr_id`),
  KEY `fk_badger_body1_idx` (`body_id`),
  CONSTRAINT `fk_badger_body1` FOREIGN KEY (`body_id`) REFERENCES `body` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `badger`
--

LOCK TABLES `badger` WRITE;
/*!40000 ALTER TABLE `badger` DISABLE KEYS */;
INSERT INTO `badger` VALUES (1,'Maxime','PIC','1',1),(2,'Jimmy','LEROY','2',1);
/*!40000 ALTER TABLE `badger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `body`
--

DROP TABLE IF EXISTS `body`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `body` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `body`
--

LOCK TABLES `body` WRITE;
/*!40000 ALTER TABLE `body` DISABLE KEYS */;
INSERT INTO `body` VALUES (1,'RIL15');
/*!40000 ALTER TABLE `body` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presence`
--

DROP TABLE IF EXISTS `presence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presence` (
  `badger_id` int(11) NOT NULL,
  `room_id` int(11) NOT NULL,
  `morning_date` timestamp NULL DEFAULT NULL,
  `afternoon_date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`badger_id`,`room_id`),
  KEY `fk_badger_has_room_room1_idx` (`room_id`),
  KEY `fk_badger_has_room_badger1_idx` (`badger_id`),
  CONSTRAINT `fk_badger_has_room_badger1` FOREIGN KEY (`badger_id`) REFERENCES `badger` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_badger_has_room_room1` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presence`
--

LOCK TABLES `presence` WRITE;
/*!40000 ALTER TABLE `presence` DISABLE KEYS */;
/*!40000 ALTER TABLE `presence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `room` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-16  0:14:42
