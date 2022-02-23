from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from config.config import config
from flask_mysqldb import MySQL

app = Flask(__name__)

conexion = MySQL(app)

def traer_estados():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM nombres_estados"
        cursor.execute(sql)
        datos = cursor.fetchall()
        estados = []
        for fila in datos:
            estado = {'id_estado': fila[0], 'nombre_estado': fila[1]}
            estados.append(estado)
        #return render_template('index.html', estados = estados)
        return estados
    except Exception as e:
        return jsonify({'mensaje': "Error", 'error': 404})
    
def traer_municipios(id):
    try:     
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM municipios_por_estado WHERE id_estado='{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchall()
        municipios = []
        for fila in datos:
            municipio = {'D_mnpio': fila[0], 'id_estado': fila[1]}
            municipios.append(municipio)
        return municipios
    except Exception as e:
        return jsonify({'mensaje': "Error", 'error': 404})
#Routes
@app.route('/')
def get_estados():
    estados = traer_estados()
    return render_template('index.html', estados = estados)

@app.route('/estado/<string:id>', methods=['GET'])
def get_estado(id):
    estados = traer_estados()
    municipios = traer_municipios(id)
    return render_template('index.html', estados = estados, municipios = municipios )

def error_404(error):
    return '<h1>Página no encontrada</h1>', 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, error_404)
    app.secret_key = 'misesion'
    app.run()

