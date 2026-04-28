const IMOVEL = "imoveis";

const imovelRepository = {
    buscarTodos() {
        return JSON.parse(localStorage.getItem(IMOVEL)) || [];
    },

    salvarTodos(imoveis) {
        localStorage.setItem(IMOVEL, JSON.stringify(imoveis));
    },

    buscarPorId(id) {
        return this.buscarTodos().find(imovel => imovel.id == id);
    },

    adicionar(novoImovel) {
        const imoveis = this.buscarTodos();
        imoveis.push(novoImovel);
        this.salvarTodos(imoveis);
    },

    atualizar(imovelAtualizado) {
        const imoveis = this.buscarTodos();
        const index = imoveis.findIndex(i => i.id == imovelAtualizado.id);
        
        if (index !== -1) {
            imoveis[index] = imovelAtualizado;
            this.salvarTodos(imoveis);
        }
    },

    removerPorId(id) {
        const imoveis = this.buscarTodos();
        const imoveisFiltrados = imoveis.filter(imovel => imovel.id != id);
        this.salvarTodos(imoveisFiltrados);
    }
};