USE `expense_tracker`;

--
-- Table structure for table `categories`
--
CREATE TABLE IF NOT EXISTS `categories` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Store expense categories.';

--
-- Table structure for table `expense`
--
CREATE TABLE IF NOT EXISTS `expenses` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `expense_date` date NOT NULL,
  `category_id` int UNSIGNED NOT NULL,
  `description` varchar(250) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id_fk_constraint` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Store expense data.';

--
-- Constraints for table `expenses`
--
ALTER TABLE `expenses`
  ADD CONSTRAINT `category_id_fk_constraint` FOREIGN KEY (`category_id`)
   REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;