class SavingsAccount:
    def __init__(self, account_id="default_id", account_type="debit"):
        self.account_id = account_id
        self.balance = 0
        self.account_type = account_type
        self.credit_limit = 10000
        self.amortization_schedule = []

        if self.account_type == "credit":
            self.credit_limit = 8000
            self.debt = 10000
        else:
            self.credit_limit = None
            self.debt = None

    def create_card(self):
        if self.account_type == "credit":
            return f"Tarjeta de crédito creada con límite de {self.credit_limit}"
        elif self.account_type == "debit":
            return "Tarjeta de débito creada"
        else:
            return "Tipo de cuenta no válido"

    def withdraw(self, amount):
        if self.account_type == "debit" and self.balance >= amount:
            self.balance -= amount
            return f"Retirados {amount}. Saldo actual: {self.balance}"
        elif self.account_type == "credit" and self.credit_limit >= amount:
            self.credit_limit -= amount
            self.amortization_schedule.append({
                "amount": amount,
                "status": "pending",
            })
            return f"Retirados {amount} como crédito. Límite restante: {self.credit_limit}"
        else:
            return "Fondos insuficientes"

    def amortize(self, amount):
        if self.account_type != "credit":
            print("Solo se puede amortizar en cuentas de crédito.")
            return
        amount = int(input("Ingrese la cantidad para amortizar: "))
        if amount <= 0 or amount > self.debt:
            print("Cantidad para amortizar no válida. Debe ser mayor que cero y menor o igual a la deuda actual.")
            return

        self.debt -= amount
        print(f"Amortización de {amount} realizada con éxito. Deuda restante: {self.debt}.")  # Mensaje final

    def check_balance_credit(self, titular_key):
        user_input_key = int(input("Ingrese su clave para confirmar: "))

        if user_input_key != titular_key:
            print("Clave incorrecta. Operación cancelada.")
            return

        print(f"Límite de crédito restante: {self.credit_limit}")
        print(f"Deuda pendiente: {self.debt}")

    def insert(self, db):
        query = "INSERT INTO SavingsAccount (account_id, balance, account_type, credit_limit, amortization_schedule) VALUES (%s, %s, %s, %s, %s)"
        amortization_schedule_str = str(self.amortization_schedule)
        values = (self.account_id, self.balance, self.account_type, self.credit_limit, amortization_schedule_str)
        result = db.execute_query(query, values)
        if result:
            print(f"Cuenta de ahorros {self.account_id} insertada correctamente en la base de datos.")
