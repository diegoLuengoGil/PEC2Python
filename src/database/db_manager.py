import sqlite3
import os


class DBManager:
    """
    Maneja la conexion con la base de datos
    """

    def __init__(self, db_path="store.db", schema_path="resources\schema.sql"):
        self.db_path = db_path
        self.schema_path = schema_path
        self.connection = None

    def connect(self):
        """
        Inicia la conexion con la base de datos
        """
        msg = "Exito en la conexion"

        try:
            if not self.connection:
                self.connection = sqlite3.connect(self.db_path)
                # Enable foreign keys
                self.connection.execute("PRAGMA foreign_keys = ON")
        except sqlite3.Error as e:
            msg = f"Error conectando a la base de datos: {e}"

        return msg

    def close(self):
        """
        Cierra la conexion con la base de datos
        """
        resultado = False
        if self.connection:
            self.connection.close()
            self.connection = None
            resultado = True
        return resultado

    def initialize_database(self):
        """
        Lee el script de la base de datos y lo ejecuta
        """
        resultado = "Base de datos iniciada"
        try:
            self.connect()
            if os.path.exists(self.schema_path):
                with open(self.schema_path, "r", encoding="utf-8") as f:
                    schema_sql = f.read()
                self.connection.executescript(schema_sql)
            else:
                resultado = f"Error: El archivo del script '{self.schema_path}' no se a encontrado."
        except sqlite3.Error as e:
            resultado = f"Error al iniciar la base de datos: {e}"
        except OSError as e:
            resultado = f"Error en el archivo: {e}"

        return resultado


    def get_connection(self):
        """Devuelve la conxion."""
        connection = self.connection
        if connection is None:
            self.connect()
            connection = self.connection
        return connection
