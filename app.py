import os
from flask import Flask, jsonify, request

app = Flask(__name__)

servicios = []
usuarios = {"admin": {"contrasena": "1234", "rol": "administrador"}}

@app.route('/autenticar-usuario', methods=['POST'])
def autenticar():
    data = request.json
    nombre = data.get("nombre_usuario")
    contrasena = data.get(contrasena)
    if nombre in usuarios and usuarios[nombre]["contrasena"] == contrasena:
        return jsonify({"token": "token_valido", "rol": usuarios[nombre]["rol"]})
    return jsonify({"error": "credenciales invalidas"}), 401

@app.route('/autorizar-acceso', methods=['POST'])
def autorizar():
    data = request.json
    token = data.get("token")
    rol = data.get("rol")
    if token == "token_valido" and rol == "administrador":
        return jsonify({"autorizado": True})
    return jsonify({"autorizado": False}), 403

@app.route('/registrar-serrvicio', methods=['POST'])
def registrar_servicio():
    data = request.json
    servicios.append(data)
    return jsonify({"mensaje": "servicio registrado", "servicios": servicios})

@app.route('/actualizar-reglas-orquestacion', methods=['PUT'])
def actualizar_reglas():
    return jsonify({"mensaje": "reglas de orquestacion actualizadas"}), 200

@app.route('/informacion-servicio/<int:id>', methods=['GET'])
def obtener_servicio(id):
    if 0 <= id < len(servicios):
        return jsonify(servicios[id])
    return jsonify({"error": "servicio no encontrado"}), 404

@app.route('/orquestar', methods=['POST'])
def orquestar():
    data = request.json
    servicio = data.get("servicio_destino")
    parametros = data.get("parametros_adicionales")
    return jsonify({"mensaje": f"servicio {servicio} orquestado con parametros {parametros}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))