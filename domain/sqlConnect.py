import mysql.connector

class DatabaseConnector:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )
            print("Conexión establecida.")
        except mysql.connector.Error as err:
            print(f"Error de conexión a la base de datos: {err}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Consulta ejecutada exitosamente")
            if query.lower().startswith('select'):
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta", error)
            return None
        finally:
            cursor.close()

    def execute_insert_query(self, query, values):
        if self.connection:
            try:
                cursor = self.connection.cursor(buffered=True)
                cursor.execute(query, values)
                self.connection.commit()
                cursor.close()
                print("Datos insertados correctamente.")
            except mysql.connector.Error as err:
                print(f"Error al ejecutar la consulta de inserción: {err}")
        else:
            print("No se pudo establecer la conexión.")

# Ejemplo de uso
db_connector = DatabaseConnector(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="thegoodbank"
)
db_connector.connect()

# Ejecutar una consulta
query = "SELECT * FROM Person"
results = db_connector.execute_query(query)

# Mostrar los resultados
if results:
    for row in results:
        print(row)

# Cerrar la conexión
db_connector.close()
