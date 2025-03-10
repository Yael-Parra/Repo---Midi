import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------------------------------------------
def creacion_bbdd():
    try:
        # Conectar a MySQL Server
        cnx = mysql.connector.connect(
            user=os.getenv('mysql_username'),       
            password=os.getenv('mysql_password'),  
            host=os.getenv('mysql_host'),
            port=os.getenv('mysql_port'),   
        )
        
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
                print("⚠️ Error al seleccionar la base de datos.")
                print("Código de Error:", err.errno)
                print("SQLSTATE:", err.sqlstate)
                print("Mensaje:", err.msg)

    except mysql.connector.Error as err:
        print("⚠️ Se produjo un error al crear la base de datos.")
        print("Código de Error:", err.errno)
        print("SQLSTATE:", err.sqlstate)
        print("Mensaje:", err.msg)

    finally:
        if cnx.is_connected():
            mycursor.close()
            cnx.close()
            print("Conexión MySQL cerrada.")

# ------------------------------------------------------------------------------
# Ejecutar la función para crear la base de datos
creacion_bbdd()