from .entities.Entrega import Entrega

class ModelEntrega():

    @classmethod
    def crear_entrega(self, db, entrega):
        try:
            conn = db.connection
            sql = """INSERT INTO `entrega` (`id`, `peso`, `longitud`, `latitud`, `nombre_receptor`) 
                    VALUES (0,'{}','{}','{}','{}');""".format( entrega.peso, entrega.longitud, entrega.latitud, entrega.nombre_receptor)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_entregas(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, peso, longitud, latitud, nombre_receptor, fecha_creacion, activo FROM entrega"
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
            sql = "SELECT id, peso, longitud, latitud, nombre_receptor, fecha_creacion, activo FROM entrega WHERE activo = 1"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            entregas = cursor.fetchall()
            return entregas
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def eliminar_entrega(self, db, id):
        try:
            conn = db.connection
            sql = "UPDATE `entrega` SET `activo` = '0' WHERE `entrega`.`id` = '{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            entrega = cursor.fetchone()
            return entrega
        except Exception as ex:
            raise Exception(ex)
