from domain.Person import Person
from domain.Product import Product
from domain.Titular import Titular

class Asesor(Person):
    def __init__(self, id=None, name=None, last_name=None, mail=None, phone=None):
        super().__init__(id, name, last_name, mail, phone)

    def create_product(self):
        product = Product(None, None)
        product.create_product()
        return product

    def create_titular(self, product):
        titular = Titular(None, None, None, None, None, product, None)
        titular.create_person()
        return titular

    def insert(self, db):
        super().insert(db)  # Esto insertará los datos de la persona en la tabla Person
        query = "INSERT INTO Asesor (id) VALUES (%s)"
        values = (self.id,)
        result = db.execute_query(query, values)
        if result:
            print(f"Asesor {self.name} insertado correctamente en la base de datos.")
