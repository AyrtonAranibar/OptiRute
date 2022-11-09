from flask import Flask,render_template,request,redirect,url_for,flash
from config import config
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager,login_user,logout_user,login_required
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash
import requests



import openrouteservice
from openrouteservice import convert
import folium



import numpy as np #numpy de toda la vida
### Libreria de optimizacion ###
import hygese as hgs

#Modelos:
from models.ModelAdmin import ModelAdmin
import json 

#Entidades:
from models.entities.Admin import Admin

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelAdmin.get_id(db,id)


matriz_distancias = []
array_pedidos = []

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
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    administradores = cursor.fetchall()
    # print(administradores)
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

################## ENTREGAS ##################

@app.route('/entregas')
@login_required
def entregas():
    sql ="SELECT * FROM `entrega` where `activo` = 1 "
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    entregas = cursor.fetchall()
    conn.commit()
    return render_template('administradores/entregas/index.html', entregas=entregas)

@app.route('/entregas/crear_entrega', methods=['GET', 'POST'])
@login_required
def crear_entrega():
    if request.method == 'POST':

        peso = request.form['peso']
        coordenadas = request.form['coordenada']
        coordenadas = json.loads(coordenadas)
        longitud = coordenadas['lng']
        latitud = coordenadas['lat']
        nombre = request.form['nombre']
        
        sql ="""INSERT INTO `entrega` (`id`, `peso`, `longitud`, `latitud`, `nombre_receptor`) 
        VALUES (0,'{}','{}','{}','{}');""".format( peso, longitud, latitud, nombre)
        conn = db.connection
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        flash("Entrega creada con éxito")
        return render_template('administradores/entregas/crear.html')
    else:
        return render_template('administradores/entregas/crear.html')

############################ RUTAS ######################

@app.route('/rutas')
@login_required
def rutas():
    sql ="SELECT * FROM `entrega` where `activo` = 1 "
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    entregas = cursor.fetchall()
    conn.commit()


    # client = openrouteservice.Client(key='5b3ce3597851110001cf62488b5f9fc52aec4396a6e94f225de93894')
    
    # matriz_distancias = []
    # fila_matriz = []
    # for entrega1 in entregas:
    #     fila_matriz.clear()
    #     for entrega2 in entregas:
    #         if (entrega1[3] != entrega2[3] and entrega1[2] != entrega2[2]):
    #             coordenada = ((  float(entrega1[2])  ,   float(entrega1[3])  ) , (  float(entrega2[2])  ,  float(entrega2[3])   ))
    #             lugar = entrega1[4] + entrega2[4]
    #             print(lugar)
    #             respuesta = client.directions(coordenada)
    #             distancia = round(respuesta['routes'][0]['summary']['distance'])
    #         else:
    #             distancia = 0
    #         fila_matriz.append(distancia)
    #     matriz_distancias.append(fila_matriz.copy())
    # print(matriz_distancias)

    # headers = {
    # 'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    # }
    # call = requests.get('https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf62488b5f9fc52aec4396a6e94f225de93894&start=-71.5279236901535,-16.41041958501789&end=-71.5070003854512,-16.4018162742952', headers=headers)

    # print(call.status_code, call.reason)
    # res = json.loads(call.text)
    # distancia = round(res['features'][0]['properties']['segments'][0]["distance"])
    # print(distancia)



    # with(open('test.json','+w')) as f:
    #     f.write(json.dumps(res,indent=4, sort_keys=True))

    #set location coordinates in longitude,latitude order
    coords = ((-71.5279236901535,-16.41041958501789),(-71.5070003854512,-16.4018162742952))
    #call API
    # res = client.directions(coords)
    #test our response
    # with(open('test.json','+w')) as f:
    #     f.write(json.dumps(res,indent=4, sort_keys=True))
    # geometry = client.directions(coords)['routes'][0]['geometry']
    # decoded = convert.decode_polyline(geometry)



    # distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
    # duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"

    #Matriz de distancias#


    #Mapa#
    m = folium.Map(location=[-16.41041958501,-71.5279236901],zoom_start=13, control_scale=True,tiles="cartodbpositron")
    # folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt,max_width=300)).add_to(m)

    for entrega in entregas:
        if (entrega[0] != 0):
            coordenada = (entrega[3],entrega[2])

            folium.Marker(
            location=list(coordenada),
            popup= entrega[4],
            icon=folium.Icon(color="blue"),
            ).add_to(m)
        
    folium.Marker(
        location=list(coords[0][::-1]),
        popup="Qaliwarma",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    m.save('src/templates/map.html')

    return render_template('administradores/rutas/index.html', entregas=entregas)


@app.route('/ruta/generar_ruta')
@login_required
def generar_ruta():
    sql ="SELECT * FROM `entrega` where `activo` = 1 "
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    entregas = cursor.fetchall()
    conn.commit()

    client = openrouteservice.Client(key='5b3ce3597851110001cf62488b5f9fc52aec4396a6e94f225de93894')
    
    matriz_distancias.clear()
    array_pedidos.clear()

    fila_matriz = []
    for entrega1 in entregas:
        fila_matriz.clear()
        

        array_pedidos.append(entrega1[1])
        for entrega2 in entregas:
            if (entrega1[3] != entrega2[3] and entrega1[2] != entrega2[2]):
                coordenada = ((  float(entrega1[2])  ,   float(entrega1[3])  ) , (  float(entrega2[2])  ,  float(entrega2[3])   ))
                lugar = entrega1[4] + entrega2[4]
                print(lugar)
                respuesta = client.directions(coordenada)
                distancia = round(respuesta['routes'][0]['summary']['distance'])
            else:
                distancia = 0
            fila_matriz.append(distancia)
        matriz_distancias.append(fila_matriz.copy())
    print(matriz_distancias)
    print(array_pedidos)



    #### Algoritmos geneticos ####
    data = dict()
    data['distance_matrix'] = matriz_distancias
    data['num_vehicles'] = 2
    data['depot'] = 0
    data['demands'] = array_pedidos
    data['vehicle_capacity'] = 1400  # different from OR-Tools: homogeneous capacity
    data['service_times'] = np.zeros(len(data['demands']))

    # Solver initialization
    ap = hgs.AlgorithmParameters(timeLimit=20)  # seconds
    hgs_solver = hgs.Solver(parameters=ap, verbose=True)

    # Solve
    result = hgs_solver.solve_cvrp(data)
    print("solucion:")
    print(result.cost)
    print(result.routes)
    return render_template('administradores/rutas/index.html', entregas=entregas)


############################ PROTOCOLOS ######################

def status_401(error):
    return render_template('codigos_http/401.html')

def status_404(error):
    return render_template('codigos_http/404.html')

################################### Test #########################

@app.route('/map')
def map():
    return render_template('map.html')


############################################################
if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()





# if __name__=='__main__':
#     app.run(debug = True)
