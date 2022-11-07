from .entities.Admin import Admin

class ModelAdmin():

    @classmethod
    def ingreso(self, db, admin):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id_administrador,usuario,contrasenia,correo,imagen,nombre_completo FROM administrador WHERE usuario = '{}'".format(admin.usuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                admin = Admin(row[0], row[1], Admin.check_password(row[2],admin.contrasenia), row[3], row[4], row[5])
                return admin
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id_administrador,usuario,correo,imagen,nombre_completo FROM administrador WHERE id_administrador = '{}'".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                logged_admin = Admin(row[0], row[1],None, row[2], row[3], row[4])
                return logged_admin
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def crear_usuario(self, db, admin):
        try:
            sql ="""INSERT INTO `administrador` (`id_administrador`, `usuario`, `contrasenia`, `correo` , `imagen` ,`nombre_completo` ) 
            VALUES (0,'{}','{}','{}','{}','{}');""".format(admin.usuario, admin.contrasenia, admin.correo, admin.imagen, admin.nombre_completo)
            conn = db.connection
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            raise Exception(ex)