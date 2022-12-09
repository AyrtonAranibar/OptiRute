

class Cliente():

    def __init__(self, id, nombre, longitud, latitud, direccion, referencia, numero, fecha_creacion, correo, activo )-> None:
        self.id = id #reservar el nombre id para usos con diferentes componentes como "login_user"
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud
        self.direccion = direccion
        self.referencia = referencia
        self.numero = numero
        self.fecha_creacion = fecha_creacion
        self.correo = correo
        self.activo = activo
        
