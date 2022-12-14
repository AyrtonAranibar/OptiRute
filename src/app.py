from flask import Flask,render_template,request,redirect,url_for,flash,send_from_directory
from config import config
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager,login_user,logout_user,login_required
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash
import requests
import numpy
import asyncio

import openrouteservice
from openrouteservice import convert
import folium

#test
# import pytest

import numpy as np #numpy de toda la vida
### Libreria de optimizacion ###
import hygese as hgs

#Modelos:
from models.ModelAdmin import ModelAdmin
from models.ModelEntrega import ModelEntrega
from models.ModelCliente import ModelCliente
from models.ModelTransportista import ModelTransportista
from models.ModelVehiculo import ModelVehiculo

import json 
import os

#Entidades:
from models.entities.Admin import Admin
from models.entities.Entrega import Entrega
from models.entities.Cliente import Cliente
from models.entities.Transportista import Transportista
from models.entities.Vehiculo import Vehiculo

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelAdmin.get_id(db,id)


matriz_distancias = []
array_pedidos = []
########## UPLOADS ############

CARPETA = os.path.join('uploads')
app.config['CARPETA'] = CARPETA

@app.route('/uploads/<nombreFoto>')
@login_required
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)

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
                flash("Contrase??a no valida")
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


################## CLIENTES ##################

@app.route('/clientes')
@login_required
def clientes():
    clientes = ModelCliente.get_clientes_activos(db)
    return render_template('administradores/clientes/index.html', clientes=clientes)



@app.route('/clientes/crear_cliente', methods=['GET', 'POST'])
@login_required
def crear_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        coordenadas = request.form['coordenada']
        coordenadas = json.loads(coordenadas)
        longitud = coordenadas['lng']
        latitud = coordenadas['lat']
        direccion = request.form['direccion']
        referencia = request.form['referencia']
        numero = request.form['numero']
        correo = request.form['correo']
        fecha = datetime.now() 

        cliente = Cliente(0, nombre, longitud, latitud, direccion, referencia, numero, fecha, correo, 0)
        nueva_entrega = ModelCliente.crear_cliente(db, cliente)

        if (cliente != None):
            flash("Entrega "+nombre+" creada con ??xito")
        else:
            flash("Ha ocurrido un error!")
        return render_template('administradores/clientes/crear.html')
    else:
        return render_template('administradores/clientes/crear.html')


@app.route('/clientes/eliminar_cliente/<int:id>', methods=['GET'])
@login_required
def eliminar_cliente(id):
    cliente_eliminado = ModelCliente.eliminar_cliente(db, id)
    flash("Cliente eliminado con ??xito")
    clientes = ModelCliente.get_clientes_activos(db)
    return render_template('administradores/clientes/index.html', clientes=clientes)


@app.route('/clientes/editar_cliente/<int:id>', methods=['GET'])
@login_required
def editar_cliente(id):
    cliente = ModelCliente.get_cliente_id(db, id)
    return render_template('administradores/clientes/editar.html', cliente=cliente)

@app.route('/clientes/guardar_cliente/', methods=['POST'])
@login_required
def guardar_cliente():
    id = request.form['id']
    nombre = request.form['nombre']
    coordenadas = request.form['coordenada']
    coordenadas = json.loads(coordenadas)
    longitud = coordenadas['lng']
    latitud = coordenadas['lat']
    direccion = request.form['direccion']
    referencia = request.form['referencia']
    numero = request.form['numero']
    correo = request.form['correo']
    cliente = Cliente(id, nombre, longitud, latitud, direccion, referencia, numero,0, correo, 0)
    cliente = ModelCliente.editar_cliente(db,cliente)
    clientes = ModelCliente.get_clientes_activos(db)
    return render_template('administradores/clientes/index.html', clientes=clientes)




################ ENTREGAS ################
@app.route('/entregas')
@login_required
def entregas():
    entregas = ModelEntrega.get_entregas_activas(db)
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

        entrega = Entrega(0, peso, longitud, latitud, nombre, 0, 0)
        nueva_entrega = ModelEntrega.crear_entrega(db, entrega)

        if (entregas != None):
            flash("Entrega "+nombre+" creada con ??xito")
        else:
            flash("Ha ocurrido un error!")
        return render_template('administradores/entregas/crear.html')
    else:
        return render_template('administradores/entregas/crear.html')



