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
                    "nombre": "Sarah",
                    "apellido": "Johnson",
                    "telefono": "9876543210",
                    "correo": "sarah.johnson@example.com",
                    "contrasena": "pass1234"
                },
                {
                    "rol": "administrador",
                    "nombre": "Michael",
                    "apellido": "Anderson",
                    "telefono": "1234567890",
                    "correo": "michael.anderson@example.com",
                    "contrasena": "admin456"
                },
                {
                    "rol": "cliente",
                    "nombre": "Emily",
                    "apellido": "Davis",
                    "telefono": "5555555555",
                    "correo": "emily.davis@example.com",
                    "contrasena": "password123"
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
                    "titulo": "Avengers: Age of Ultron",
                    "director": "Joss Whedon",
                    "anio": "2015",
                    "fecha": "2023-06-05",
                    "hora": "18:30",
                    "imagen": "https://m.media-amazon.com/images/M/MV5BMTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_.jpg",
                    "precio": "42"
                },
                {
                    "categoria": "Acción",
                    "titulo": "Mad Max: Fury Road",
                    "director": "George Miller",
                    "anio": "2015",
                    "fecha": "2023-06-06",
                    "hora": "20:00",
                    "imagen": "https://m.media-amazon.com/images/M/MV5BN2EwM2I5OWMtMGQyMi00Zjg1LWJkNTctZTdjYTA4OGUwZjMyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_FMjpg_UX1000_.jpg",
                    "precio": "45"
                },
                {
                    "categoria": "Acción",
                    "titulo": "Mission: Impossible - Rogue Nation",
                    "director": "Christopher McQuarrie",
                    "anio": "2015",
                    "fecha": "2023-06-07",
                    "hora": "19:15",
                    "imagen": "https://m.media-amazon.com/images/M/MV5BOTFmNDA3ZjMtN2Y0MC00NDYyLWFlY2UtNTQ4OTQxMmY1NmVjXkEyXkFqcGdeQXVyNTg4NDQ4NDY@._V1_FMjpg_UX1000_.jpg",
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
                    "numero": "#USACIPC2_202111849_4",
                    "asientos": "50"
                },
                {
                    "numero": "#USACIPC2_202111849_5",
                    "asientos": "20"
                },
                {
                    "numero": "#USACIPC2_202111849_6",
                    "asientos": "70"
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