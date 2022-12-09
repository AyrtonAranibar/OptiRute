from .entities.Transportista import Transportista
from werkzeug.security import check_password_hash,generate_password_hash

class ModelTransportista():

    @classmethod
    def crear_transportista(self, db, transportista):
        try:
            conn = db.connection
            sql = """INSERT INTO `transportista` (`nombre`, `usuario`, `contraseña`, `numero`, `correo`, `imagen`) 
                    VALUES ('{}','{}','{}','{}','{}','{}');""".format( transportista.nombre, transportista.usuario, transportista.contrasenia, transportista.numero, transportista.correo, transportista.imagen)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_transportistas(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, nombre, usuario, numero, correo, imagen, activo FROM transportista"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            transportistas = cursor.fetchall()
            return transportistas
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_transportistas_activos(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, nombre, usuario, numero, correo, imagen, activo FROM transportista WHERE activo = 1"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            transportistas = cursor.fetchall()
            return transportistas
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def eliminar_transportista(self, db, id):
        try:
            conn = db.connection
            sql = "UPDATE `transportista` SET `activo` = '0' WHERE `transportista`.`id` = '{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            transportista = cursor.fetchone()
            return transportista
        except Exception as ex:
            raise Exception(ex)
            
    @classmethod
    def get_transportista_id(self, db, id):
        try:
            conn = db.connection
            sql = "SELECT id, nombre, usuario, numero, correo, imagen, activo FROM transportista WHERE id ='{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            transportista = cursor.fetchone()
            return transportista
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_transportista(self, db, transportista):
        try:
            conn = db.connection
            sql = """UPDATE `transportista` SET `nombre` = '{}',`numero` = '{}',`correo` = '{}',`imagen` = '{}'
            WHERE `transportista`.`id` = '{}'""".format( transportista.nombre, transportista.numero, transportista.correo, transportista.imagen, transportista.id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            transportista = cursor.fetchone()
            return transportista
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def check_password(self, hashed_password, contrasenia):
        return check_password_hash(hashed_password, contrasenia)