@app.route('/entregas/eliminar_entrega/<int:id>', methods=['GET'])
@login_required
def eliminar_entrega(id):
    entrega_eliminada = ModelEntrega.eliminar_entrega(db, id)
    flash("Entrega eliminada con ??xito")
    entregas = ModelEntrega.get_entregas_activas(db)
    return render_template('administradores/entregas/index.html', entregas=entregas)

################ TRANSPORTISTAS ################

@app.route('/transportistas')
@login_required
def transportistas():
    transportistas = ModelTransportista.get_transportistas_activos(db)
    return render_template('administradores/transportistas/index.html', transportistas=transportistas)



@app.route('/transportistas/crear_transportista', methods=['GET', 'POST'])
@login_required
def crear_transportista():
    if request.method == 'POST':
        # (`id`, `nombre`, `usuario`, `contrasenia`, `numero`, `correo`, `imagen`, `activo`) 
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        contrasenia = generate_password_hash(request.form['contrasenia'])
        numero = request.form['numero']
        correo = request.form['correo']
        imagen = request.files['imagen']

        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        nuevoNombreFoto = ''
        if imagen.filename!='':
            nuevoNombreFoto = tiempo + imagen.filename
            imagen.save("uploads/" + nuevoNombreFoto)
        transportista = Transportista(0, nombre, usuario, contrasenia, numero, correo, nuevoNombreFoto, 1)
        ModelTransportista.crear_transportista(db, transportista)

        print("el nombre es "+transportista.nombre)

        if (transportista != None):
            flash("Transportista "+nombre+" creado con ??xito")
        else:
            flash("Ha ocurrido un error!")
        return render_template('administradores/transportistas/crear.html')
    else:
        return render_template('administradores/transportistas/crear.html')


@app.route('/transportistas/eliminar_transportista/<int:id>', methods=['GET'])
@login_required
def eliminar_transportista(id):
    transportista_eliminado = ModelTransportista.eliminar_transportista(db, id)
    flash("transportista eliminado con ??xito")
    transportistas = ModelTransportista.get_transportistas_activos(db)
    return render_template('administradores/transportistas/index.html', transportistas=transportistas)


@app.route('/transportistas/editar_transportista/<int:id>', methods=['GET'])
@login_required
def editar_transportista(id):
    transportista = ModelTransportista.get_transportista_id(db, id)
    return render_template('administradores/transportistas/editar.html', transportista=transportista)

@app.route('/transportistas/guardar_transportista/', methods=['POST'])
@login_required
def guardar_transportista():
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    numero = request.form['numero']
    correo = request.form['correo']
    imagen = request.files['imagen']

    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    nuevoNombreFoto = ''
    if imagen.filename!='':
        nuevoNombreFoto = tiempo + imagen.filename
        imagen.save("uploads/" + nuevoNombreFoto)
    transportista = Transportista(0, nombre, usuario, None, numero, correo, nuevoNombreFoto, 1)
    ModelTransportista.crear_transportista(db, transportista)
    transportista = ModelTransportista.editar_transportista(db,transportista)
    transportistas = ModelTransportista.get_transportistas_activos(db)
    return render_template('administradores/transportistas/index.html', transportistas=transportistas)


################ VEHICULOS ################

@app.route('/vehiculos')
@login_required
def vehiculos():
    vehiculos = ModelVehiculo.get_vehiculos_activos(db)
    return render_template('administradores/vehiculos/index.html', vehiculos=vehiculos)



@app.route('/vehiculos/crear_vehiculo', methods=['GET', 'POST'])
@login_required
def crear_vehiculo():
    if request.method == 'POST':
        # (id, estado, placa, activo, imagen) 
        estado = request.form['estado']
        placa = request.form['placa']
        imagen = request.files['imagen']

        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        nuevoNombreFoto = ''
        if imagen.filename!='':
            nuevoNombreFoto = tiempo + imagen.filename
            imagen.save("uploads/" + nuevoNombreFoto)
        vehiculo = Vehiculo(0, estado, placa, 1, nuevoNombreFoto)
        ModelVehiculo.crear_vehiculo(db, vehiculo)

        if (vehiculo != None):
            flash("Vehiculo "+placa+" creado con ??xito")
        else:
            flash("Ha ocurrido un error!")
        return render_template('administradores/vehiculos/crear.html')
    else:
        return render_template('administradores/vehiculos/crear.html')


