-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojo-survey
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojo-survey` ;

-- -----------------------------------------------------
-- Schema dojo-survey
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojo-survey` DEFAULT CHARACTER SET utf8 ;
USE `dojo-survey` ;

-- -----------------------------------------------------
-- Table `dojo-survey`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo-survey`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `location` VARCHAR(255) NULL,
  `language` VARCHAR(45) NULL,
  `comment` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
