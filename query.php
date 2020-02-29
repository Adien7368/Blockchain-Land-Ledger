<?php
//create table
CREATE TABLE `ledger`.`records` ( `land_id` INT(100) NOT NULL , `owner` VARCHAR(200) NOT NULL , `address` VARCHAR(200) NOT NULL , `documents` VARCHAR(200) NOT NULL , `dig_sign` VARCHAR(200) NOT NULL , `availability` INT(100) NOT NULL DEFAULT '0' , PRIMARY KEY (`land_id`)) ENGINE = InnoDB;

//add inspec
$sql = "ALTER TABLE `records`  ADD `inspector` VARCHAR(111) NOT NULL  AFTER `availability`";
?>