from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def getUsuarios():
    try:
        if request.method == 'GET':
            retorno = [
                {
                    "rol": "cliente",
                    "nombre": "John",
                    "apellido": "Doe",
                    "telefono": "123456789",
                    "correo": "john.doe@example.com",
                    "contrasena": "mipassword123"
                },
                {
                    "rol": "administrador",
                    "nombre": "Jane",
                    "apellido": "Smith",
                    "telefono": "987654321",
                    "correo": "jane.smith@example.com",
                    "contrasena": "password456"
                },
                {
                    "rol": "cliente",
                    "nombre": "Chabelo",
                    "apellido": "Perez",
                    "telefono": "838383",
                    "correo": "chabelo@gmail.com",
                    "contrasena": "838938"
                }
            ]
        else:
            retorno = {'Mensaje': 'Error, método incorrecto'}
            return jsonify(retorno)
    except:
        retorno = {'Mensaje': 'Error, no se pudo obtener los usuarios'}
        return jsonify(retorno)
    
@app.route('/peliculas', methods=['GET'])
def getPeliculas():
    try:
        if request.method == 'GET':
            retorno = [
                {
                    "categoria": "Acción",
                    "titulo": "Avengers: Endgame",
                    "director": "Joe Russo, Anthony Russo",
                    "anio": "2019",
                    "fecha": "2023-06-05",
                    "hora": "18:30",
                    "imagen": "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg",
                    "precio": "42"
                },
                {
                    "categoria": "Acción",
                    "titulo": "John Wick",
                    "director": "Chad Stahelski",
                    "anio": "2014",
                    "fecha": "2023-06-06",
                    "hora": "20:00",
                    "imagen": "https://m.media-amazon.com/images/I/71+k2-r7vQL._AC_UF1000,1000_QL80_.jpg",
                    "precio": "45"
                },
                {
                    "categoria": "Acción",
                    "titulo": "Misión Imposible: Fallout",
                    "director": "Christopher McQuarrie",
                    "anio": "2018",
                    "fecha": "2023-06-07",
                    "hora": "19:15",
                    "imagen": "https://pics.filmaffinity.com/Misiaon_imposible_Fallout-180739766-mmed.jpg",
                    "precio": "55"
                }
            ]
        else:
            retorno = {'Mensaje': 'Error, método incorrecto'}
            return jsonify(retorno)
    except:
        retorno = {'Mensaje': 'Error, no se pudo obtener las películas'}
        return jsonify(retorno)

@app.route('/salas', methods=['GET'])
def getSalas():
    try:
        if request.method == 'GET':
            retorno = [
                {
                    "numero": "#USACIPC2_202111849_1",
                    "asientos": "100"
                },
                {
                    "numero": "#USACIPC2_202111849_2",
                    "asientos": "80"
                },
                {
                    "numero": "#USACIPC2_202111849_3",
                    "asientos": "120"
                }
            ]
        else:
            retorno = {'Mensaje': 'Error, método incorrecto'}
            return jsonify(retorno)
    except:
        retorno = {'Mensaje': 'Error, no se pudo obtener las salas'}
        return jsonify(retorno)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5022)