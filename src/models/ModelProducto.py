from .entities.Producto import Producto

class ModelProducto():

    @classmethod
    def crear_producto(self, db, producto):
        try:
            conn = db.connection
            sql = """INSERT INTO `productos` (`id`, `nombre`, `peso`, `descripcion`, `precio`) 
                    VALUES (0,'{}','{}','{}','{}');""".format( producto.nombre, producto.peso, producto.descripcion, producto.precio)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_productos(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, nombre, peso, descripcion, precio, activo FROM productos"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            productos = cursor.fetchall()
            return productos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_productos_activos(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, nombre, peso, descripcion, precio, activo FROM productos WHERE activo = 1"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            productos = cursor.fetchall()
            return productos
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_productos_nombres(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, nombre FROM productos WHERE activo = 1"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            productos = cursor.fetchall()
            return productos
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def eliminar_producto(self, db, id):
        try:
            conn = db.connection
            sql = "UPDATE `productos` SET `activo` = '0' WHERE `producto`.`id` = '{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            producto = cursor.fetchone()
            return producto
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_producto_id(self, db, id):
        try:
            conn = db.connection
            sql = "SELECT  id, nombre, peso, descripcion, precio, activo FROM productos WHERE id = '{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            producto = cursor.fetchone()
            return producto
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_producto(self, db, producto):
        try:
            conn = db.connection
            sql = """UPDATE `productos` SET `nombre` = '{}',`peso` = '{}',`descripcion` = '{}',`precio` = '{}'
            WHERE `productos`.`id` = '{}'""".format( producto.nombre, producto.peso, producto.descripcion, producto.precio, producto.id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            producto = cursor.fetchone()
            return producto
        except Exception as ex:
            raise Exception(ex)