# database.py

import mysql.connector
from mysql.connector import Error

# Configura estos datos con tu información de conexión
DB_CONFIG = {
    "host": "localhost",
    "user": "root",         # Reemplaza con tu usuario de MySQL
    "password": "",  # Reemplaza con tu contraseña
    "database": "sistema_experto_db"
}

def get_connection():
    """Establece y retorna una conexión a la base de datos."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error al conectar a MySQL:", e)
    return None

def get_padecimientos():
    """
    Retorna una lista de diccionarios con los padecimientos.
    Cada elemento tiene las claves: 'codigo', 'nombre' y 'descripcion'
    """
    connection = get_connection()
    padecimientos = []
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT codigo, nombre, descripcion FROM padecimientos")
            padecimientos = cursor.fetchall()
        except Error as e:
            print("Error al obtener padecimientos:", e)
        finally:
            cursor.close()
            connection.close()
    return padecimientos

def get_farmacos(padecimiento_codigo, categoria):
    """
    Retorna una lista de fármacos para un padecimiento y categoría dados.
    Cada fármaco es un diccionario con las claves: 'nombre', 'dosis' y 'contraindicaciones'
    """
    connection = get_connection()
    farmacos = []
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = ("SELECT nombre, dosis, contraindicaciones FROM farmacos "
                     "WHERE padecimiento_codigo = %s AND categoria = %s")
            cursor.execute(query, (padecimiento_codigo, categoria))
            farmacos = cursor.fetchall()
        except Error as e:
            print("Error al obtener fármacos:", e)
        finally:
            cursor.close()
            connection.close()
    return farmacos