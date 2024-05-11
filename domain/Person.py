
from domain.sqlConnect import DatabaseConnector

class Person:

    def __init__(self, id,name, last_name, mail, phone):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._mail = mail
        self._phone = phone

        Person.users[self.id] = self

    users = {}

    # Crear una instancia de DatabaseConnector
    db_connector = DatabaseConnector(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="thegoodbank"
    )

    # Conectar a la base de datos
    db_connector.connect()

    #Getter and Setter
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone


    # Metodos propios
    def create_person(self):
        self._id = int(input("Id: "))
        self._name = input("Name: ")
        self._last_name = input("LastName: ")
        self._mail = input("Mail: ")
        self._phone = input("Phone: ")

        # Asegurarse de que el ID es único y válido antes de añadir al diccionario
        if self._id in Person.users:
            print("ID ya existe, elija otro ID.")
            return

        # Agregar al diccionario solo si el ID es válido
        Person.users[self._id] = self


    def __str__(self):
        return (
            f"id: {self.id}, "
            f"name: {self.name}, "
            f"last_name: {self.last_name}, "
            f"Mail: {self.mail}, "
            f"Phone: {self.phone}"
        )

    def insert(self, db):
        query = "INSERT INTO Person (id, name, last_name, mail, phone) VALUES (%s, %s, %s, %s, %s)"
        values = (self.id, self.name, self.last_name, self.mail, self.phone)
        result = db.execute_query(query, values)

        if result:
            print(f"Persona {self.name} insertado correctamente en la base de datos.")