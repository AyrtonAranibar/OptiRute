from .entities.Admin import Admin

class ModelAdmin():

    @classmethod
    def ingreso(self, db, admin):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_administrador,usuario,contrasenia,nombre_completo FROM administrador
                    WHERE usuario = '{}'""".format(admin.usuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                admin = Admin(row[0], row[1], Admin.check_password(row[2],admin.contrasenia), row[3])
                return admin
            else:
                return None
        except Exception as ex:
            raise Exception(ex)