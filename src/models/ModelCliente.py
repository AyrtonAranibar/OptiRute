from .entities.Cliente import Cliente

class ModelCliente():

    @classmethod
    def crear_cliente(self, db, cliente):
        try:
            conn = db.connection
            sql = """INSERT INTO `cliente` (`id`, `nombre`, `longitud`, `latitud`, `direccion`, `referencia`, `numero`, `fecha_creacion`, `correo`, `activo`) 
                    VALUES (0,'{}','{}','{}','{}','{}','{}','{}','{}','1');""".format( cliente.nombre, cliente.longitud, cliente.latitud, cliente.direccion, cliente.referencia, cliente.numero, cliente.fecha_creacion, cliente.correo)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_clientes(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, nombre, longitud, latitud, direccion, referencia, numero, fecha_creacion, correo, activo FROM cliente"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            clientes = cursor.fetchall()
            return clientes
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_clientes_activos(self, db):
        try:
            conn = db.connection
            sql = "SELECT id, nombre, longitud, latitud, direccion, referencia, numero, fecha_creacion, correo, activo FROM cliente WHERE activo = 1"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            clientes = cursor.fetchall()
            return clientes
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def eliminar_cliente(self, db, id):
        try:
            conn = db.connection
            sql = "UPDATE `cliente` SET `activo` = '0' WHERE `cliente`.`id` = '{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cliente = cursor.fetchone()
            return cliente
        except Exception as ex:
            raise Exception(ex)
            
    @classmethod
    def get_cliente_id(self, db, id):
        try:
            conn = db.connection
            sql = "SELECT id, nombre, longitud, latitud, direccion, referencia, numero, fecha_creacion, correo, activo FROM cliente WHERE id ='{}'".format(id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cliente = cursor.fetchone()
            return cliente
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_cliente(self, db, cliente):
        try:
            conn = db.connection
            sql = """UPDATE `cliente` SET `nombre` = '{}',`longitud` = '{}',`latitud` = '{}',`direccion` = '{}',
            `referencia` = '{}',`numero` = '{}',`correo` = '{}' WHERE `cliente`.`id` = '{}'""".format( cliente.nombre, cliente.longitud, cliente.latitud, cliente.direccion, cliente.referencia, cliente.numero, cliente.correo, cliente.id)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cliente = cursor.fetchone()
            return cliente
        except Exception as ex:
            raise Exception(ex)
