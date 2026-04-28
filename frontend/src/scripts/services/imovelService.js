const imovelService = {
    buscarPorId(id) {
        return imovelRepository.buscarPorId(id);
    },
    buscarParaListagem() {
        const imoveis = imovelRepository.buscarTodos();
        return imoveis.reverse();
    },
    excluir(id) {
        imovelRepository.removerPorId(id);
    },
    salvar(imovel) {
        if (!imovel.titulo || imovel.titulo.trim() === "") {
            alert("O título é obrigatório.");
            return false;
        }

        if (isNaN(imovel.preco) || imovel.preco <= 0) {
            alert("O preço deve ser superior a zero.");
            return false;
        }
        if (!imovel.tipo) {
            alert("Selecione se o anúncio é para Aluguel ou Venda.");
            return false;
        }
        if (imovel.id && this.buscarPorId(imovel.id)) {
            imovelRepository.atualizar(imovel);
        } else {
            imovelRepository.adicionar(imovel);
        }

        return true;
    }
};