@app.route('/vehiculos/eliminar_vehiculo/<int:id>', methods=['GET'])
@login_required
def eliminar_vehiculo(id):
    vehiculo_eliminado = ModelVehiculo.eliminar_vehiculo(db, id)
    flash("vehiculo eliminado con ??xito")
    vehiculos = ModelVehiculo.get_vehiculos_activos(db)
    return render_template('administradores/vehiculos/index.html', vehiculos=vehiculos)


@app.route('/vehiculos/editar_vehiculo/<int:id>', methods=['GET'])
@login_required
def editar_vehiculo(id):
    vehiculo = ModelVehiculo.get_vehiculo_id(db, id)
    return render_template('administradores/vehiculos/editar.html', vehiculo=vehiculo)

@app.route('/vehiculos/guardar_vehiculo/', methods=['POST'])
@login_required
def guardar_vehiculo():
    estado = request.form['estado']
    placa = request.form['placa']
    imagen = request.files['imagen']
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    nuevoNombreFoto = ''
    if imagen.filename!='':
        nuevoNombreFoto = tiempo + imagen.filename
        imagen.save("uploads/" + nuevoNombreFoto)
    vehiculo = Vehiculo(0, estado, placa, 1, nuevoNombreFoto)
    ModelVehiculo.crear_vehiculo(db, vehiculo)

    vehiculo = vehiculo(id, estado, placa, nuevoNombreFoto)
    vehiculo = ModelVehiculo.editar_vehiculo(db,vehiculo)
    vehiculos = ModelVehiculo.get_vehiculos_activos(db)
    return render_template('administradores/vehiculos/index.html', vehiculos=vehiculos)

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
    coords = ((-71.5279236901535,-16.41041958501789),(-71.5070003854512,-16.4018162742952))
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


