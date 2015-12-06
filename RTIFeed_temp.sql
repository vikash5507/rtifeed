-- MySQL dump 10.13  Distrib 5.6.22, for osx10.8 (x86_64)
--
-- Host: localhost    Database: RTIFeed_temp
-- ------------------------------------------------------
-- Server version	5.6.21

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user social auth',7,'add_usersocialauth'),(20,'Can change user social auth',7,'change_usersocialauth'),(21,'Can delete user social auth',7,'delete_usersocialauth'),(22,'Can add nonce',8,'add_nonce'),(23,'Can change nonce',8,'change_nonce'),(24,'Can delete nonce',8,'delete_nonce'),(25,'Can add association',9,'add_association'),(26,'Can change association',9,'change_association'),(27,'Can delete association',9,'delete_association'),(28,'Can add code',10,'add_code'),(29,'Can change code',10,'change_code'),(30,'Can delete code',10,'delete_code'),(31,'Can add state',11,'add_state'),(32,'Can change state',11,'change_state'),(33,'Can delete state',11,'delete_state'),(34,'Can add address',12,'add_address'),(35,'Can change address',12,'change_address'),(36,'Can delete address',12,'delete_address'),(37,'Can add user_profile',13,'add_user_profile'),(38,'Can change user_profile',13,'change_user_profile'),(39,'Can delete user_profile',13,'delete_user_profile'),(40,'Can add department',14,'add_department'),(41,'Can change department',14,'change_department'),(42,'Can delete department',14,'delete_department'),(43,'Can add authority',15,'add_authority'),(44,'Can change authority',15,'change_authority'),(45,'Can delete authority',15,'delete_authority'),(46,'Can add state_department',16,'add_state_department'),(47,'Can change state_department',16,'change_state_department'),(48,'Can delete state_department',16,'delete_state_department'),(49,'Can add central_department',17,'add_central_department'),(50,'Can change central_department',17,'change_central_department'),(51,'Can delete central_department',17,'delete_central_department'),(52,'Can add rt i_query',18,'add_rti_query'),(53,'Can change rt i_query',18,'change_rti_query'),(54,'Can delete rt i_query',18,'delete_rti_query'),(55,'Can add rt i_query_file',19,'add_rti_query_file'),(56,'Can change rt i_query_file',19,'change_rti_query_file'),(57,'Can delete rt i_query_file',19,'delete_rti_query_file'),(58,'Can add rt i_response',20,'add_rti_response'),(59,'Can change rt i_response',20,'change_rti_response'),(60,'Can delete rt i_response',20,'delete_rti_response'),(61,'Can add rt i_response_file',21,'add_rti_response_file'),(62,'Can change rt i_response_file',21,'change_rti_response_file'),(63,'Can delete rt i_response_file',21,'delete_rti_response_file'),(64,'Can add tag',22,'add_tag'),(65,'Can change tag',22,'change_tag'),(66,'Can delete tag',22,'delete_tag'),(67,'Can add rt i_tag',23,'add_rti_tag'),(68,'Can change rt i_tag',23,'change_rti_tag'),(69,'Can delete rt i_tag',23,'delete_rti_tag'),(70,'Can add user_tag',24,'add_user_tag'),(71,'Can change user_tag',24,'change_user_tag'),(72,'Can delete user_tag',24,'delete_user_tag'),(73,'Can add activity',25,'add_activity'),(74,'Can change activity',25,'change_activity'),(75,'Can delete activity',25,'delete_activity'),(76,'Can add follow_user',26,'add_follow_user'),(77,'Can change follow_user',26,'change_follow_user'),(78,'Can delete follow_user',26,'delete_follow_user'),(79,'Can add follow_state',27,'add_follow_state'),(80,'Can change follow_state',27,'change_follow_state'),(81,'Can delete follow_state',27,'delete_follow_state'),(82,'Can add follow_topic',28,'add_follow_topic'),(83,'Can change follow_topic',28,'change_follow_topic'),(84,'Can delete follow_topic',28,'delete_follow_topic'),(85,'Can add follow_department',29,'add_follow_department'),(86,'Can change follow_department',29,'change_follow_department'),(87,'Can delete follow_department',29,'delete_follow_department'),(88,'Can add notification',30,'add_notification'),(89,'Can change notification',30,'change_notification'),(90,'Can delete notification',30,'delete_notification'),(91,'Can add user_feed',31,'add_user_feed'),(92,'Can change user_feed',31,'change_user_feed'),(93,'Can delete user_feed',31,'delete_user_feed'),(94,'Can add relevance',32,'add_relevance'),(95,'Can change relevance',32,'change_relevance'),(96,'Can delete relevance',32,'delete_relevance'),(97,'Can add activity_relevance',33,'add_activity_relevance'),(98,'Can change activity_relevance',33,'change_activity_relevance'),(99,'Can delete activity_relevance',33,'delete_activity_relevance'),(100,'Can add rt i_unlinked_files',34,'add_rti_unlinked_files'),(101,'Can change rt i_unlinked_files',34,'change_rti_unlinked_files'),(102,'Can delete rt i_unlinked_files',34,'delete_rti_unlinked_files');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$15000$ROWn53FWiwC1$WbyPD4VGQP8hCPzKz3oc4ByLv9w+CKVNLn4uGI+4bfg=','2015-12-05 19:14:34',0,'paarth.n','Paarth','Neekhara','paarth.n@gmail.com',0,1,'2015-11-19 14:13:37'),(2,'pbkdf2_sha256$15000$KyRvfeDvOtiH$LWcgln0zmLC6LZNHHrTlQpuFjCW6tdNkhKThosjatkA=','2015-11-19 15:20:05',0,'skp','shubham','pandey','skp@gmail.com',0,1,'2015-11-19 15:19:15'),(3,'pbkdf2_sha256$15000$q3RuEQQZ16k9$mDn0Jtpd+wG8VyQtbKVg2eiDTrq0LBSHdrNsAbcQfr8=','2015-11-25 14:12:43',0,'vikas','vikas','yadac','vikas@gmail.com',0,1,'2015-11-19 15:20:51'),(4,'pbkdf2_sha256$15000$ROWn53FWiwC1$WbyPD4VGQP8hCPzKz3oc4ByLv9w+CKVNLn4uGI+4bfg=','2015-11-28 16:53:31',0,'rahul','rahul','yadav','rahul@gmail.com',0,1,'2015-11-28 16:53:21'),(5,'pbkdf2_sha256$15000$7OYzIF3VUKpN$PxuT12CkhURdwrdtFK0EskHW6grvDOgznmOaPyNl/DM=','2015-12-05 11:32:22',0,'palash','palash','agrwawal','palash@gmail.com',0,1,'2015-12-05 11:31:35');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'user social auth','default','usersocialauth'),(8,'nonce','default','nonce'),(9,'association','default','association'),(10,'code','default','code'),(11,'state','rtiapp','state'),(12,'address','rtiapp','address'),(13,'user_profile','rtiapp','user_profile'),(14,'department','rtiapp','department'),(15,'authority','rtiapp','authority'),(16,'state_department','rtiapp','state_department'),(17,'central_department','rtiapp','central_department'),(18,'rt i_query','rtiapp','rti_query'),(19,'rt i_query_file','rtiapp','rti_query_file'),(20,'rt i_response','rtiapp','rti_response'),(21,'rt i_response_file','rtiapp','rti_response_file'),(22,'tag','rtiapp','tag'),(23,'rt i_tag','rtiapp','rti_tag'),(24,'user_tag','rtiapp','user_tag'),(25,'activity','rtiapp','activity'),(26,'follow_user','rtiapp','follow_user'),(27,'follow_state','rtiapp','follow_state'),(28,'follow_topic','rtiapp','follow_topic'),(29,'follow_department','rtiapp','follow_department'),(30,'notification','rtiapp','notification'),(31,'user_feed','rtiapp','user_feed'),(32,'relevance','rtiapp','relevance'),(33,'activity_relevance','rtiapp','activity_relevance'),(34,'rt i_unlinked_files','rtiapp','rti_unlinked_files');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-11-19 14:12:03'),(2,'auth','0001_initial','2015-11-19 14:12:04'),(3,'admin','0001_initial','2015-11-19 14:12:05'),(4,'default','0001_initial','2015-11-19 14:12:06'),(5,'default','0002_add_related_name','2015-11-19 14:12:06'),(6,'default','0003_alter_email_max_length','2015-11-19 14:12:06'),(7,'rtiapp','0001_initial','2015-11-19 14:12:17'),(8,'rtiapp','0002_auto_20151104_1356','2015-11-19 14:12:19'),(9,'rtiapp','0003_useractivity','2015-11-19 14:12:20'),(10,'rtiapp','0004_auto_20151107_2008','2015-11-19 14:12:21'),(11,'rtiapp','0005_auto_20151107_2014','2015-11-19 14:12:22'),(12,'rtiapp','0006_relevance_feed_head_line','2015-11-19 14:12:24'),(13,'rtiapp','0007_activity_user_feed','2015-11-19 14:12:25'),(14,'rtiapp','0008_auto_20151109_0017','2015-11-19 14:12:27'),(15,'rtiapp','0009_auto_20151119_1941','2015-11-19 14:12:36'),(16,'sessions','0001_initial','2015-11-19 14:12:36'),(17,'rtiapp','0010_auto_20151119_1954','2015-11-19 14:29:36'),(18,'rtiapp','0011_auto_20151120_1206','2015-11-20 06:37:00'),(19,'rtiapp','0012_notification_read_status','2015-11-25 10:44:17'),(20,'rtiapp','0013_activity_relevance','2015-11-25 11:07:22'),(21,'rtiapp','0014_rti_unlinked_files','2015-12-01 17:59:33'),(22,'rtiapp','0015_auto_20151202_2201','2015-12-02 16:31:34'),(23,'rtiapp','0016_remove_rti_query_rti_number','2015-12-02 17:04:37'),(24,'rtiapp','0017_remove_rti_response_description','2015-12-02 19:24:00');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('coh655cwml986iwdygk1ku7t685ehc91','MGUyMzVjYjMzNDcxMjliNzI3YTlhZmNiMjI5NTdmMGU1NmZjNmM0YTp7ImZhY2Vib29rX3N0YXRlIjoiTDR2MmVNWXNvVml1dU16eG92VXg2cmtJdzhoY1VBNUkiLCJlbWFpbF92YWxpZGF0aW9uX2FkZHJlc3MiOiJwYWFydGgubkBnbWFpbC5jb20iLCJuZXh0IjoiL2hvbWUifQ==','2015-12-10 08:30:02'),('fo9uz00nonpqcxy3igm7uz7pg1toc7ry','N2Y2OWE5YjM1OTExNTYwNWExZDM0YzU1ZmRjNTdlMzZkYTNhZjVlOTp7fQ==','2015-12-20 19:42:57');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_activity`
--

