from .entities.Vehiculo import Vehiculo
from werkzeug.security import check_password_hash,generate_password_hash

class ModelVehiculo():

    @classmethod
    def crear_vehiculo(self, db, vehiculo):
        try:
            conn = db.connection
            sql = """INSERT INTO `vehiculo` (`estado`, `placa`, `activo`, `imagen`) 
                    VALUES ('{}','{}','{}','{}');""".format( vehiculo.estado, vehiculo.placa, vehiculo.activo, vehiculo.imagen)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_vehiculos(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, estado, placa, imagen, activo  FROM vehiculo"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            vehiculos = cursor.fetchall()
            return vehiculos
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_vehiculos_activos(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, estado, placa, imagen, activo FROM vehiculo WHERE activo = 1"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            vehiculos = cursor.fetchall()
            return vehiculos
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def eliminar_vehiculo(self, db, id):
        try:
            conn = db.connection
            sql = "UPDATE `vehiculo` SET `activo` = '0' WHERE `vehiculo`.`id` = '{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            vehiculo = cursor.fetchone()
            return vehiculo
        except Exception as ex:
            raise Exception(ex)
            
    @classmethod
    def get_vehiculo_id(self, db, id):
        try:
            conn = db.connection
            sql = "SELECT id, estado, placa, imagen, activo FROM vehiculo WHERE id ='{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            vehiculo = cursor.fetchone()
            return vehiculo
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_vehiculo(self, db, vehiculo):
        try:
            conn = db.connection
            sql = """UPDATE `vehiculo` SET `estado` = '{}',`placa` = '{}',`imagen` = '{}'
            WHERE `vehiculo`.`id` = '{}'""".format( vehiculo.estado, vehiculo.placa, vehiculo.imagen, vehiculo.id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            vehiculo = cursor.fetchone()
            return vehiculo
        except Exception as ex:
            raise Exception(ex)

