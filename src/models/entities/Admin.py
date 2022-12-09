from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

class Admin(UserMixin):

    def __init__(self, id_administrador, usuario, contrasenia, correo, imagen, nombre_completo )-> None:
        self.id = id_administrador #reservar el nombre id para usos con diferentes componentes como "login_user"
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.correo = correo
        self.imagen = imagen
        self.nombre_completo = nombre_completo
        
        
        
    
    @classmethod
    def check_password(self, hashed_password, contrasenia):
        return check_password_hash(hashed_password, contrasenia)