DROP TABLE IF EXISTS `rtiapp_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activity_type` varchar(20) NOT NULL,
  `meta_data` longtext,
  `entry_date` datetime NOT NULL,
  `rti_query_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_activity_ef94a2f6` (`rti_query_id`),
  KEY `rtiapp_activity_e8701ad4` (`user_id`),
  CONSTRAINT `rtiapp_acti_rti_query_id_732dab1e5f8846a2_fk_rtiapp_rti_query_id` FOREIGN KEY (`rti_query_id`) REFERENCES `rtiapp_rti_query` (`id`),
  CONSTRAINT `rtiapp_activity_user_id_24c35299b65fa8b8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_activity`
--

LOCK TABLES `rtiapp_activity` WRITE;
/*!40000 ALTER TABLE `rtiapp_activity` DISABLE KEYS */;
INSERT INTO `rtiapp_activity` VALUES (1,'rti_query','{\"activity_id\": 1}','2015-11-19 14:17:50',1,1),(2,'rti_query','','2015-11-19 14:17:50',1,1),(3,'rti_query','{\"activity_id\": 2}','2015-11-19 14:20:37',2,1),(4,'rti_query','','2015-11-19 14:20:37',2,1),(5,'rti_query','{\"activity_id\": 3}','2015-11-19 14:20:56',3,1),(6,'rti_query','','2015-11-19 14:20:56',3,1),(7,'rti_query','','2015-11-19 14:21:50',4,1),(8,'rti_query','','2015-11-19 14:22:07',5,1),(9,'rti_query','','2015-11-19 14:22:33',6,1),(10,'rti_query','','2015-11-19 14:23:14',7,1),(11,'rti_query','','2015-11-19 14:23:46',8,1),(12,'rti_query',NULL,'2015-11-19 14:29:54',9,1),(13,'rti_query',NULL,'2015-11-19 14:30:53',10,1),(14,'rti_query',NULL,'2015-11-19 14:38:13',11,1),(22,'comment','{\"comment_text\": \"sample\"}','2015-11-19 15:24:31',11,3),(23,'comment','{\"comment_text\": \"wtf\"}','2015-11-19 15:24:40',11,3),(24,'comment','{\"comment_text\": \"ok\"}','2015-11-19 15:28:00',11,3),(25,'comment','{\"comment_text\": \"ab theek hai\"}','2015-11-19 15:30:58',11,3),(26,'comment','{\"comment_text\": \"bas\"}','2015-11-19 15:32:04',11,3),(32,'comment','{\"comment_text\": \"fine! gr8\"}','2015-11-19 15:44:54',11,1),(33,'comment','{\"comment_text\": \"ok\"}','2015-11-19 16:04:19',11,1),(34,'comment','{\"comment_text\": \"fine -_-\"}','2015-11-19 16:05:08',11,1),(35,'comment','{\"comment_text\": \"ok\"}','2015-11-25 06:53:18',11,1),(37,'like',NULL,'2015-11-25 10:43:24',10,1),(40,'rti_query',NULL,'2015-11-25 10:45:28',12,1),(44,'like',NULL,'2015-11-25 12:35:38',1,1),(45,'like',NULL,'2015-11-25 14:11:59',11,1),(46,'like',NULL,'2015-11-25 14:36:48',7,3),(64,'spam',NULL,'2015-11-26 06:52:54',11,3),(65,'comment','{\"comment_text\": \"This is just not acceptable. we need to do something about this. what the funcj man, i mena what will haen is the lineint wxecennajk rhe alloted space\"}','2015-11-27 14:41:49',11,3),(66,'comment','{\"comment_text\": \"o\"}','2015-11-27 14:42:03',11,3),(67,'rti_query',NULL,'2015-11-27 15:35:41',13,3),(73,'like',NULL,'2015-11-27 16:53:47',11,3),(74,'like',NULL,'2015-11-28 16:12:24',8,3),(75,'follow',NULL,'2015-11-28 16:12:25',8,3),(78,'spam',NULL,'2015-11-28 17:48:10',8,1),(82,'like',NULL,'2015-11-28 17:48:54',8,1),(83,'follow',NULL,'2015-11-28 17:48:56',1,1),(84,'follow',NULL,'2015-11-28 17:48:58',10,1),(85,'like',NULL,'2015-11-28 17:49:03',3,1),(86,'spam',NULL,'2015-11-28 17:49:41',11,1),(87,'like',NULL,'2015-11-29 05:23:45',4,1),(88,'follow',NULL,'2015-11-29 05:25:38',11,1),(89,'rti_query',NULL,'2015-11-30 05:20:05',14,1),(90,'rti_query',NULL,'2015-12-02 17:07:04',18,1);
/*!40000 ALTER TABLE `rtiapp_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_activity_relevance`
--

DROP TABLE IF EXISTS `rtiapp_activity_relevance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_activity_relevance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relevance` double NOT NULL,
  `views` int(11) NOT NULL,
  `update_date` datetime NOT NULL,
  `activity_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_activity_relevance_f8a3193a` (`activity_id`),
  KEY `rtiapp_activity_relevance_e8701ad4` (`user_id`),
  CONSTRAINT `rtiapp_activi_activity_id_61abac7f150f0218_fk_rtiapp_activity_id` FOREIGN KEY (`activity_id`) REFERENCES `rtiapp_activity` (`id`),
  CONSTRAINT `rtiapp_activity_relevanc_user_id_d0af852d018ac5a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_activity_relevance`
--

LOCK TABLES `rtiapp_activity_relevance` WRITE;
/*!40000 ALTER TABLE `rtiapp_activity_relevance` DISABLE KEYS */;
INSERT INTO `rtiapp_activity_relevance` VALUES (1,0.199961957537774,9,'2015-11-25 13:13:39',1,1),(2,0.199961956545698,9,'2015-11-25 13:13:39',2,1),(3,0,27,'2015-11-25 13:13:39',3,1),(4,0,16,'2015-11-25 13:13:39',4,1),(5,0,22,'2015-11-25 13:13:39',5,1),(6,0,11,'2015-11-25 13:13:39',6,1),(7,0,24,'2015-11-25 13:13:39',7,1),(8,0,242,'2015-11-25 13:13:39',8,1),(9,0,239,'2015-11-25 13:13:39',9,1),(10,0,228,'2015-11-25 13:13:39',10,1),(11,0.199988577430515,9,'2015-11-25 13:13:39',11,1),(12,0,26,'2015-11-25 13:13:39',12,1),(13,0.200020548333824,9,'2015-11-25 13:13:39',13,1),(14,2.00053531259347,9,'2015-11-25 13:13:39',14,1),(15,2.20288926958264,9,'2015-11-25 13:13:39',22,1),(16,2.20289673673234,9,'2015-11-25 13:13:39',23,1),(17,2.20306299891325,9,'2015-11-25 13:13:39',24,1),(18,2.20321104517321,9,'2015-11-25 13:13:39',25,1),(19,2.20326594541673,9,'2015-11-25 13:13:39',26,1),(22,2.00355208699304,9,'2015-11-25 13:13:39',32,1),(23,2.00443652214376,9,'2015-11-25 13:13:39',33,1),(24,2.00447377309198,9,'2015-11-25 13:13:39',34,1),(25,4.02925194644204,31,'2015-11-25 13:13:39',35,1),(26,0.477244504311193,24,'2015-11-25 13:13:39',37,1),(28,0,243,'2015-11-25 13:13:39',40,1),(29,0.545305398747013,24,'2015-11-25 13:13:39',44,1),(30,0.199961929441007,0,'2015-11-25 13:13:39',1,2),(31,0.199961928511362,0,'2015-11-25 13:13:39',2,2),(32,0,0,'2015-11-25 13:13:39',3,2),(33,0,0,'2015-11-25 13:13:39',4,2),(34,0,0,'2015-11-25 13:13:39',5,2),(35,0,0,'2015-11-25 13:13:39',6,2),(36,0,0,'2015-11-25 13:13:39',7,2),(37,0,0,'2015-11-25 13:13:39',8,2),(38,0,0,'2015-11-25 13:13:39',9,2),(39,0,0,'2015-11-25 13:13:39',10,2),(40,0.199988550108373,0,'2015-11-25 13:13:39',11,2),(41,0,0,'2015-11-25 13:13:39',12,2),(42,0.200020521576406,0,'2015-11-25 13:13:39',13,2),(43,2.00053504434354,0,'2015-11-25 13:13:39',14,2),(44,2.00262634002964,0,'2015-11-25 13:13:39',22,2),(45,2.00263313118595,0,'2015-11-25 13:13:39',23,2),(46,2.00278428018829,0,'2015-11-25 13:13:39',24,2),(47,2.00291886944129,0,'2015-11-25 13:13:39',25,2),(48,2.00296878449559,0,'2015-11-25 13:13:39',26,2),(51,2.00355183531038,0,'2015-11-25 13:13:39',32,2),(52,2.00443627342214,0,'2015-11-25 13:13:39',33,2),(53,2.00447352594412,0,'2015-11-25 13:13:39',34,2),(54,4.02923965420345,0,'2015-11-25 13:13:39',35,2),(55,0.477241998999059,0,'2015-11-25 13:13:39',37,2),(57,0,0,'2015-11-25 13:13:39',40,2),(58,0.545301300286939,0,'2015-11-25 13:13:40',44,2),(59,0.399923812113275,87,'2015-11-25 13:13:40',1,3),(60,0.399923810763145,87,'2015-11-25 13:13:40',2,3),(61,0.199974393399937,87,'2015-11-25 13:13:40',3,3),(62,0.199974392675958,87,'2015-11-25 13:13:40',4,3),(63,0.199975813195474,87,'2015-11-25 13:13:40',5,3),(64,0.19997581223381,87,'2015-11-25 13:13:40',6,3),(65,0.199979851195452,88,'2015-11-25 13:13:40',7,3),(66,0.199981122386841,88,'2015-11-25 13:13:40',8,3),(67,0.199983066973391,88,'2015-11-25 13:13:40',9,3),(68,0.199986134161737,88,'2015-11-25 13:13:40',10,3),(69,0.399977055724019,87,'2015-11-25 13:13:40',11,3),(70,0.200016080088571,88,'2015-11-25 13:13:40',12,3),(71,0.40004099868729,87,'2015-11-25 13:13:40',13,3),(72,2.40064178808132,87,'2015-11-25 13:13:40',14,3),(73,2.20288873043465,87,'2015-11-25 13:13:40',22,3),(74,2.20289620003258,87,'2015-11-25 13:13:40',23,3),(75,2.20306246471262,87,'2015-11-25 13:13:40',24,3),(76,2.20321051311757,87,'2015-11-25 13:13:40',25,3),(77,2.20326541948013,87,'2015-11-25 13:13:40',26,3),(80,2.40426193701458,87,'2015-11-25 13:13:40',32,3),(81,2.40532326314597,87,'2015-11-25 13:13:40',33,3),(82,2.40536796573824,87,'2015-11-25 13:13:40',34,3),(83,4.83507463526826,88,'2015-11-25 13:13:40',35,3),(84,0.954479450051416,88,'2015-11-25 13:13:40',37,3),(86,0.478208661605578,88,'2015-11-25 13:13:40',40,3),(87,1.09059456177157,88,'2015-11-25 13:13:40',44,3),(88,1.75978873043945,0,'2015-11-28 16:12:24',74,1),(89,1.17319195135446,0,'2015-11-28 16:12:24',74,2),(90,1.1731915122006,0,'2015-11-28 16:12:24',74,3),(91,1.75978978665422,235,'2015-11-28 16:12:25',75,1),(92,1.17319276522443,0,'2015-11-28 16:12:25',75,2),(93,1.75978830678636,1,'2015-11-28 16:12:25',75,3),(101,1.75978996667862,0,'2015-11-28 17:48:10',78,1),(102,1.17319285882517,0,'2015-11-28 17:48:10',78,2),(103,2.34638431729004,0,'2015-11-28 17:48:10',78,3),(104,1.1731916433732,0,'2015-11-28 17:48:10',78,4),(117,1.75978966392694,0,'2015-11-28 17:48:54',82,1),(118,1.17319266568026,0,'2015-11-28 17:48:54',82,2),(119,2.3463842513213,0,'2015-11-28 17:48:54',82,3),(120,1.1731914764705,0,'2015-11-28 17:48:54',82,4),(121,1.17319308109663,220,'2015-11-28 17:48:56',83,1),(122,0.586596291096935,0,'2015-11-28 17:48:56',83,2),(123,1.17319203727367,0,'2015-11-28 17:48:56',83,3),(124,0.586595841828241,0,'2015-11-28 17:48:56',83,4),(125,1.17319317365475,220,'2015-11-28 17:48:58',84,1),(126,0.586596340017459,0,'2015-11-28 17:48:58',84,2),(127,1.17319220080524,0,'2015-11-28 17:48:58',84,3),(128,0.586595896396628,0,'2015-11-28 17:48:58',84,4),(129,0.586596651336553,220,'2015-11-28 17:49:03',85,1),(130,0.58659638843402,0,'2015-11-28 17:49:03',85,2),(131,1.17319220000583,0,'2015-11-28 17:49:03',85,3),(132,0.586595832165815,0,'2015-11-28 17:49:03',85,4),(133,7.6257544849177,0,'2015-11-28 17:49:41',86,1),(134,7.62575192184586,0,'2015-11-28 17:49:41',86,2),(135,8.21234466990096,0,'2015-11-28 17:49:41',86,3),(136,7.62574543341383,0,'2015-11-28 17:49:41',86,4),(137,0.586596434626144,216,'2015-11-29 05:23:45',87,1),(138,0.586596150383174,0,'2015-11-29 05:23:45',87,2),(139,1.17319182876669,0,'2015-11-29 05:23:45',87,3),(140,0.586595732309197,0,'2015-11-29 05:23:45',87,4),(141,8.2123518097595,213,'2015-11-29 05:25:38',88,1),(142,7.62575273516051,0,'2015-11-29 05:25:38',88,2),(143,8.21234561925314,0,'2015-11-29 05:25:38',88,3),(144,7.62574673697252,0,'2015-11-29 05:25:38',88,4);
/*!40000 ALTER TABLE `rtiapp_activity_relevance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_address`
--

DROP TABLE IF EXISTS `rtiapp_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address_line` varchar(200) DEFAULT NULL,
  `city` varchar(200) DEFAULT NULL,
  `pincode` varchar(200) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `entry_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  `state_id` int(11),
  PRIMARY KEY (`id`),
  KEY `rtiapp_address_d5582625` (`state_id`),
  CONSTRAINT `rtiapp_address_state_id_29093c0df4db9d65_fk_rtiapp_state_id` FOREIGN KEY (`state_id`) REFERENCES `rtiapp_state` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_address`
--

LOCK TABLES `rtiapp_address` WRITE;
/*!40000 ALTER TABLE `rtiapp_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `rtiapp_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_authority`
--

DROP TABLE IF EXISTS `rtiapp_authority`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_authority` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `authority_name` varchar(200) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_authority_bf691be4` (`department_id`),
  CONSTRAINT `rtiapp_au_department_id_7d5484cd45ee4324_fk_rtiapp_department_id` FOREIGN KEY (`department_id`) REFERENCES `rtiapp_department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_authority`
--

LOCK TABLES `rtiapp_authority` WRITE;
/*!40000 ALTER TABLE `rtiapp_authority` DISABLE KEYS */;
/*!40000 ALTER TABLE `rtiapp_authority` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_central_department`
--

DROP TABLE IF EXISTS `rtiapp_central_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_central_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `department_id` (`department_id`),
  CONSTRAINT `rtiapp_ce_department_id_35f51815f826f084_fk_rtiapp_department_id` FOREIGN KEY (`department_id`) REFERENCES `rtiapp_department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_central_department`
--

LOCK TABLES `rtiapp_central_department` WRITE;
/*!40000 ALTER TABLE `rtiapp_central_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `rtiapp_central_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_department`
--

DROP TABLE IF EXISTS `rtiapp_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(200) NOT NULL,
  `website` varchar(200) DEFAULT NULL,
  `department_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_department`
--

LOCK TABLES `rtiapp_department` WRITE;
/*!40000 ALTER TABLE `rtiapp_department` DISABLE KEYS */;
INSERT INTO `rtiapp_department` VALUES (1,'Department of Administrative Reforms & PG','http://darpg.gov.in/','centre'),(2,'Department of Agricultural Research & Education','http://dare.nic.in','centre'),(3,'Department of Agriculture & Cooperation','http://agricoop.nic.in','centre'),(4,'Department of AIDS Control','http://www.naco.gov.in/NACO','centre'),(5,'Department of Animal Husbandry Dairying and Fisheries','http://dahd.nic.in/animal.htm','centre'),(6,'Department of AYUSH','http://www.indianmedicine.nic.in','centre'),(7,'Department of Bio-Technology','http://dbtindia.nic.in','centre'),(8,'Department of Chemicals & Petrochemicals','http://chemicals.nic.in/','centre'),(9,'Department of Commerce','http://commerce.nic.in','centre'),(10,'Department of Consumer Affairs','http://consumeraffairs.nic.in','centre'),(11,'Department of Defence','http://www.mod.nic.in','centre'),(12,'Department of Defence Production','http://ddpmod.gov.in','centre'),(13,'Department of Defence Research & Development','http://www.drdo.gov.in/','centre'),(14,'Department of Disinvestment','http://www.divest.nic.in/','centre'),(15,'Department of Economic Affairs','http://finmin.nic.in/the_ministry/dept_eco_affairs/dea.asp','centre'),(16,'Department of Expenditure','http://finmin.nic.in/the_ministry/dept_expenditure/index.asp','centre'),(17,'Department of Ex-Servicemen Welfare','http://desw.gov.in','centre'),(18,'Department of Fertilisers','http://fert.nic.in/index.htm','centre'),(19,'Department of Financial Services','','centre'),(20,'Department of Food & Public Distribution','http://www.fcamin.nic.in/dfpd_html/index.asp','centre'),(21,'Department of Health & Family Welfare','http://www.mohfw.nic.in/','centre'),(22,'Department of Health Research','http://www.dhr.gov.in','centre'),(23,'Department of Heavy Industries','http://dhi.nic.in','centre'),(24,'Department of Higher Education','http://mhrd.gov.in/higher_education','centre'),(25,'Department of Home','http://mha.nic.in/uniquepage.asp?Id_Pk=225','centre'),(26,'Department of Industrial Policy & Promotion','http://dipp.nic.in/','centre'),(27,'Department of Information Technology','http://mit.gov.in/','centre'),(28,'Department of Justice','http://lawmin.nic.in/doj/','centre'),(29,'Department of Land Resources','http://dolr.nic.in','centre'),(30,'Department of Legal Affairs','http://lawmin.nic.in/Legal.htm','centre'),(31,'Department of Pensions & Pensioners Welfare','http://persmin.nic.in/pension/','centre'),(32,'Department of Personnel & Training','http://persmin.nic.in','centre'),(33,'Department of Pharmaceuticals','http://pharmaceuticals.gov.in','centre'),(34,'Department of Posts','http://www.indiapost.gov.in','centre'),(35,'Department of Public Enterprises','http://dpe.nic.in','centre'),(36,'Department of Revenue','http://dor.gov.in','centre'),(37,'Department of Rural Development','http://rural.nic.in/','centre'),(38,'Department of School Education and Literacy','http://mhrd.gov.in/schooleducation','centre'),(39,'Department of Science & Technology','http://www.dst.gov.in','centre'),(40,'Department of Scientific & Industrial Research','http://www.dsir.gov.in/','centre'),(41,'Department of Telecommunications','http://www.dot.gov.in/','centre'),(42,'Legislative Department','http://lawmin.nic.in/Legis.htm','centre');
/*!40000 ALTER TABLE `rtiapp_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_follow_department`
--

DROP TABLE IF EXISTS `rtiapp_follow_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_follow_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entry_date` datetime NOT NULL,
  `followee_id` int(11) NOT NULL,
  `follower_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_follow_department_641c2af7` (`followee_id`),
  KEY `rtiapp_follow_department_6bde7ca3` (`follower_id`),
  CONSTRAINT `rtiapp_foll_followee_id_69c958870446b06e_fk_rtiapp_department_id` FOREIGN KEY (`followee_id`) REFERENCES `rtiapp_department` (`id`),
  CONSTRAINT `rtiapp_follow_depar_follower_id_423f07293eabd3b5_fk_auth_user_id` FOREIGN KEY (`follower_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_follow_department`
--

LOCK TABLES `rtiapp_follow_department` WRITE;
/*!40000 ALTER TABLE `rtiapp_follow_department` DISABLE KEYS */;
INSERT INTO `rtiapp_follow_department` VALUES (1,'2015-11-26 18:50:37',3,3);
/*!40000 ALTER TABLE `rtiapp_follow_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_follow_state`
--

DROP TABLE IF EXISTS `rtiapp_follow_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_follow_state` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entry_date` datetime NOT NULL,
  `followee_id` int(11) NOT NULL,
  `follower_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_follow_state_641c2af7` (`followee_id`),
  KEY `rtiapp_follow_state_6bde7ca3` (`follower_id`),
  CONSTRAINT `rtiapp_follow_st_followee_id_6c16014ad0b0a54e_fk_rtiapp_state_id` FOREIGN KEY (`followee_id`) REFERENCES `rtiapp_state` (`id`),
  CONSTRAINT `rtiapp_follow_state_follower_id_6f38ed36ec77dcb1_fk_auth_user_id` FOREIGN KEY (`follower_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_follow_state`
--

LOCK TABLES `rtiapp_follow_state` WRITE;
/*!40000 ALTER TABLE `rtiapp_follow_state` DISABLE KEYS */;
/*!40000 ALTER TABLE `rtiapp_follow_state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_follow_topic`
--

DROP TABLE IF EXISTS `rtiapp_follow_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_follow_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entry_date` datetime NOT NULL,
  `followee_id` int(11) NOT NULL,
  `follower_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_follow_topic_641c2af7` (`followee_id`),
  KEY `rtiapp_follow_topic_6bde7ca3` (`follower_id`),
  CONSTRAINT `rtiapp_follow_topi_followee_id_578fb0a0c1184594_fk_rtiapp_tag_id` FOREIGN KEY (`followee_id`) REFERENCES `rtiapp_tag` (`id`),
  CONSTRAINT `rtiapp_follow_topic_follower_id_11a56401e098c75b_fk_auth_user_id` FOREIGN KEY (`follower_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_follow_topic`
--

LOCK TABLES `rtiapp_follow_topic` WRITE;
/*!40000 ALTER TABLE `rtiapp_follow_topic` DISABLE KEYS */;
/*!40000 ALTER TABLE `rtiapp_follow_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_follow_user`
--

DROP TABLE IF EXISTS `rtiapp_follow_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_follow_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entry_date` datetime NOT NULL,
  `followee_id` int(11) NOT NULL,
  `follower_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_follow_user_641c2af7` (`followee_id`),
  KEY `rtiapp_follow_user_6bde7ca3` (`follower_id`),
  CONSTRAINT `rtiapp_follow_user_followee_id_47d3a079313dce01_fk_auth_user_id` FOREIGN KEY (`followee_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `rtiapp_follow_user_follower_id_6c3493f30b0c44b0_fk_auth_user_id` FOREIGN KEY (`follower_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_follow_user`
--

LOCK TABLES `rtiapp_follow_user` WRITE;
/*!40000 ALTER TABLE `rtiapp_follow_user` DISABLE KEYS */;
INSERT INTO `rtiapp_follow_user` VALUES (1,'2015-11-19 15:21:34',1,3),(2,'2015-11-25 12:35:10',3,1),(3,'2015-12-06 05:12:59',4,1);
/*!40000 ALTER TABLE `rtiapp_follow_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_notification`
--

DROP TABLE IF EXISTS `rtiapp_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `notification_type` varchar(20) DEFAULT NULL,
  `entry_date` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `activity_id` int(11),
  `follow_id` int(11),
  `read_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_notification_e8701ad4` (`user_id`),
  KEY `rtiapp_notification_f8a3193a` (`activity_id`),
  KEY `rtiapp_notification_5aba7d47` (`follow_id`),
  CONSTRAINT `rtiapp_notifi_activity_id_46a175ee1cdf3634_fk_rtiapp_activity_id` FOREIGN KEY (`activity_id`) REFERENCES `rtiapp_activity` (`id`),
  CONSTRAINT `rtiapp_notifi_follow_id_1a026410aa8a732_fk_rtiapp_follow_user_id` FOREIGN KEY (`follow_id`) REFERENCES `rtiapp_follow_user` (`id`),
  CONSTRAINT `rtiapp_notification_user_id_741a6107c88eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_notification`
--

LOCK TABLES `rtiapp_notification` WRITE;
/*!40000 ALTER TABLE `rtiapp_notification` DISABLE KEYS */;
INSERT INTO `rtiapp_notification` VALUES (6,'rti_query','2015-11-25 12:35:38',1,44,NULL,1),(7,'rti_query','2015-11-25 14:11:59',1,45,NULL,1),(8,'rti_query','2015-11-25 14:36:48',1,46,NULL,1),(26,'rti_query','2015-11-26 06:52:54',1,64,NULL,1),(27,'rti_query','2015-11-27 14:41:49',1,65,NULL,1),(28,'rti_query','2015-11-27 14:42:03',1,66,NULL,1),(30,'rti_query','2015-11-27 16:53:47',1,73,NULL,1),(31,'rti_query','2015-11-28 16:12:24',1,74,NULL,1),(32,'rti_query','2015-11-28 16:12:25',1,75,NULL,1),(35,'rti_query','2015-11-28 17:48:10',1,78,NULL,1),(39,'rti_query','2015-11-28 17:48:54',1,82,NULL,1),(40,'rti_query','2015-11-28 17:48:56',1,83,NULL,1),(41,'rti_query','2015-11-28 17:48:58',1,84,NULL,1),(42,'rti_query','2015-11-28 17:49:03',1,85,NULL,1),(43,'rti_query','2015-11-28 17:49:41',1,86,NULL,1),(44,'rti_query','2015-11-29 05:23:45',1,87,NULL,1),(45,'rti_query','2015-11-29 05:25:38',1,88,NULL,1);
/*!40000 ALTER TABLE `rtiapp_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_relevance`
--

DROP TABLE IF EXISTS `rtiapp_relevance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_relevance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relevance` double NOT NULL,
  `views` int(11) NOT NULL,
  `update_date` datetime NOT NULL,
  `rti_query_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `feed_head_line` longtext,
  PRIMARY KEY (`id`),
  KEY `rtiapp_relevance_ef94a2f6` (`rti_query_id`),
  KEY `rtiapp_relevance_e8701ad4` (`user_id`),
  CONSTRAINT `rtiapp_rele_rti_query_id_5105e0717f18c57f_fk_rtiapp_rti_query_id` FOREIGN KEY (`rti_query_id`) REFERENCES `rtiapp_rti_query` (`id`),
  CONSTRAINT `rtiapp_relevance_user_id_1cc9b05394f17e6b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_relevance`
--

LOCK TABLES `rtiapp_relevance` WRITE;
/*!40000 ALTER TABLE `rtiapp_relevance` DISABLE KEYS */;
INSERT INTO `rtiapp_relevance` VALUES (4,0.000576721399003745,311,'2015-12-06 05:12:59',1,1,NULL),(5,0.000411991090205547,61,'2015-12-06 05:12:59',2,1,NULL),(6,0.00045319610831927,316,'2015-12-06 05:12:59',3,1,NULL),(7,0.000453212907120032,308,'2015-12-06 05:12:59',4,1,NULL),(8,0.000412016540167887,272,'2015-12-06 05:12:59',5,1,NULL),(9,0.000412023608437761,281,'2015-12-06 05:12:59',6,1,NULL),(10,0.000453239035363602,283,'2015-12-06 05:12:59',7,1,NULL),(11,0.000618066809286117,334,'2015-12-06 05:12:59',8,1,NULL),(12,0.00041214869592818,114,'2015-12-06 05:12:59',9,1,NULL),(13,0.000577031557547667,325,'2015-12-06 05:12:59',10,1,NULL),(14,0.00152547304802141,360,'2015-12-06 05:12:59',11,1,NULL),(15,0.00110422779012024,0,'2015-11-26 06:39:32',1,2,NULL),(16,0.021431364109062,0,'2015-11-19 16:27:13',2,2,NULL),(17,0.0214459150387742,0,'2015-11-19 16:27:13',3,2,NULL),(18,0.0214873849812862,0,'2015-11-19 16:27:13',4,2,NULL),(19,0.0215004710655563,0,'2015-11-19 16:27:13',5,2,NULL),(20,0.0215197461198483,0,'2015-11-19 16:27:13',6,2,NULL),(21,0.00122309620634568,0,'2015-11-25 14:36:48',7,2,NULL),(22,0.00125559287991982,0,'2015-11-25 10:44:34',8,2,NULL),(23,0.00114181502366366,0,'2015-11-25 10:47:53',9,2,NULL),(24,0.00125678088428571,0,'2015-11-25 10:43:24',10,2,NULL),(25,0.00283438007960448,0,'2015-11-27 16:53:47',11,2,NULL),(26,0.00110422777980776,74,'2015-11-26 06:39:32',1,3,NULL),(27,0.0214313245256054,73,'2015-11-19 16:27:13',2,3,NULL),(28,0.0214458753915836,73,'2015-11-19 16:27:13',3,3,NULL),(29,0.0214873454337848,74,'2015-11-19 16:27:13',4,3,NULL),(30,0.0215004317040865,74,'2015-11-19 16:27:13',5,3,NULL),(31,0.0215197070273773,74,'2015-11-19 16:27:13',6,3,NULL),(32,0.00122309619377732,76,'2015-11-25 14:36:48',7,3,NULL),(33,0.00125559286689447,79,'2015-11-25 10:44:34',8,3,NULL),(34,0.00114181501147802,74,'2015-11-25 10:47:53',9,3,NULL),(35,0.00125678086852902,74,'2015-11-25 10:43:24',10,3,NULL),(36,0.00283438005170703,87,'2015-11-27 16:53:47',11,3,NULL);
/*!40000 ALTER TABLE `rtiapp_relevance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_rti_query`
--

DROP TABLE IF EXISTS `rtiapp_rti_query`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_rti_query` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `query_text` longtext NOT NULL,
  `description` varchar(200) NOT NULL,
  `rti_file_date` datetime NOT NULL,
  `response_status` tinyint(1) NOT NULL,
  `query_type` varchar(50) NOT NULL,
  `entry_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  `authority_id` int(11),
  `department_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_rti_query_b43ca67e` (`authority_id`),
  KEY `rtiapp_rti_query_bf691be4` (`department_id`),
  KEY `rtiapp_rti_query_e8701ad4` (`user_id`),
  CONSTRAINT `rtiapp_rt_department_id_1c7e97dc265378e5_fk_rtiapp_department_id` FOREIGN KEY (`department_id`) REFERENCES `rtiapp_department` (`id`),
  CONSTRAINT `rtiapp_rti__authority_id_7d6786e008fd2785_fk_rtiapp_authority_id` FOREIGN KEY (`authority_id`) REFERENCES `rtiapp_authority` (`id`),
  CONSTRAINT `rtiapp_rti_query_user_id_14b02a499c4fc3a0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_rti_query`
--

LOCK TABLES `rtiapp_rti_query` WRITE;
/*!40000 ALTER TABLE `rtiapp_rti_query` DISABLE KEYS */;
INSERT INTO `rtiapp_rti_query` VALUES (1,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',0,'centre','2015-11-19 14:17:50','2015-11-19 14:17:50',NULL,3,1),(2,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',0,'centre','2015-11-19 14:20:37','2015-11-19 14:20:37',NULL,3,1),(3,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',0,'centre','2015-11-19 14:20:56','2015-11-19 14:20:56',NULL,3,1),(4,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',0,'centre','2015-11-19 14:21:50','2015-11-19 14:21:50',NULL,3,1),(5,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',0,'centre','2015-11-19 14:22:07','2015-11-19 14:22:07',NULL,3,1),(6,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',0,'centre','2015-11-19 14:22:32','2015-11-19 14:22:33',NULL,3,1),(7,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',0,'centre','2015-11-19 14:23:14','2015-11-19 14:23:14',NULL,3,1),(8,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',0,'centre','2015-11-19 14:23:46','2015-11-19 14:23:46',NULL,3,1),(9,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',0,'centre','2015-11-19 14:29:54','2015-11-19 14:29:54',NULL,3,1),(10,'<p>wvwrfwemf;lwkefl</p>','wefwef','2014-12-31 18:30:00',1,'centre','2015-11-19 14:30:53','2015-11-19 14:30:53',NULL,3,1),(11,'<p>wefwef</p>','wedewd','2014-12-31 18:30:00',0,'centre','2015-11-19 14:38:13','2015-11-19 14:38:13',NULL,2,1),(12,'<p>djhfdskj hsdkjfhdskjfh hkldfjsdlkfjlsdk</p>','this is a test','2014-12-31 18:30:00',0,'centre','2015-11-25 10:45:28','2015-11-25 10:45:28',NULL,4,1),(13,'<p>fine this is just a test</p>','ok','2014-12-31 18:30:00',0,'centre','2015-11-27 15:35:41','2015-11-27 15:35:41',NULL,2,3),(14,'<p>qdeqd</p>','wdcw','2014-12-31 18:30:00',0,'centre','2015-11-30 05:20:05','2015-11-30 05:20:05',NULL,1,1),(15,'<p>ewf</p>','wef','2014-12-31 18:30:00',0,'centre','2015-12-02 17:04:55','2015-12-02 17:04:55',NULL,1,1),(16,'<p>ewf</p>','wef','2014-12-31 18:30:00',0,'centre','2015-12-02 17:05:43','2015-12-02 17:05:43',NULL,1,1),(17,'<p>ewf</p>','wef','2014-12-31 18:30:00',0,'centre','2015-12-02 17:06:44','2015-12-02 17:06:44',NULL,1,1),(18,'<p>ewf</p>','wef','2014-12-31 18:30:00',0,'centre','2015-12-02 17:07:04','2015-12-02 17:07:04',NULL,1,1);
/*!40000 ALTER TABLE `rtiapp_rti_query` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_rti_query_file`
--

DROP TABLE IF EXISTS `rtiapp_rti_query_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_rti_query_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `query_picture` varchar(100) NOT NULL,
  `query_document` varchar(100) DEFAULT NULL,
  `rti_query_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_rti_query_file_ef94a2f6` (`rti_query_id`),
  CONSTRAINT `rtiapp_rti__rti_query_id_6643fa92e9b0e06c_fk_rtiapp_rti_query_id` FOREIGN KEY (`rti_query_id`) REFERENCES `rtiapp_rti_query` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_rti_query_file`
--

LOCK TABLES `rtiapp_rti_query_file` WRITE;
/*!40000 ALTER TABLE `rtiapp_rti_query_file` DISABLE KEYS */;
INSERT INTO `rtiapp_rti_query_file` VALUES (1,'query_pictures/Screen_Shot_2015-11-15_at_10.05.58_pm.png','',11),(2,'query_pictures/Screen_Shot_2015-11-22_at_2.23.06_am.png','',12),(3,'query_pictures/Screen_Shot_2015-11-30_at_9.20.15_pm_I1msu29.png','',18);
/*!40000 ALTER TABLE `rtiapp_rti_query_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_rti_response`
--

DROP TABLE IF EXISTS `rtiapp_rti_response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_rti_response` (
  `rti_query_id` int(11) NOT NULL,
  `response_text` longtext NOT NULL,
  `rti_response_date` datetime DEFAULT NULL,
  `entry_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  PRIMARY KEY (`rti_query_id`),
  CONSTRAINT `rtiapp_rti__rti_query_id_1173043daae1baaa_fk_rtiapp_rti_query_id` FOREIGN KEY (`rti_query_id`) REFERENCES `rtiapp_rti_query` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_rti_response`
--

LOCK TABLES `rtiapp_rti_response` WRITE;
/*!40000 ALTER TABLE `rtiapp_rti_response` DISABLE KEYS */;
INSERT INTO `rtiapp_rti_response` VALUES (10,'<p>This is a test</p>','2015-12-08 18:30:00','2015-12-03 16:44:01','2015-12-03 16:44:02'),(18,'<p>ewfewfewf</p>','2014-12-31 18:30:00','2015-12-02 19:32:40','2015-12-02 19:32:40');
/*!40000 ALTER TABLE `rtiapp_rti_response` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_rti_response_file`
--

DROP TABLE IF EXISTS `rtiapp_rti_response_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_rti_response_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `query_picture` varchar(100) NOT NULL,
  `query_document` varchar(100) DEFAULT NULL,
  `rti_response_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_rti_response_file_aa2d7465` (`rti_response_id`),
  CONSTRAINT `D6083293722e3ec645d20deb70a3baa0` FOREIGN KEY (`rti_response_id`) REFERENCES `rtiapp_rti_response` (`rti_query_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_rti_response_file`
--

LOCK TABLES `rtiapp_rti_response_file` WRITE;
/*!40000 ALTER TABLE `rtiapp_rti_response_file` DISABLE KEYS */;
INSERT INTO `rtiapp_rti_response_file` VALUES (1,'query_pictures/Screen_Shot_2015-11-30_at_9.25.33_pm_Y9qPJjx.png','',18),(2,'query_pictures/Screen_Shot_2015-11-30_at_9.20.15_pm_i5qm047.png','',18),(3,'query_pictures/Screen_Shot_2015-11-30_at_9.25.33_pm_mKxVvEP.png','',10),(4,'query_pictures/Screen_Shot_2015-11-30_at_9.20.15_pm_UiV0Mwo.png','',10);
/*!40000 ALTER TABLE `rtiapp_rti_response_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_rti_tag`
--

DROP TABLE IF EXISTS `rtiapp_rti_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_rti_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entry_date` datetime NOT NULL,
  `rti_query_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_rti_tag_ef94a2f6` (`rti_query_id`),
  KEY `rtiapp_rti_tag_76f094bc` (`tag_id`),
  CONSTRAINT `rtiapp_rti__rti_query_id_558205ecca3bf2c0_fk_rtiapp_rti_query_id` FOREIGN KEY (`rti_query_id`) REFERENCES `rtiapp_rti_query` (`id`),
  CONSTRAINT `rtiapp_rti_tag_tag_id_47d9a1881a2ee914_fk_rtiapp_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `rtiapp_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_rti_tag`
--

LOCK TABLES `rtiapp_rti_tag` WRITE;
/*!40000 ALTER TABLE `rtiapp_rti_tag` DISABLE KEYS */;
INSERT INTO `rtiapp_rti_tag` VALUES (1,'2015-12-02 17:07:04',18,5),(2,'2015-12-02 17:07:04',18,6);
/*!40000 ALTER TABLE `rtiapp_rti_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_rti_unlinked_files`
--

DROP TABLE IF EXISTS `rtiapp_rti_unlinked_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_rti_unlinked_files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rti_hash` varchar(200) NOT NULL,
  `query_picture` varchar(100) NOT NULL,
  `linked` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_rti_unlinked_files_e8701ad4` (`user_id`),
  CONSTRAINT `rtiapp_rti_unlinked_fil_user_id_36338c4fe70df2ff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_rti_unlinked_files`
--

LOCK TABLES `rtiapp_rti_unlinked_files` WRITE;
/*!40000 ALTER TABLE `rtiapp_rti_unlinked_files` DISABLE KEYS */;
INSERT INTO `rtiapp_rti_unlinked_files` VALUES (106,'1####2015-12-03 22:13:44.763090','query_pictures/Screen_Shot_2015-11-30_at_9.25.33_pm_mKxVvEP.png',1,1),(107,'1####2015-12-03 22:13:44.763090','query_pictures/Screen_Shot_2015-11-30_at_9.20.15_pm_UiV0Mwo.png',1,1);
/*!40000 ALTER TABLE `rtiapp_rti_unlinked_files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_state`
--

DROP TABLE IF EXISTS `rtiapp_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_state` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state_name` varchar(200) NOT NULL,
  `capital_name` varchar(200) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_state`
--

LOCK TABLES `rtiapp_state` WRITE;
/*!40000 ALTER TABLE `rtiapp_state` DISABLE KEYS */;
INSERT INTO `rtiapp_state` VALUES (1,'Andhra Pradesh',NULL,NULL,NULL),(2,'Arunachal Pradesh',NULL,NULL,NULL),(3,'Assam',NULL,NULL,NULL),(4,'Bihar',NULL,NULL,NULL),(5,'Chhattisgarh',NULL,NULL,NULL),(6,'Goa',NULL,NULL,NULL),(7,'Gujarat',NULL,NULL,NULL),(8,'Haryana',NULL,NULL,NULL),(9,'Himachal Pradesh',NULL,NULL,NULL),(10,'Jammu and Kashmir',NULL,NULL,NULL),(11,'Jharkhand',NULL,NULL,NULL),(12,'Karnataka',NULL,NULL,NULL),(13,'Kerala',NULL,NULL,NULL),(14,'Madhya Pradesh',NULL,NULL,NULL),(15,'Maharashtra',NULL,NULL,NULL),(16,'Manipur',NULL,NULL,NULL),(17,'Meghalaya',NULL,NULL,NULL),(18,'Mizoram',NULL,NULL,NULL),(19,'Nagaland',NULL,NULL,NULL),(20,'Orrisa',NULL,NULL,NULL),(21,'Punjab',NULL,NULL,NULL),(22,'Rajasthan',NULL,NULL,NULL),(23,'Sikkim',NULL,NULL,NULL),(24,'Tamil Nadu',NULL,NULL,NULL),(25,'Tripura',NULL,NULL,NULL),(26,'Uttar Pradesh',NULL,NULL,NULL),(27,'Uttarakhand',NULL,NULL,NULL),(28,'West Bengal',NULL,NULL,NULL);
/*!40000 ALTER TABLE `rtiapp_state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_state_department`
--

DROP TABLE IF EXISTS `rtiapp_state_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_state_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` int(11) NOT NULL,
  `state_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `department_id` (`department_id`),
  KEY `rtiapp_state_department_d5582625` (`state_id`),
  CONSTRAINT `rtiapp_st_department_id_12129a5999c371fa_fk_rtiapp_department_id` FOREIGN KEY (`department_id`) REFERENCES `rtiapp_department` (`id`),
  CONSTRAINT `rtiapp_state_depart_state_id_6285841708395cf4_fk_rtiapp_state_id` FOREIGN KEY (`state_id`) REFERENCES `rtiapp_state` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_state_department`
--

LOCK TABLES `rtiapp_state_department` WRITE;
/*!40000 ALTER TABLE `rtiapp_state_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `rtiapp_state_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_tag`
--

DROP TABLE IF EXISTS `rtiapp_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_text` varchar(200) NOT NULL,
  `entry_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_tag`
--

LOCK TABLES `rtiapp_tag` WRITE;
/*!40000 ALTER TABLE `rtiapp_tag` DISABLE KEYS */;
INSERT INTO `rtiapp_tag` VALUES (1,'sample','2015-10-10 00:00:00'),(2,'education','2015-10-10 00:00:00'),(3,'efwef','2015-12-02 17:01:40'),(4,'ewfwef','2015-12-02 17:01:40'),(5,'ef','2015-12-02 17:02:19'),(6,'efw','2015-12-02 17:02:19');
/*!40000 ALTER TABLE `rtiapp_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_user_feed`
--

DROP TABLE IF EXISTS `rtiapp_user_feed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_user_feed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relevance` double NOT NULL,
  `entry_date` datetime NOT NULL,
  `activity_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_user_feed_f8a3193a` (`activity_id`),
  KEY `rtiapp_user_feed_e8701ad4` (`user_id`),
  CONSTRAINT `rtiapp_user_f_activity_id_6f1fe66f951e634c_fk_rtiapp_activity_id` FOREIGN KEY (`activity_id`) REFERENCES `rtiapp_activity` (`id`),
  CONSTRAINT `rtiapp_user_feed_user_id_4ddcf0e995dd4a8e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_user_feed`
--

LOCK TABLES `rtiapp_user_feed` WRITE;
/*!40000 ALTER TABLE `rtiapp_user_feed` DISABLE KEYS */;
/*!40000 ALTER TABLE `rtiapp_user_feed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_user_profile`
--

DROP TABLE IF EXISTS `rtiapp_user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_user_profile` (
  `user_id` int(11) NOT NULL,
  `profile_picture` varchar(100) NOT NULL,
  `reputation` double NOT NULL,
  `gender` varchar(200) DEFAULT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `bio_description` varchar(200) DEFAULT NULL,
  `entry_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  `email_signed_up` tinyint(1) NOT NULL,
  `verification_url` varchar(500) DEFAULT NULL,
  `profile_status` varchar(200) NOT NULL,
  `address_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `rtiapp_user_profile_ea8e5d12` (`address_id`),
  CONSTRAINT `rtiapp_user_pro_address_id_5cfe669a537ac582_fk_rtiapp_address_id` FOREIGN KEY (`address_id`) REFERENCES `rtiapp_address` (`id`),
  CONSTRAINT `rtiapp_user_profile_user_id_9ba51f2881b2a70_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_user_profile`
--

LOCK TABLES `rtiapp_user_profile` WRITE;
/*!40000 ALTER TABLE `rtiapp_user_profile` DISABLE KEYS */;
INSERT INTO `rtiapp_user_profile` VALUES (1,'profile_pictures/paarthn-social_skjopGX.jpg',10,'male',NULL,NULL,'2015-11-19 14:13:37','2015-11-19 14:13:37',0,NULL,'complete',NULL),(2,'profile_pictures/default.jpg',10,NULL,NULL,NULL,'2015-11-19 15:20:04','2015-11-19 15:20:04',1,NULL,'complete',NULL),(3,'profile_pictures/default.jpg',10,NULL,NULL,NULL,'2015-11-19 15:20:51','2015-11-19 15:20:51',1,NULL,'complete',NULL),(4,'profile_pictures/default.jpg',10,NULL,NULL,NULL,'2015-11-28 16:53:21','2015-11-28 16:53:21',1,NULL,'complete',NULL),(5,'profile_pictures/default.jpg',10,NULL,NULL,NULL,'2015-12-05 11:31:35','2015-12-05 11:31:35',1,NULL,'complete',NULL);
/*!40000 ALTER TABLE `rtiapp_user_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtiapp_user_tag`
--

DROP TABLE IF EXISTS `rtiapp_user_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtiapp_user_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entry_date` datetime NOT NULL,
  `tag_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rtiapp_user_tag_76f094bc` (`tag_id`),
  KEY `rtiapp_user_tag_e8701ad4` (`user_id`),
  CONSTRAINT `rtiapp_user_tag_tag_id_746e3c33523c75dd_fk_rtiapp_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `rtiapp_tag` (`id`),
  CONSTRAINT `rtiapp_user_tag_user_id_b8c494944b5af9b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtiapp_user_tag`
--

LOCK TABLES `rtiapp_user_tag` WRITE;
/*!40000 ALTER TABLE `rtiapp_user_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `rtiapp_user_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_association`
--

DROP TABLE IF EXISTS `social_auth_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_association` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `handle` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int(11) NOT NULL,
  `lifetime` int(11) NOT NULL,
  `assoc_type` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_association`
--

LOCK TABLES `social_auth_association` WRITE;
/*!40000 ALTER TABLE `social_auth_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_code`
--

DROP TABLE IF EXISTS `social_auth_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) DEFAULT NULL,
  `code` varchar(32) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_code_email_75f27066d057e3b6_uniq` (`email`,`code`),
  KEY `social_auth_code_c1336794` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_code`
--

LOCK TABLES `social_auth_code` WRITE;
/*!40000 ALTER TABLE `social_auth_code` DISABLE KEYS */;
INSERT INTO `social_auth_code` VALUES (1,'paarth.n@gmail.com','8dc1827b5f244c049d74aa1e554fb8a1',0),(2,'vikas@gmail.com','cacc7228445f4d3b902cb7b543f8807e',1),(3,'rahul@gmail.com','ef89ceade7a04319ab2747dec4a8a087',1),(4,'palash@gmail.com','4de8f2eebe6f4d12940f119282b6779d',1);
/*!40000 ALTER TABLE `social_auth_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_nonce`
--

DROP TABLE IF EXISTS `social_auth_nonce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_nonce` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `salt` varchar(65) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_nonce_server_url_36601f978463b4_uniq` (`server_url`,`timestamp`,`salt`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_nonce`
--

LOCK TABLES `social_auth_nonce` WRITE;
/*!40000 ALTER TABLE `social_auth_nonce` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_nonce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_usersocialauth`
--

DROP TABLE IF EXISTS `social_auth_usersocialauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_usersocialauth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_usersocialauth_provider_2f763109e2c4a1fb_uniq` (`provider`,`uid`),
  KEY `social_auth_usersocialauth_e8701ad4` (`user_id`),
  CONSTRAINT `social_auth_usersociala_user_id_193b2d80880502b2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_usersocialauth`
--

LOCK TABLES `social_auth_usersocialauth` WRITE;
/*!40000 ALTER TABLE `social_auth_usersocialauth` DISABLE KEYS */;
INSERT INTO `social_auth_usersocialauth` VALUES (1,'email','paarth.n@gmail.com','{\"email\": \"paarth.n@gmail.com\"}',1),(2,'facebook','432477263629988','{\"access_token\": \"CAAXlLfvZCIcsBAJrVGqzvVPcMLNo9xNCXkCFZC8Pd0Ucf4b8pLZBe6lz5w9fBV0QR7sk54SrFBh7EHK1Otha3c4kWDVTfI7rqKEapXyYE6X54EwWLGZCZBLzCAutNT0JZCFUUBX8EkmtScfaYdKrOA44gXdH9ZAAKNZAlCcrRWh8TiZBZC08fZA1H6ohEQimZAF2yBUZD\", \"expires\": null, \"id\": \"432477263629988\"}',1),(3,'email','skp@gmail.com','{\"email\": \"skp@gmail.com\"}',2),(4,'email','vikas@gmail.com','{\"email\": \"vikas@gmail.com\"}',3),(5,'email','rahul@gmail.com','{\"email\": \"rahul@gmail.com\"}',4),(6,'email','palash@gmail.com','{\"email\": \"palash@gmail.com\"}',5);
/*!40000 ALTER TABLE `social_auth_usersocialauth` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-12-07  1:14:32
