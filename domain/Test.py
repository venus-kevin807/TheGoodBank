from domain.Person import Person
from domain.Product import Product
from domain.Titular import Titular
from domain.Asesor import Asesor
from domain.UserSystem import UserSystem

from domain.sqlConnect import DatabaseConnector
from domain.Savings_Account import SavingsAccount


class Test:
    def __init__(self):
        self.user_system = UserSystem()
        self.product = None
        self.titular1 = None
        self.titular2 = None
        self.titular3 = None

    db = DatabaseConnector(host="localhost", port=3306, user="root", password="", database="bancokdapp")

    db.connect()

    def run(self):
        print("\nBienvenido al Sistema de Usuarios")
        while True:
            user_type = input("¿Es usted un Asesor o una Persona? (ase/asr para Asesor, per/prs para Persona): ").lower()
            if user_type in ["ase", "asr"]:
                self.user_system.set_user_type(Asesor)
                print("Usted ha seleccionado ser un Asesor.")
                break
            elif user_type in ["per", "prs"]:
                self.user_system.set_user_type(Person)
                print("Usted ha seleccionado ser una Persona.")
                break
            else:
                print("Tipo de usuario no válido. Por favor, intente de nuevo.")

        while True:
            print("\nMenú Principal:")
            print("1. Registrarse")
            print("2. Login")
            print("3. Crear Producto (solo para Asesor)")
            print("4. Crear Titular con Tarjeta de Crédito")
            print("5. Crear Titular con Tarjeta de Débito")
            print("5.1 Crear Titular con Tarjeta de Débito")
            print("6. Crear Persona")
            print("7. Mirar Titulares creados (solo para Asesor)")
            print("8. Consignar")
            print("8.1 Amortizar(Cuentas Crediticias)")
            print("9. Transferir")
            print("10. Retirar")
            print("11. Consultar saldo")
            print("12. Salir")

            option = input("Por favor, seleccione una opción: ")

            if option == "1":
                self.user_system.register()
            elif option == "2":
                self.user_system.login()
            elif option == "3":
                if self.user_system.get_user_type() == Asesor:
                    self.product = Product(None, None)
                    self.product.create_product()
                    self.product.insert(self.db)
                else:
                    print("Esta opción solo está disponible para Asesores.")
            elif option == "4":
                if self.titular1 is None:
                    self.titular1 = Titular(None, None, None, None, None, self.product, None, 0)
                    self.titular1.create_credit_card()
                    self.titular1.insert(self.db)
                    print("Titular con Tarjeta de Crédito creado con éxito.")
            elif option == "5":
                if self.titular2 is None:
                    self.titular2 = Titular(None, None, None, None, None, self.product, None, 0)
                    self.titular2.create_person()
                    print("Titular con Tarjeta de Débito creado con éxito.")
            elif option == "5.1":
                if self.titular3 is None:
                    self.titular3 = Titular(None, None, None, None, None, self.product, None, 0)
                    self.titular3.create_person()
                    print("Titular con Tarjeta de Débito creado con éxito.")
            elif option == "6":
                    self.person = Person(None, None, None, None, None)
                    self.person.create_person()
                    self.person.insert(self.db)
            elif option == "7":
                if self.user_system.get_user_type() == Asesor:
                    print("Usuarios en el sistema:")
                    for key, value in Person.users.items():
                        print(f"ID: {key}, Usuario: {value}")
                else:
                    print("Esta opción solo está disponible para Asesores.")
            elif option == "8":
                tit = input("¿Deseas actuar desde el Titular 2 o 3?: ")
                if tit == "3":
                    self.titular3.record(None)
                elif tit == "2":
                    self.titular2.record(None)
            elif option == "8.1":
                if self.titular1 is None:
                    print("Titular 1 no existe para amortizar.")
                    return

                user_input_key = int(input("Ingrese su clave para realizar la amortizacion: "))
                if user_input_key != self.titular1.key:
                    print("Clave incorrecta. Transferencia cancelada.")
                    return
                self.titular1.savings_account.amortize(None)
            elif option == "9":
                tit = input("¿Deseas actuar desde el Titular 2 o 3?: ")
                if tit == "2":
                    self.titular2.transfer(None, None)
                elif tit == "3":
                    self.titular3.transfer(None, None)
            elif option == "10":
                tit = input("¿Deseas actuar desde el Titular 1, 2 o 3?: ")
                if tit == "1":
                    amount = int(input("Ingresa la cantidad de dinero a retirar: "))
                    resultado = self.titular1.savings_account.withdraw(amount)
                elif tit == "2":
                    resultado = self.titular2.withdra(None)
                elif tit == "3":
                    resultado = self.titular3.withdra(None)
                else:
                    resultado = "Titular no válido."
                print(resultado)
            elif option == "11":
                tit = input("¿Deseas actuar desde el Titular 1, 2 o 3?: ")
                if tit == "1":
                    self.titular1.check_balance()
                elif tit == "2":
                    self.titular2.check_balance()
                elif tit == "3":
                    self.titular3.check_balance()
            elif option == "12":
                print("Gracias por usar el Sistema de Usuarios. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    test = Test()
    test.run()
