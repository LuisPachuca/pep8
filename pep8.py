# CamelCase
# Identacion: 4 espacios (No tabs)
# Parametros separados por la "," deben de llevar un espacio
# snake_case
# espacios entre operadores
# Terminar scripts con un enter 


class UserAdmin():


    def __init__(self, username, password = ''):
        self.username = username
        self.password = password


    def set_password(self):
        pass


cody_user = UserAdmin('Cody')