@app.route('/rutas/generar_ruta')
@login_required
def generar_ruta():
    entregas = ModelEntrega.get_entregas_activas(db)

    client = openrouteservice.Client(key='5b3ce3597851110001cf62488b5f9fc52aec4396a6e94f225de93894')
    
    matriz_distancias.clear()
    array_pedidos.clear()

    m = folium.Map(location=[-16.41041958501,-71.5279236901],zoom_start=13, control_scale=True,tiles="cartodbpositron")#crear el mapa

    # Lista de entregas
    coordenadas =[]
    for entrega in entregas:
        coordenadas.append([float(entrega[2]),float(entrega[3]) ])
        array_pedidos.append(entrega[1])

        coordenada = (entrega[3],entrega[2])
        folium.Marker(
            location=list(coordenada),
            popup= entrega[4],
            icon=folium.Icon(color="red"),
        ).add_to(m)

    almacen = (-16.41041958501,-71.5279236901)
    folium.Marker(
        location=list(almacen),
        popup="Qaliwarma",
        icon=folium.Icon(color="green"),
    ).add_to(m)


    # matriz de distancias
    # documentacion: https://openrouteservice-py.readthedocs.io/en/latest/openrouteservice.html#module-openrouteservice.distance_matrix
    matrix = client.distance_matrix(
    locations=coordenadas,
    profile='driving-car',
    metrics=['distance'],
    # units=['meters'],
    validate=False,
    )   

    matriz_distancia = matrix['distances']
    matriz_distancia_redondeada = numpy.round(matriz_distancia)
    print(matriz_distancia_redondeada)

    #### Algoritmos geneticos ####
    data = dict()
    data['distance_matrix'] = matriz_distancia_redondeada
    data['num_vehicles'] = 4
    data['depot'] = 0
    data['demands'] = array_pedidos
    data['vehicle_capacity'] = 1400  
    data['service_times'] = np.zeros(len(data['demands']))

    
    ap = hgs.AlgorithmParameters(timeLimit=3)  # seconds
    hgs_solver = hgs.Solver(parameters=ap, verbose=True)

    
    result = hgs_solver.solve_cvrp(data)
    print("solucion:")
    print(result.cost)
    print(result.routes)


    ########### MOSTRAR LA SOLUCION POR EL MAPA #############
    solucion = result.routes

    array_rutas = []
    fila_ruta = []
    for instancia in solucion:
        fila_ruta.clear()
        fila_ruta.append([entregas[0][2] ,entregas[0][3]])
        for cliente in instancia:
            fila_ruta.append([entregas[cliente][2], entregas[cliente][3]])
        fila_ruta.append([entregas[0][2] ,entregas[0][3]])
        array_rutas.append(fila_ruta.copy())

    # print(array_rutas)

    ##COLORS##
    style1 = {'fillColor': '#d4271e', 'color': '#d4271e'}
    style2 = {'fillColor': '#d47c1e', 'color': '#d47c1e'}
    colores = [
        {'fillColor': '#d4271e', 'color': '#d4271e'},
        {'fillColor': '#d47c1e', 'color': '#d47c1e'},
        {'fillColor': '#d4cb1e', 'color': '#d4cb1e'},
        {'fillColor': '#97d41e', 'color': '#97d41e'},
        {'fillColor': '#64d41e', 'color': '#64d41e'},
        {'fillColor': '#30d41e', 'color': '#30d41e'},
        {'fillColor': '#1ed442', 'color': '#1ed442'},
        {'fillColor': '#1ed47f', 'color': '#1ed47f'},
        {'fillColor': '#1ed4c2', 'color': '#1ed4c2'},
        {'fillColor': '#1e91d4', 'color': '#1e91d4'},
        {'fillColor': '#1e61d4', 'color': '#1e61d4'},
        {'fillColor': '#1e24d4', 'color': '#1e24d4'},
        {'fillColor': '#451ed4', 'color': '#451ed4'},
        {'fillColor': '#7c1ed4', 'color': '#7c1ed4'},
        {'fillColor': '#a71ed4', 'color': '#a71ed4'},
        {'fillColor': '#d41e5b', 'color': '#d41e5b'},
    ]

    
    roads_highlight_function = lambda x: {
    'color' :   'black',
    'opacity' : 0.90,
    # specifying properties from GeoJSON
    'weight' : 5
    }

    color_index = 0

    if (array_rutas != 0):
        for ruta in array_rutas:
            i = 0
            color_index = color_index + 1
            
            for coordenadas in ruta:
                if (i >= 1):
                    style_function = lambda x: {
                    'color' : 'red',
                    'opacity' : 0.50,
                    }
                    coords = (( float(ruta[i-1][0]), float(ruta[i-1][1])),( float(ruta[i][0]), float(ruta[i][1])))
                    res = client.directions(coords)
                    geometry = client.directions(coords)['routes'][0]['geometry']
                    decoded = convert.decode_polyline(geometry)

                    distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
                    duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"
                    color = getcolor(color_index)
                    folium.GeoJson(decoded, style_function = lambda color_index: {
                    'fillColor': getcolor(color_index),
                    'color': color,
                    'weight': 2,
                    'fillOpacity': 0.8}, highlight_function = roads_highlight_function).add_child(folium.Popup(distance_txt+duration_txt,max_width=300)).add_to(m)
                    
                    # print(ruta[i-1]+ruta[i])
                    # print(coordenadas[0],coordenadas[1])
                i = i + 1

    m.save('src/templates/map.html')


    return render_template('administradores/rutas/index.html', entregas=entregas)


@app.route('/rutas/mapa')
@login_required
def mapa():
    return render_template('map.html')

############################ FUNCIONES ######################



def getcolor(index):
    if index == 1:
        return 'red'
    if index == 2:
        return 'orange'
    if index == 3:
        return 'blue'
    if index == 4:
        return 'gold'
    if index == 5:
        return 'purple'
    if index == 6:
        return 'yellow'
    if index == 7:
        return 'greenyellow'
    if index == 8:
        return 'lime'
    if index == 9:
        return 'black'
    if index == 10:
        return 'green'
    else:
        return 'gray'

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
