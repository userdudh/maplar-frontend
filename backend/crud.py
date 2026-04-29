from flask import Blueprint, request, jsonify

imoveis_bp = Blueprint("imoveis", __name__)

imoveis = []

@imoveis_bp.route("/imoveis", methods=["GET"])
def listar():
    return jsonify(imoveis)

@imoveis_bp.route("/imoveis/<string:id>", methods=["GET"])
def buscar_por_id(id):
    for imovel in imoveis:
        if imovel["id"] == id:
            return jsonify(imovel)
    return jsonify({"erro": "Não encontrado"}), 404

@imoveis_bp.route("/imoveis", methods=["POST"])
def criar():
    data = request.get_json()

    print("CHEGOU NO BACK:", data)

    if not data:
        return jsonify({"erro": "Sem dados"}), 400

    imoveis.append(data)
    return jsonify({"msg": "Criado com sucesso"}), 201


@imoveis_bp.route("/imoveis/<string:id>", methods=["PUT"])
def atualizar(id):
    data = request.json

    for i, imovel in enumerate(imoveis):
        if imovel["id"] == id:
            imoveis[i] = data
            return jsonify({"msg": "Atualizado"})
    
    return jsonify({"erro": "Não encontrado"}), 404

@imoveis_bp.route("/imoveis/<string:id>", methods=["DELETE"])
def deletar(id):
    global imoveis
    imoveis = [i for i in imoveis if i["id"] != id]
    return jsonify({"msg": "Removido"})
