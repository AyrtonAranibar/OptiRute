from flask import Flask,render_template,request,redirect,url_for,flash
from config import config
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager,login_user,logout_user,login_required
# from flaskext.mysql import MySQL
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash
#Modelos:
from models.ModelAdmin import ModelAdmin


#Entidades:
from models.entities.Admin import Admin

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelAdmin.get_id(db,id)

########## CODIGO ANTIGUO ############
# mysql = MySQL()
# app.config['MYSQL_DATABASE_HOST']='localhost'
# app.config['MYSQL_DATABASE_USER']='root'
# app.config['MYSQL_DATABASE_PASSWORD']=''
# app.config['MYSQL_DATABASE_DB']='optirute_db'
# mysql.init_app(app)

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
    _contrasenia = generate_password_hash(request.form['txtContrasenia'])
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']
    _nombrecompleto = request.form['txtNombreCompleto']
    
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    nuevoNombreFoto = ''
    if _foto.filename!='':
        nuevoNombreFoto = tiempo + _foto.filename
        _foto.save("uploads/" + nuevoNombreFoto)

    admin = Admin(0,_nombre, _contrasenia, _correo, nuevoNombreFoto, _nombrecompleto)
    ModelAdmin.crear_usuario(db, admin)

    # cursor = db.connection.cursor()
    # sql ="""INSERT INTO `administrador` (`id_administrador`, `usuario`, `contrasenia`, `correo`, `imagen`, `nombre_completo`) 
    # VALUES (0,'{}','{}','{}','{}','{}');""".format(_nombre, _contrasenia, _correo, nuevoNombreFoto, _nombrecompleto)
    # conn = db.connection
    # cursor = conn.cursor()
    # cursor.execute(sql)
    # conn.commit()
    flash("Usuario "+_nombre+" creado con exito")
    return redirect('ingresar')

@app.route('/eliminar_administrador/<int:id>')
def eliminar_administrador(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE `administrador` SET `activo` = "0" WHERE `administrador`.`id_administrador` =%s',(id))
    conn.commit();
    return redirect('/administrador')



###################################################################


@app.route('/ingresar', methods = ['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['contrasena'])
        admin = Admin(0,request.form['username'],request.form['password'],0,0,0)
        logged_admin = ModelAdmin.ingreso(db,admin)
        if logged_admin != None:
            if logged_admin.contrasenia:
                login_user(logged_admin)
                return redirect(url_for('menu_administrador'))
            else:
                flash("Contraseña no valida")
                return redirect('ingresar')
        else:
            flash("Usuario no encontrado")
        return redirect('ingresar')
    else:
        return render_template('ingreso/index.html')

@app.route('/logout')
def logout():
    logout_user()
    return render_template('ingreso/index.html')


@app.route('/registrarse')
def registrarse():
    return render_template('ingreso/registro.html')

@app.route('/menu_administrador')#ruta protegida#
@login_required
def menu_administrador():
    return render_template('administradores/admin_dashboard.html')

@app.route('/tablas')
def tablas():
    return render_template('administradores/pages/tables.html')


############################ PROTOCOLOS ######################

def status_401(error):
    return render_template('codigos_http/401.html')

def status_404(error):
    return render_template('codigos_http/404.html')

############################################################
if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()





# if __name__=='__main__':
#     app.run(debug = True)
