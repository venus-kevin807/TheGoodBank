class Product:
    def __init__(self, id_product, product_name):
        self.id_product = id_product
        self.product_name = product_name


    @staticmethod
    def from_row(row):
        return Product(row[0],row[1])

    def create_product(self):
        self.id_product = int(input("ID del producto: "))
        self.product_name = input("Nombre del producto: ")
        ##self.products[self.id_product] = self.product_name
        print(f"Producto {self.product_name} creado con éxito.")

    def select_product(self):
        for id, name in self.products.items():
            print(f"ID del producto: {id}, Nombre del producto: {name}")

    def insert(self, db):
        query = "INSERT INTO product (id_product, product_name) VALUES (%s, %s)"
        values = (self.id_product, self.product_name)
        result = db.execute_query(query, values)

        if result:
            print(f"Producto {self.product_name} insertado correctamente en la base de datos.")


