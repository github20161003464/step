#创建一个项目
CREATE SCHEMA `student` DEFAULT CHARACTER SET utf8 ;

#创建department表格
CREATE TABLE `department` (
  `dept-name` varchar(45) NOT NULL,
  `building` varchar(45) DEFAULT NULL,
  `budget` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`dept-name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#创建student表格
CREATE TABLE `student`.`student` (
  `ID` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NULL,
  `sex` CHAR(1) NULL,
  `emotion_state` VARCHAR(45) NULL,
  `dept_name` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_student_1_idx` (`dept_name` ASC),
  CONSTRAINT `fk_student_1`
    FOREIGN KEY (`dept_name`)
    REFERENCES `student`.`department` (`dept-name`)
    ON DELETE CASCADE
    ON UPDATE SET NULL);

#创建exam表格
CREATE TABLE `student`.`exam` (
  `student_ID` INT UNSIGNED NOT NULL,
  `exam_name` VARCHAR(45) NOT NULL,
  `grade` INT UNSIGNED NULL,
  PRIMARY KEY (`student_ID`, `exam_name`),
  CONSTRAINT `fk_exam_1`
    FOREIGN KEY (`student_ID`)
    REFERENCES `student`.`student` (`ID`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);
    
#后来发现少了年龄age这个参数加上去的
ALTER TABLE `student`.`student` 
ADD COLUMN `age` INT(3) NULL AFTER `sex`;