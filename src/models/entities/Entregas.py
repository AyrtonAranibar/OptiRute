

class Entregas():

    def __init__(self, id, cliente_id, producto_id, cantidad, fecha, fecha_entrega, estado )-> None:
        self.id = id #reservar el nombre id para usos con diferentes componentes como "login_user"
        self.cliente_id = cliente_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.fecha = fecha
        self.fecha_entrega = fecha_entrega
        self.estado = estado
        
