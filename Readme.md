# OptiRute

¡Hola! 

OptiRute es un CRUD optimizador de rutas utilizando algoritmos genéticos, para el desarrollo de este proyecto académico se utilizó:

- MySQL
- PyHygese (Solucionador para el problema de enrutamiento de vehículos capacitados )
- MapBox
- Folium 

> El aspecto visual (frontend) fue extraido de https://www.creative-tim.com/product/material-dashboard

# Imágenes del proyecto
![Añadir una entregas](https://github.com/AyrtonAranibar/OptiRute/blob/master/src/project/entregas_v2.PNG)
![Ruta optimizada](https://github.com/AyrtonAranibar/OptiRute/blob/master/src/project/rutas_v2.PNG)

# URL

Proyecto en desarrollo :hammer:

# Autor

- [@AyrtonAranibar](https://www.github.com/AyrtonAranibar)
- [Linkedin](https://www.linkedin.com/in/ayrton-aranibar-castillo-479441222/)

# Dependencias

Python 3
La instalación requiere gcc, makey cmakepara construir. En Windows, por ejemplo, puedes instalarlos scoop install gcc make cmakeusando Scoop.

# Instalación

En el terminal:

```cmd
git clone git@github.com:AyrtonAranibar/OptiRute.git
cd optirute
# Activa un entorno virtual
python -m venv venv
\venv\Scripts\activate
# Instala los requisitos
pip install -r requirements.txt
```
> terminado el trabajo activa el entorno por defecto

Set-ExecutionPolicy -Scope CurrentUser -Default

# Base de datos

Dentro de la carpeta raiz hay un archivo llamado "database", dentro esta la sentencia SQL para generar la base de datos.

# Ejecucion del proyecto

```cmd
cd src
python app.py
```

# Agradecimientos

Agradezco a Creative Tim por permitirme usar sus plantillas frontend para el desarrollo de este proyecto.

- **[Recursos Externos](https://www.creative-tim.com/product/material-dashboard):**

# Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE.md](LICENSE.md) para obtener más detalles.