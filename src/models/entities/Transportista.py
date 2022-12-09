

class Transportista():

    def __init__(self, id, nombre, usuario, contrasenia, numero, correo, imagen, activo )-> None:
        self.id = id #reservar el nombre id para usos con diferentes componentes como "login_user"
        self.nombre = nombre
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.numero = numero
        self.correo = correo
        self.imagen = imagen
        self.activo = activo
        
