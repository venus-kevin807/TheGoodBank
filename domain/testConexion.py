from domain.sqlConnect import DatabaseConnector
##from domain.Product import Product
from domain.Person import Person


db = DatabaseConnector(host="localhost", port=3306, user="root", password= "", database="thegoodbank")

db.connect()

person = Person(None, None, None, None, None)

person.create_person()
person.insert(db)

##producto = Product(None, None)

