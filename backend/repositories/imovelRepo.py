import logging
from bd import session as db_session, Imovel

def _serializar_imovel(imovel):
    return {
        "id": imovel.id,
        "titulo": imovel.titulo,
        "preco": imovel.valor, 
        "tipo": imovel.tipo,
        "quarto": imovel.quarto,
        "banheiro": imovel.banheiro,
        "descricao": imovel.descricao
    }

def listar_imovel():
    try:
        imoveis_db = db_session.query(Imovel).all()
        resultado = [_serializar_imovel(imovel) for imovel in imoveis_db]
        return resultado, 200
    except Exception as erro:
        logging.error(f"Erro ao listar imóveis: {erro}")
        return {"erro": "Falha interna no servidor"}, 500

def buscar_por_id_imovel(id):
    imovel = db_session.get(Imovel, id)
    
    if imovel:
        return _serializar_imovel(imovel), 200
        
    return {"erro": "Imóvel não encontrado"}, 404

def criar_imovel(data):
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
        return {"msg": "Criado com sucesso", "id": novo_imovel.id}, 201
    except Exception as erro:
        db_session.rollback()
        logging.error(f"Erro ao salvar no banco: {erro}")
        return {"erro": "Falha ao salvar no banco de dados."}, 500
        
def atualizar_imovel(id, data):
    imovel = db_session.get(Imovel, id)

    if not imovel:
        return {"erro": "Imóvel não encontrado"}, 404
        
    try:
        if 'titulo' in data: imovel.titulo = data['titulo']
        if 'preco' in data: imovel.valor = data['preco']
        if 'tipo' in data: imovel.tipo = data['tipo']
        if 'quarto' in data: imovel.quarto = data['quarto']
        if 'banheiro' in data: imovel.banheiro = data['banheiro']
        if 'descricao' in data: imovel.descricao = data['descricao']
            
        db_session.commit()
        return {"msg": "Atualizado com sucesso"}, 200
    except Exception as erro:
        db_session.rollback()
        logging.error(f"Erro ao atualizar no banco: {erro}")
        return {"erro": "Falha ao atualizar no banco de dados."}, 500

def deletar_imovel(id):
    imovel = db_session.get(Imovel, id)
    
    if not imovel:
         return {"erro": "Imóvel não encontrado"}, 404
         
    try:
        db_session.delete(imovel)
        db_session.commit()
        return {"msg": "Removido com sucesso"}, 200
    except Exception as erro:
        db_session.rollback()
        logging.error(f"Erro ao deletar no banco: {erro}")
        return {"erro": "Falha ao remover do banco de dados."}, 500