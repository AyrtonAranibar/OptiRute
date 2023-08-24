from .entities.Sede import Sede

class ModelSede():

    @classmethod
    def crear_sede(self, db, sede):
        try:
            conn = db.connection
            sql = """INSERT INTO `sede` (`id`, `peso`, `longitud`, `latitud`, `nombre_receptor`) 
                    VALUES (0,'{}','{}','{}','{}');""".format( sede.peso, sede.longitud, sede.latitud, sede.nombre_receptor)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_sede(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, nombre_sede, direccion_sede, longitud, latitud FROM sede WHERE id = 1"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            sede = cursor.fetchone()
            return sede
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def editar_sede(self, db, sede):
        try:
            conn = db.connection
            sql = """UPDATE `sede` SET `nombre_sede` = '{}',`direccion_sede` = '{}',`longitud` = '{}',`latitud` = '{}'
             WHERE `sede`.`id` = '{}'""".format( sede.nombre_sede, sede.direccion_sede, sede.longitud, sede.latitud, sede.id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            sede = cursor.fetchone()
            return sede
        except Exception as ex:
            raise Exception(ex)

    
    
    
    
