SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `raspberry` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `raspberry`.`badger` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(45) NULL DEFAULT NULL,
  `lastname` VARCHAR(45) NULL DEFAULT NULL,
  `qr_id` VARCHAR(45) NOT NULL,
  `body_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`, `body_id`),
  INDEX `fk_badger_body1_idx` (`body_id` ASC),
  UNIQUE INDEX `qr_id_UNIQUE` (`qr_id` ASC),
  CONSTRAINT `fk_badger_body1`
    FOREIGN KEY (`body_id`)
    REFERENCES `raspberry`.`body` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `raspberry`.`room` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `raspberry`.`body` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `raspberry`.`admin` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(45) NULL DEFAULT NULL,
  `admincol` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `raspberry`.`presence` (
  `badger_id` INT(11) NOT NULL,
  `room_id` INT(11) NOT NULL,
  `morning_date` DATETIME NOT NULL,
  `afternoon_date` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`badger_id`, `room_id`, `morning_date`),
  INDEX `fk_badger_has_room_room1_idx` (`room_id` ASC),
  INDEX `fk_badger_has_room_badger1_idx` (`badger_id` ASC),
  CONSTRAINT `fk_badger_has_room_badger1`
    FOREIGN KEY (`badger_id`)
    REFERENCES `raspberry`.`badger` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_badger_has_room_room1`
    FOREIGN KEY (`room_id`)
    REFERENCES `raspberry`.`room` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
