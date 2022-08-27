
-- Schema esquema_correo
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_correo` ;

-- -----------------------------------------------------
-- Schema esquema_correo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_correo` DEFAULT CHARACTER SET utf8 ;
USE `esquema_correo` ;

-- -----------------------------------------------------
-- Table `esquema_correo`.`correos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_correo`.`correos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `correo` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
