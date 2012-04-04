SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';


-- -----------------------------------------------------
-- Table `SAES2GO`.`Usuarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`Usuarios` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`Usuarios` (
  `usuIdUsuario` VARCHAR(45) NOT NULL ,
  `usuNombre` VARCHAR(45) NOT NULL ,
  `usuCorreo` VARCHAR(45) NOT NULL ,
  `usuPassword` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`usuIdUsuario`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`Mensajes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`Mensajes` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`Mensajes` (
  `menIdMensaje` INT NOT NULL ,
  `menTexto` VARCHAR(255) NOT NULL ,
  `usuIdUsuarioOrigen` VARCHAR(45) NOT NULL ,
  `usuIdUsuarioDestino` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`menIdMensaje`) ,
  INDEX `fk_Mensajes_Usuarios1` (`usuIdUsuarioOrigen` ASC) ,
  INDEX `fk_Mensajes_Usuarios2` (`usuIdUsuarioDestino` ASC) ,
  CONSTRAINT `fk_Mensajes_Usuarios1`
    FOREIGN KEY (`usuIdUsuarioOrigen` )
    REFERENCES `SAES2GO`.`Usuarios` (`usuIdUsuario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Mensajes_Usuarios2`
    FOREIGN KEY (`usuIdUsuarioDestino` )
    REFERENCES `SAES2GO`.`Usuarios` (`usuIdUsuario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`Profesores`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`Profesores` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`Profesores` (
  `profCedulaProfesor` INT NOT NULL ,
  `usuIdUsuario` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`profCedulaProfesor`) ,
  INDEX `fk_Profesores_Usuarios1` (`usuIdUsuario` ASC) ,
  CONSTRAINT `fk_Profesores_Usuarios1`
    FOREIGN KEY (`usuIdUsuario` )
    REFERENCES `SAES2GO`.`Usuarios` (`usuIdUsuario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`Alumnos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`Alumnos` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`Alumnos` (
  `aluBoletaAlumno` INT NOT NULL ,
  `usuIdUsuario` VARCHAR(45) NOT NULL ,
  `aluMateriasReprobadas` INT NOT NULL ,
  `aluMateriasDesfasadas` INT NOT NULL ,
  `aluCreditosAdquiridos` FLOAT NOT NULL ,
  PRIMARY KEY (`aluBoletaAlumno`) ,
  INDEX `fk_Alumnos_Usuarios1` (`usuIdUsuario` ASC) ,
  CONSTRAINT `fk_Alumnos_Usuarios1`
    FOREIGN KEY (`usuIdUsuario` )
    REFERENCES `SAES2GO`.`Usuarios` (`usuIdUsuario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`Materias`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`Materias` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`Materias` (
  `matIdMateria` INT NOT NULL ,
  `matNombreMateria` VARCHAR(45) NOT NULL ,
  `matNumCreditos` FLOAT NOT NULL ,
  `matNomArea` VARCHAR(45) NOT NULL ,
  `matNumNivel` INT NOT NULL ,
  PRIMARY KEY (`matIdMateria`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`Grupos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`Grupos` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`Grupos` (
  `gruIdGrupo` VARCHAR(6) NOT NULL ,
  `gruNumGrupo` INT NOT NULL ,
  `gruTurno` CHAR(1) NOT NULL ,
  PRIMARY KEY (`gruIdGrupo`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`TiposHorario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`TiposHorario` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`TiposHorario` (
  `tihIdTipoHorario` INT NOT NULL ,
  `tihHoraIniLunes` TIME NULL ,
  `tihHoraIniMartes` TIME NULL ,
  `tihHoraIniMiercoles` TIME NULL ,
  `tihHoraIniJueves` TIME NULL ,
  `tihHoraIniViernes` TIME NULL ,
  PRIMARY KEY (`tihIdTipoHorario`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`MateriasGrupo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`MateriasGrupo` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`MateriasGrupo` (
  `matgIdMateriaGrupo` VARCHAR(45) NOT NULL ,
  `matIdMateria` INT NOT NULL ,
  `gruIdGrupo` VARCHAR(6) NOT NULL ,
  `profCedulaProfesor` INT NOT NULL ,
  `matgAnio` INT NOT NULL ,
  `matgTipoSemestre` CHAR(1) NOT NULL ,
  `magtLugaresDisp` INT NOT NULL ,
  `matgSalon` INT NOT NULL ,
  `tihIdTipoHorario` INT NOT NULL ,
  INDEX `fk_MateriasGrupo_Materias1` (`matIdMateria` ASC) ,
  INDEX `fk_MateriasGrupo_Grupos1` (`gruIdGrupo` ASC) ,
  INDEX `fk_MateriasGrupo_Profesores1` (`profCedulaProfesor` ASC) ,
  INDEX `fk_MateriasGrupo_TiposHorario1` (`tihIdTipoHorario` ASC) ,
  PRIMARY KEY (`matgIdMateriaGrupo`) ,
  CONSTRAINT `fk_MateriasGrupo_Materias1`
    FOREIGN KEY (`matIdMateria` )
    REFERENCES `SAES2GO`.`Materias` (`matIdMateria` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MateriasGrupo_Grupos1`
    FOREIGN KEY (`gruIdGrupo` )
    REFERENCES `SAES2GO`.`Grupos` (`gruIdGrupo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MateriasGrupo_Profesores1`
    FOREIGN KEY (`profCedulaProfesor` )
    REFERENCES `SAES2GO`.`Profesores` (`profCedulaProfesor` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MateriasGrupo_TiposHorario1`
    FOREIGN KEY (`tihIdTipoHorario` )
    REFERENCES `SAES2GO`.`TiposHorario` (`tihIdTipoHorario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`HorariosALumno`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`HorariosALumno` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`HorariosALumno` (
  `aluBoletaAlumno` INT NOT NULL ,
  `matIdMateria` INT NOT NULL ,
  `gruIdGrupo` VARCHAR(6) NOT NULL ,
  `matgAnio` INT NOT NULL ,
  `matgTipoSemestre` CHAR(1) NOT NULL ,
  `halDificultad` INT NULL ,
  `halCalificacion` FLOAT NULL ,
  PRIMARY KEY (`aluBoletaAlumno`, `matIdMateria`, `gruIdGrupo`, `matgAnio`, `matgTipoSemestre`) ,
  INDEX `fk_HorariosALumno_Alumnos1` (`aluBoletaAlumno` ASC) ,
  INDEX `fk_HorariosALumno_MateriasGrupo1` (`matIdMateria` ASC, `gruIdGrupo` ASC, `matgAnio` ASC, `matgTipoSemestre` ASC) ,
  CONSTRAINT `fk_HorariosALumno_Alumnos1`
    FOREIGN KEY (`aluBoletaAlumno` )
    REFERENCES `SAES2GO`.`Alumnos` (`aluBoletaAlumno` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_HorariosALumno_MateriasGrupo1`
    FOREIGN KEY (`matIdMateria` , `gruIdGrupo` , `matgAnio` , `matgTipoSemestre` )
    REFERENCES `SAES2GO`.`MateriasGrupo` (`matIdMateria` , `gruIdGrupo` , `matgAnio` , `matgTipoSemestre` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`Temarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`Temarios` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`Temarios` (
  `matIdMateria` INT NOT NULL ,
  `temIdTema` VARCHAR(5) NOT NULL ,
  `temTemaPadre` VARCHAR(5) NULL ,
  `temIdNombre` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`matIdMateria`, `temIdTema`) ,
  INDEX `fk_Temarios_Materias1` (`matIdMateria` ASC) ,
  CONSTRAINT `fk_Temarios_Materias1`
    FOREIGN KEY (`matIdMateria` )
    REFERENCES `SAES2GO`.`Materias` (`matIdMateria` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`ElementosMultimedia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`ElementosMultimedia` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`ElementosMultimedia` (
  `mulIdElemento` INT NOT NULL ,
  `temIdTema` VARCHAR(5) NOT NULL ,
  `matgIdMateriaGrupo` VARCHAR(45) NOT NULL ,
  `mulFechaClase` DATE NOT NULL ,
  `mulTipoMultimedia` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`mulIdElemento`, `temIdTema`, `matgIdMateriaGrupo`) ,
  INDEX `fk_ElementosMultimedia_Temarios` (`temIdTema` ASC) ,
  INDEX `fk_ElementosMultimedia_MateriasGrupo1` (`matgIdMateriaGrupo` ASC) ,
  CONSTRAINT `fk_ElementosMultimedia_Temarios`
    FOREIGN KEY (`temIdTema` )
    REFERENCES `SAES2GO`.`Temarios` (`temIdTema` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ElementosMultimedia_MateriasGrupo1`
    FOREIGN KEY (`matgIdMateriaGrupo` )
    REFERENCES `SAES2GO`.`MateriasGrupo` (`matgIdMateriaGrupo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`Actividades`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`Actividades` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`Actividades` (
  `actIdActividad` INT NOT NULL ,
  `matgIdMateriaGrupo` VARCHAR(45) NOT NULL ,
  `actNombre` VARCHAR(45) NOT NULL ,
  `actNumMiembros` INT NOT NULL ,
  `actFchaInicio` DATE NOT NULL ,
  `actFechaLimite` DATE NULL ,
  `actEspecificaciones` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`actIdActividad`, `matgIdMateriaGrupo`) ,
  INDEX `fk_Actividades_MateriasGrupo1` (`matgIdMateriaGrupo` ASC) ,
  CONSTRAINT `fk_Actividades_MateriasGrupo1`
    FOREIGN KEY (`matgIdMateriaGrupo` )
    REFERENCES `SAES2GO`.`MateriasGrupo` (`matgIdMateriaGrupo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAES2GO`.`ActividadesAlumno`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SAES2GO`.`ActividadesAlumno` ;

CREATE  TABLE IF NOT EXISTS `SAES2GO`.`ActividadesAlumno` (
  `aluBoletaAlumno` INT NOT NULL ,
  `actIdActividad` INT NOT NULL ,
  `matgIdMateriaGrupo` VARCHAR(45) NOT NULL ,
  `acalNumEquipo` INT NULL ,
  `acalCalificacion` FLOAT NULL ,
  `acalFechaEntrega` DATE NULL ,
  PRIMARY KEY (`aluBoletaAlumno`, `actIdActividad`, `matgIdMateriaGrupo`) ,
  INDEX `fk_ActividadesAlumno_Alumnos1` (`aluBoletaAlumno` ASC) ,
  INDEX `fk_ActividadesAlumno_Actividades1` (`actIdActividad` ASC, `matgIdMateriaGrupo` ASC) ,
  CONSTRAINT `fk_ActividadesAlumno_Alumnos1`
    FOREIGN KEY (`aluBoletaAlumno` )
    REFERENCES `SAES2GO`.`Alumnos` (`aluBoletaAlumno` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ActividadesAlumno_Actividades1`
    FOREIGN KEY (`actIdActividad` , `matgIdMateriaGrupo` )
    REFERENCES `SAES2GO`.`Actividades` (`actIdActividad` , `matgIdMateriaGrupo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
