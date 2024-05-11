from domain.Person import Person
from domain.Savings_Account import SavingsAccount

class Titular(Person):
    def __init__(self, id=None, name=None, last_name=None, mail=None, phone=None, product=None, key=None, balance=0):
        super().__init__(id, name, last_name, mail, phone)
        self.product = product
        self.key = key
        self.balance = balance
        self.savings_account = None


    def create_savings_account(self):
        self.savings_account = SavingsAccount(self.id, "debit")

    def create_person(self):
        super().create_person()
        self.savings_account = SavingsAccount(self.id, "debit")
        self.key = int(input("Clave: "))
        print(f"Titular creado con éxito. Clave: {self.key}")

    def create_credit_card(self):
        super().create_person()
        self.savings_account = SavingsAccount(self.id, "credit")
        self.key = int(input("Clave: "))
        print(f"Tarjeta de crédito creada con límite de {self.savings_account.credit_limit}. Clave: {self.key}")
        print(f"Deuda de: {self.savings_account.debt}")
        return self.savings_account.create_card()

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"producto: {self.product}, "
            f"key: {self.key}, "
            f"balance: {self.balance}"
        )


    def select_user(self):
        for i in self.users.items():
            print(i)

    def transfer(self, amount, target_phone):
        user_input_key = int(input("Ingrese su clave para realizar la transferencia: "))

        # Verificar si la clave es correcta
        if user_input_key != self.key:
            print("Clave incorrecta. Transferencia cancelada.")
            return

        amount = int(input("Ingresa la cantidad de dinero a transferir: "))
        if amount <= 0 or amount > self.balance:
            print("Cantidad inválida para transferencia.")
            return

        target_phone = input("Ingresa el numero del telefono del destinatario: ")
        target_user = None
        for user in self.users.values():
            if user.phone == target_phone:
                target_user = user
                break

        if target_user is None:
            print("El teléfono del destinatario no existe.")
            return

        self.balance -= amount
        target_user.balance += amount

        print(f"Transferencia de {amount} realizada con éxito al teléfono {target_phone}.")


    def record(self, amount):
        # Clave ingresada para confirmar la consignación
        user_input_key = int(input("Ingrese su clave para realizar la consignación: "))  # Mantener el argumento original

        # Verificar si la clave es correcta
        if user_input_key != self.key:
            print("Clave incorrecta. Consignación cancelada.")  # Mensaje de error
            return

        # Solicitar el monto para consignar
        amount = int(input("Ingresa la cantidad de dinero a consignar: "))  # Solicitar el valor correcto
        if amount <= 0:
            print("Cantidad inválida para consignación. Debe ser mayor que cero.")  # Validación
            return

        # Actualizar el saldo del titular
        self.balance += amount
        print(f"Consignación de {amount} realizada con éxito. Nuevo saldo: {self.balance}.")  # Mensaje de éxito

    def withdra(self, amount):
        user_input_key = int(input("Ingrese su clave para realizar la consignación: "))  # Mantener el argumento original

        # Verificar si la clave es correcta
        if user_input_key != self.key:
            print("Clave incorrecta. Consignación cancelada.")  # Mensaje de error
            return

        amount = int(input("Ingresa la cantidad de dinero a retirar: "))
        if amount <= 0 or amount > self.balance:
            print("Cantidad inválida para retiro.")
            return

        self.balance -= amount
        print(f"Retiro de {amount} realizado con éxito. Nuevo saldo: {self.balance}.")

    def check_balance(self):
        user_input_key = int(input("Ingrese su clave para confirmar: "))

        if user_input_key != self.key:
            print("Clave incorrecta. Operación cancelada.")
            return

        print(f"El saldo actual es: {self.balance}")

        if self.savings_account:
            if self.savings_account.account_type == "credit":
                print(f"Límite de crédito restante: {self.savings_account.credit_limit}")
                print(f"Deuda pendiente: {self.savings_account.debt}")
        else:
            print("Cuenta de ahorros no creada.")
            return

    def insert(self, db):
        super().insert(db)  # Esto insertará los datos de la persona en la tabla Person
        query = "INSERT INTO Titular (id, id_product, key, balance) VALUES (%s, %s, %s, %s)"
        values = (self.id, self.product.id_product, self.key, self.balance)
        result = db.execute_query(query, values)
        if result:
            print(f"Titular {self.name} insertado correctamente en la base de datos.")

