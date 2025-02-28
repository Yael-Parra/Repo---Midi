import mysql.connector
from mysql.connector import errorcode

import os
from dotenv import load_dotenv
load_dotenv()
# ------------------------------------------------------------------------------
def creacion_bbdd_tablas():
    try:
        # Conectar a MySQL Server
        cnx = mysql.connector.connect(
            user= os.getenv('mysql_username'),       
            password= os.getenv('mysql_password'),  
            host= os.getenv('mysql_host'),
            port= os.getenv('mysql_port'),   
        )
# ------------------------------------------------------------------------------
        if cnx.is_connected():
            print("¡Conectado!")

            mycursor = cnx.cursor()

            # Crear la base de datos si no existe
            mycursor.execute("CREATE DATABASE IF NOT EXISTS bbdd_midi")
            print("Base de datos 'bbdd_midi' creada correctamente.")

            # Usar la base de datos
            try:
                mycursor.execute("USE bbdd_midi")
                print("Base de datos seleccionada correctamente.")
            except mysql.connector.Error as err:
                print("Error al seleccionar la base de datos.")
                print("Código de Error:", err.errno)
                print("SQLSTATE:", err.sqlstate)
                print("Mensaje:", err.msg)
# ------------------------------------------------------------------------------
            # Crear la tabla de 'alumnos'

            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS alumnos (
                             
                    id_alumno INT PRIMARY KEY AUTO_INCREMENT,
                             
                    alumno_nombre VARCHAR(50) NOT NULL, 
                    alumno_apellidos VARCHAR(50) NOT NULL,
                    alumno_fecha_nacimiento DATETIME             
                );
            """)
            print("Tabla 'alumnos' creada.")
# ------------------------------------------------------------------------------
            # Crear tabla 'info_padres_tutores_legales' (relacionada con FK a alumnos)
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS info_padres_tutores_legales (
                             
                    id_tutor INT PRIMARY KEY AUTO_INCREMENT,
                    
                    id_alumno INT,
                             
                    mama_nombre VARCHAR(50),              
                    mama_apellido VARCHAR(50),                
                    mama_cedula VARCHAR(20),
                    mama_telefono VARCHAR(20),
                    mama_email VARCHAR(50),
                    mama_empresa VARCHAR(100),
                             
                    papa_nombre VARCHAR(50),
                    papa_apellido VARCHAR(50),
                    papa_cedula VARCHAR(20),
                    papa_telefono VARCHAR(20),
                    papa_email VARCHAR(50),
                    papa_empresa VARCHAR(100),
                
                    direccion VARCHAR(100),
                             
                    FOREIGN KEY (id_alumno) REFERENCES alumnos (id_alumno)  -- Relacionado con alumnos
                );
            """)
            print("Tabla 'info_padres_tutores_legales' creada.")
# ------------------------------------------------------------------------------
            # Crear tabla 'terapeutas'
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS terapeutas (
                             
                    id_terapeuta INT PRIMARY KEY AUTO_INCREMENT,
                             
                    terapeuta_nombre VARCHAR(50),            
                    terapeuta_apellidos VARCHAR(50),                   
                    terapeuta_cedula VARCHAR(20),
                    terapeuta_telefono VARCHAR(20),
                    terapeuta_email VARCHAR(50)
                             
                );
            """)
            print("Tabla 'terapeutas' creada.")
# ------------------------------------------------------------------------------
            # Crear tabla 'colegios' (relacionada con FK a alumnos)
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS colegios (
                             
                    id_colegio INT PRIMARY KEY AUTO_INCREMENT,
                             
                    id_alumno INT,
                    id_curso INT,
                    colegio VARCHAR(100),             
                               
                    FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno)  -- Relacionado con alumnos
                    
                );
            """)
            print("Tabla 'colegios' creada.")
# ------------------------------------------------------------------------------
            # Crear tabla 'cursos' (relacionada con FK a id_colegio)
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS cursos (
                             
                    id_curso INT PRIMARY KEY AUTO_INCREMENT,
                             
                    id_colegio INT,
                             
                    nombre_curso VARCHAR(100),  
                             
                    FOREIGN KEY (id_colegio) REFERENCES colegios(id_colegio)  -- Relacionado con colegios
                );
            """)
            print("Tabla 'cursos' creada.")
# ------------------------------------------------------------------------------
# Crear tabla 'inscripciones' (relacionada con FK a  alumnos, cursos y tutores)
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS inscripciones (
                             
                    id_inscripcion INT PRIMARY KEY AUTO_INCREMENT,
                             
                    id_alumno INT,
                    id_curso INT,
                    id_colegio INT,
                    fecha_inscripcion DATETIME,
                    fecha_baja DATETIME,
                    
                    -- Definición de claves foráneas
                    FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno),
                    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
                    FOREIGN KEY (id_colegio) REFERENCES colegios(id_colegio)
                );
            """)
            print("Tabla 'inscripciones' creada.")
# ------------------------------------------------------------------------------
            # Crear tabla 'sesiones' (relacionada con FK a  alumnos, terapeutas y cursos)
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS sesiones (
                             
                    id_sesion INT PRIMARY KEY AUTO_INCREMENT,
                             
                    id_alumno INT,
                    id_curso INT,
                    id_terapeuta INT,
                    
                             
                    fecha_sesion DATETIME,
                             
                    FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno),
                    FOREIGN KEY (id_terapeuta) REFERENCES terapeutas(id_terapeuta),
                    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
                );
            """)
            print("Tabla 'sesiones' creada.")
# ------------------------------------------------------------------------------
            # Confirmar los cambios
            cnx.commit()
# ------------------------------------------------------------------------------
    except mysql.connector.Error as err:
        print("Se produjo un error al crear la tabla.")
        print("Código de Error:", err.errno)
        print("SQLSTATE:", err.sqlstate)
        print("Mensaje:", err.msg)
# ------------------------------------------------------------------------------
    finally:
        if cnx.is_connected():
            mycursor.close()
            cnx.close()
            print("Conexión MySQL cerrada.")
# ------------------------------------------------------------------------------
# Ejecutar la función para crear la base de datos y tablas
creacion_bbdd_tablas()
