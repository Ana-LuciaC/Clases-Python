from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/saludo/batman', methods=['GET'])
def saludoBatman():
    return jsonify({"Respuesta" : "Hola Soy BATMAN"})

@app.route('/saludo/superman', methods=['GET'])
def saludoSuperman():
    return jsonify({"Respuesta" : "Hola Soy SUPERMAN"})

@app.route('/atributos', methods=['POST'])
def atributos ():
    content = request.get_json()
    restaGeneral = []
    for i in content:
        if i["super heroe"]["nombre"] == 'superman':
            restaGeneral.append({'nombre': i['super heroe'] ['nombre']
                                , 'atributos': {
                                     "poder": "Super Fuerza",
                                     "debilidad": "Criptonita"
                                 }})

        if i["super heroe"]["nombre"] == 'batman':
           restaGeneral.append({'nombre': i['super heroe'] ['nombre']
                                , 'atributos': {
                                     "poder": "dinero",
                                     "debilidad": "ninguna"
                                 }})
        if i["super heroe"]["nombre"] == 'capitan america':
           restaGeneral.append({'nombre': i['super heroe'] ['nombre']
                                , 'atributos': {
                                     "poder": "super fuerza",
                                     "debilidad": "hydra"
                                 }})
                                 
    return jsonify(restaGeneral)

def main():
    app.run(host="0.0.0.0", port="4000", debug=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()