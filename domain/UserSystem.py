from domain.Person import Person

class UserSystem:
    def __init__(self):
        self.users = {}
        self.user_type = None

    def set_user_type(self, user_type):
        self.user_type = user_type

    def get_user_type(self):
        return self.user_type

    def register(self):
        if self.user_type:
            user_id = input("Ingrese su ID de usuario: ")
            name = input("Ingrese su nombre: ")
            last_name = input("Ingrese su apellido: ")
            mail = input("Ingrese su correo electrónico: ")
            phone = input("Ingrese su número de teléfono: ")
            user = self.user_type(user_id, name, last_name, mail, phone)
            self.users[user_id] = user
            print(f"Usuario {name} registrado con éxito.")
        else:
            print("Seleccione un tipo de usuario antes de registrar.")

    def login(self):
        user_id = input("Ingrese su ID de usuario: ")
        if user_id in self.users:
            user = self.users[user_id]
            print(f"Bienvenido {user.name}!")