

class Entrega():

    def __init__(self, id, peso, longitud, latitud, nombre_receptor, fecha_creacion, activo )-> None:
        self.id = id #reservar el nombre id para usos con diferentes componentes como "login_user"
        self.peso = peso
        self.longitud = longitud
        self.latitud = latitud
        self.nombre_receptor = nombre_receptor
        self.fecha_creacion = fecha_creacion
        self.activo = activo
        
