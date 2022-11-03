from flask import Flask,render_template,request,redirect,url_for,flash
from config import config
from flask_mysqldb import MySQL
# from flaskext.mysql import MySQL
from datetime import datetime

#Modelos:
from models.ModelAdmin import ModelAdmin


#Entidades:
from models.entities.Admin import Admin

app = Flask(__name__)

db = MySQL(app)


mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='optirute_db'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('menu/index.html')

@app.route('/administrador')
def administrador():
    sql ="SELECT * FROM `administrador` where `activo` = 1 "
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    administradores = cursor.fetchall()
    print(administradores)
    conn.commit()
    return render_template('administradores/index.html', administradores=administradores)


@app.route('/crear')
def crear():
    return render_template('administradores/create.html')
    
@app.route('/guardar_administrador', methods=['POST'])
def guardarAdmin():
    _nombre = request.form['txtNombre']
    _contrasenia = request.form['txtContrasenia']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']
    _nombrecompleto = request.form['txtNombreCompleto']

    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    nuevoNombreFoto = ''
    if _foto.filename!='':
        nuevoNombreFoto = tiempo + _foto.filename
        _foto.save("uploads/" + nuevoNombreFoto)

    sql ="INSERT INTO `administrador` (`id_administrador`, `usuario`, `contrasenia`, `correo`, `imagen`, `nombre_completo`) VALUES (NULL,%s,%s,%s,%s,%s);"
    datos = (_nombre, _contrasenia, _correo, nuevoNombreFoto, _nombrecompleto)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('administradores/index.html')

@app.route('/eliminar_administrador/<int:id>')
def eliminar_administrador(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE `administrador` SET `activo` = "0" WHERE `administrador`.`id_administrador` =%s',(id))
    conn.commit();
    return redirect('/administrador')


@app.route('/ingresar', methods = ['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['contrasena'])
        admin = Admin(0,request.form['username'],request.form['contrasena'])
        logged_admin = ModelAdmin.ingreso(db,admin)
        if logged_admin != None:
            if logged_admin.contrasenia:
                return redirect(url_for('menu_administrador'))
            else:
                cursor.close()
                flash("Contraseña no valida")
                return render_template('ingreso/index.html')
        else:
            flash("Usuario no encontrado")
        return render_template('ingreso/index.html')
    else:
        return render_template('ingreso/index.html')

@app.route('/registrarse')
def registrarse():
    return render_template('ingreso/registro.html')

@app.route('/menu_administrador')
def menu_administrador():
    return render_template('administradores/admin_dashboard.html')

@app.route('/tablas')
def tablas():
    return render_template('administradores/pages/tables.html')

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run()

# if __name__=='__main__':
#     app.run(debug = True)
