from flask import Flask, jsonify, request
from datetime import datetime
app = Flask(__name__)


@app.route('/suludo/superman', methods=['GET'])
def superman():
    now = datetime.now()
    horaActual = now.strftime('%H:%M:%S')
    respuesta = str("Hola soy Superman mucho gusto {}").format(horaActual)
    return jsonify({"Respuesta" : respuesta})


@app.route('/suludo/batman', methods=['GET'])
def batman():
    now = datetime.now()
    horaActual = now.strftime('%H:%M:%S')
    respuesta = str("Hola soy Batman mucho gusto {}").format(horaActual)
    return jsonify({"Respuesta" : respuesta})    

@app.route('/poderes' , methods=['POST'])
def poderes():
    content = request.get_json()
    restaGenera = []
    for i in content:
        if i["super heroe"]["nombre"] == 'superman':
            restaGenera.append({ "super Heroe": i["super heroe"]["nombre"]})
            respuesta= []
            respuesta.append({ "poder" : "supuer fuerza" })
            respuesta.append({ "debilidad" : "criptonita" })
            restaGenera.append(respuesta)
        if i["super heroe"]["nombre"] == 'batman':
            restaGenera.append({ "super Heroe": i["super heroe"]["nombre"]})
            respuesta= []
            respuesta.append({ "poder" : "dinero" })
            respuesta.append({ "debilidad" : "ninguna" })
            restaGenera.append(respuesta)
    return jsonify(restaGenera)

def main():
    app.run(host="0.0.0.0", port="4000", debug=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Seliendo")
        exit()