from flask import Blueprint, request, jsonify

from bd import session as db_session, Imovel

imoveis_bp = Blueprint("imoveis", __name__)

@imoveis_bp.route("/imoveis", methods=["GET"])
def listar():
    imoveis_db = db_session.query(Imovel).all()
    
    resultado = []
    for imovel in imoveis_db:
        resultado.append({
            "id": imovel.id,
            "titulo": imovel.titulo,
            "preco": imovel.valor, 
            "tipo": imovel.tipo,
            "quarto": imovel.quarto,
            "banheiro": imovel.banheiro,
            "descricao": imovel.descricao
        })
        
    return jsonify(resultado)

@imoveis_bp.route("/imoveis/<int:id>", methods=["GET"])
def buscar_por_id(id):
    imovel = db_session.query(Imovel).get(id)
    
    if imovel:
        return jsonify({
            "id": imovel.id,
            "titulo": imovel.titulo,
            "preco": imovel.valor,
            "tipo": imovel.tipo,
            "quarto": imovel.quarto,
            "banheiro": imovel.banheiro,
            "descricao": imovel.descricao
        })
        
    return jsonify({"erro": "Não encontrado"}), 404

@imoveis_bp.route("/imoveis", methods=["POST"])
def criar():
    data = request.get_json()

    if not data:
        return jsonify({"erro": "Sem dados"}), 400

    imagem_recebida = data.get('imagem', '')
    if isinstance(imagem_recebida, dict) or not imagem_recebida:
        imagem_recebida = ""
    else:
        imagem_recebida = str(imagem_recebida)

    novo_imovel = Imovel(
        titulo=data.get('titulo'),
        valor=data.get('preco'),
        tipo=data.get('tipo'),
        imagem=imagem_recebida,
        quarto=data.get('quarto'),
        banheiro=data.get('banheiro'),
        descricao=data.get('descricao')
    )
    
    try:
        db_session.add(novo_imovel)
        db_session.commit()
        return jsonify({"msg": "Criado com sucesso", "id": novo_imovel.id}), 201
    except Exception as erro:
        db_session.rollback()
        print(f"Erro ao salvar no banco: {erro}")
        return jsonify({"erro": "Falha ao salvar no banco de dados."}), 500

@imoveis_bp.route("/imoveis/<int:id>", methods=["PUT"])
def atualizar(id):
    data = request.json
    imovel = db_session.query(Imovel).get(id)

    if not imovel:
        return jsonify({"erro": "Não encontrado"}), 404
        
    if 'titulo' in data:
        imovel.titulo = data['titulo']
    if 'preco' in data:
        imovel.valor = data['preco']
    if 'tipo' in data:
        imovel.tipo = data['tipo']
    if 'quarto' in data:
        imovel.quarto = data['quarto']
    if 'banheiro' in data:
        imovel.banheiro = data['banheiro']
    if 'descricao' in data:
        imovel.descricao = data['descricao']
        
    db_session.commit()
    return jsonify({"msg": "Atualizado"})

@imoveis_bp.route("/imoveis/<int:id>", methods=["DELETE"])
def deletar(id):
    imovel = db_session.query(Imovel).get(id)
    
    if not imovel:
         return jsonify({"erro": "Não encontrado"}), 404
         
    db_session.delete(imovel)
    db_session.commit()
    
    return jsonify({"msg": "Removido com sucesso"})