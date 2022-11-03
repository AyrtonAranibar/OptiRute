from werkzeug.security import check_password_hash,generate_password_hash

class Admin():

    def __init__(self, id_administrador, usuario, contrasenia, nombre_completo="" )-> None:
        self.id_administrador = id_administrador
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.nombre_completo = nombre_completo
    
    @classmethod
    def check_password(self, hashed_password, contrasenia):
        return check_password_hash(hashed_password, contrasenia)
    
# print(generate_password_hash("contrasenia_complicada"))