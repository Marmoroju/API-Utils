from flask import Blueprint, jsonify, request

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", method=["GET"])
def listar_usuarios():
    return jsonify({"usuarios": ["Marcos", "Martha"]})

@usuarios_bp.route("/usuarios", method=["POST"])
def criar_usuario():
    data = request.json
    return jsonify({"status": "usuario criado", "dados": data})    


