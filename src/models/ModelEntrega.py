from .entities.Entregas import Entregas

class ModelEntrega():

    @classmethod
    def crear_entrega(self, db, entregas):
        try:
            conn = db.connection
            sql = """INSERT INTO `entregas` (`id`, `cliente_id`, `producto_id`, `cantidad`, `fecha`, `fecha_entrega`, `estado`) 
                    VALUES (0,'{}','{}','{}','{}','{}','{}');""".format( entregas.cliente_id ,entregas.producto_id, entregas.cantidad, entregas.fecha, entregas.fecha_entrega, entregas.estado)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_entregas(self, db):
        try:
            conn = db.connection
            sql = """SELECT 
                    entregas.id,
                    cliente.nombre AS nombre_cliente,
                    productos.nombre AS nombre_producto,
                    entregas.cantidad,
                    entregas.fecha,
                    entregas.fecha_entrega,
                    entregas.estado,
                    entregas.activo
                    FROM entregas
                    INNER JOIN cliente ON entregas.cliente_id = cliente.id
                    INNER JOIN productos ON entregas.producto_id = productos.id;"""
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            entregas = cursor.fetchall()
            return entregas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_entregas_activas(self, db):
        try:
            conn = db.connection
            sql = """SELECT 
                    entregas.id,
                    cliente.nombre AS nombre_cliente,
                    productos.nombre AS nombre_producto,
                    entregas.cantidad,
                    entregas.fecha,
                    entregas.fecha_entrega,
                    entregas.estado,
                    entregas.activo
                    FROM entregas
                    INNER JOIN cliente ON entregas.cliente_id = cliente.id
                    INNER JOIN productos ON entregas.producto_id = productos.id WHERE entregas.activo = 1"""
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            entregas = cursor.fetchall()
            return entregas
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def eliminar_entregas(self, db, id):
        try:
            conn = db.connection
            sql = "UPDATE `entregas` SET `activo` = '0' WHERE `entregas`.`id` = '{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            entregas = cursor.fetchone()
            return entregas
        except Exception as ex:
            raise Exception(ex)
