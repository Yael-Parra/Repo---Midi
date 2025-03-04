import pandas as pd
import numpy as np
import mysql.connector
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# ------------------------------------------------------------------------------
def cargar_datos_excel(ruta_excel):
    """Carga un archivo de Excel y devuelve un diccionario de DataFrames por hoja."""
    return pd.read_excel(ruta_excel, sheet_name=None)

def convertir_a_tuplas(df):
    """Convierte un DataFrame a una lista de tuplas, reemplazando NaN por None."""
    return [
        tuple(None if isinstance(value, float) and np.isnan(value) else value for value in row)
        for row in df.itertuples(index=False, name=None)
    ]

def conectar_base_datos():
    """Conecta a la base de datos MySQL y devuelve la conexión."""
    return mysql.connector.connect(
        user=os.getenv('mysql_username'),
        password=os.getenv('mysql_password'),
        host=os.getenv('mysql_host'),
        port=os.getenv('mysql_port'),
        database=os.getenv('bbdd_name'),  # el nombre de la base de datos está en .env
    )

def insertar_datos(cnx, sql, valores):
    """Inserta múltiples registros en la base de datos."""
    try:
        cursor = cnx.cursor()  # Crear un cursor a partir de la conexión
        cursor.executemany(sql, valores)
        cnx.commit()  # Usar la conexión para hacer commit
        print(cursor.rowcount, "registro/s insertado/s.")
    except mysql.connector.Error as insert_err:
        print("⚠️ Error al insertar registros.")
        print("Código de Error:", insert_err.errno)
        print("SQLSTATE:", insert_err.sqlstate)
        print("Mensaje:", insert_err.msg)
    finally:
        cursor.close()  # Cerrar el cursor después de usarlo

def insertar_datos(cnx, sql, valores):
    """Inserta múltiples registros en la base de datos, omitiendo duplicados."""
    try:
        cursor = cnx.cursor()  # Crear un cursor a partir de la conexión
        for value in valores:
            # Construir la consulta para verificar si el registro ya existe
            # Obtener el nombre de la tabla de la consulta SQL
            table_name = sql.split(' ')[2]
            
            # Obtener las columnas de la consulta SQL
            columns = sql.split('(')[1].split(')')[0].split(', ')
            
            # Construir la consulta de verificación de duplicados
            check_sql = f"SELECT COUNT(*) FROM {table_name} WHERE " + " AND ".join(
                [f"{col} = %s" for col in columns]
            )
            
            # Ejecutar la consulta de verificación
            cursor.execute(check_sql, value)
            exists = cursor.fetchone()[0]

            if exists == 0:  # Si no existe, insertar el registro
                cursor.execute(sql, value)
            else:
                print(f"Registro ya existe: {value}")

        cnx.commit()  # Usar la conexión para hacer commit
        print(cursor.rowcount, "registro/s insertado/s.")
    except mysql.connector.Error as insert_err:
        print("⚠️ Error al insertar registros.")
        print("Código de Error:", insert_err.errno)
        print("SQLSTATE:", insert_err.sqlstate)
        print("Mensaje:", insert_err.msg)
    finally:
        cursor.close()  # Cerrar el cursor después de usarlo
# ------------------------------------------------------------------------------
ruta_excel = "midi_datos.xlsx"
hojas = cargar_datos_excel(ruta_excel)

# Conectar a la base de datos
try:
    cnx = conectar_base_datos()
    if cnx.is_connected():
        print("¡Conectado a la base de datos!")

        # Procesar cada hoja
        for nombre_hoja, df in hojas.items():
            print(f"Procesando hoja: {nombre_hoja}")
            print(df.head())

            # Crear DataFrame dinámicamente
            globals()[f'df_{nombre_hoja}'] = df

            # Convertir DataFrame a lista de tuplas
            lista_tuplas = convertir_a_tuplas(df)
            globals()[f'lista_{nombre_hoja}'] = lista_tuplas

            # Preparar la consulta SQL
            columnas = df.columns.tolist()
            placeholders = ', '.join(['%s'] * len(columnas))
            sql = f"INSERT INTO {nombre_hoja} ({', '.join(columnas)}) VALUES ({placeholders})"
            globals()[f'sql_{nombre_hoja}'] = sql

            # Insertar datos
            if lista_tuplas:  # Solo insertar si hay datos
                insertar_datos(cnx, sql, lista_tuplas)
            else:
                print(f"No hay datos para insertar en la hoja: {nombre_hoja}")

except mysql.connector.Error as conn_err:
    print("⚠️ Error al conectar a MySQL.")
    print("Código de Error:", conn_err.errno)
    print("SQLSTATE:", conn_err.sqlstate)
    print("Mensaje:", conn_err.msg)
finally:
    if 'cnx' in locals() and cnx.is_connected():
        cnx.close()
        print("Conexión MySQL cerrada.")