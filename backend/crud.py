from flask import Blueprint, request, jsonify
from repositories import imovelRepo

imoveis_bp = Blueprint("imoveis", __name__)

@imoveis_bp.route("/imoveis", methods=["GET"])
def listar():
    resposta, status = imovelRepo.listar_imovel()
    return jsonify(resposta), status

@imoveis_bp.route("/imoveis/<int:id>", methods=["GET"])
def buscar(id):
    resposta, status = imovelRepo.buscar_por_id_imovel(id)
    return jsonify(resposta), status

@imoveis_bp.route("/imoveis", methods=["POST"])
def criar():
    data = request.get_json()
    if not data:
        return jsonify({"erro": "Sem dados enviados"}), 400
        
    resposta, status = imovelRepo.criar_imovel(data)
    return jsonify(resposta), status

@imoveis_bp.route("/imoveis/<int:id>", methods=["PUT"])
def atualizar(id):
    data = request.get_json()
    if not data:
        return jsonify({"erro": "Sem dados enviados"}), 400
        
    resposta, status = imovelRepo.atualizar_imovel(id, data)
    return jsonify(resposta), status

@imoveis_bp.route("/imoveis/<int:id>", methods=["DELETE"])
def deletar(id):
    resposta, status = imovelRepo.deletar_imovel(id)
    return jsonify(resposta), status