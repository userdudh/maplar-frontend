const API = "http://127.0.0.1:5000/api/imoveis";

const imovelService = {
    async buscarPorId(id) {
        const res = await fetch(`${API}/${id}`);
        return await res.json();
    },
    async buscarParaListagem() {
        const res = await fetch(API);
        const imoveis = await res.json();
        return imoveis.reverse();
    },

    async excluir(id) {
        await fetch(`${API}/${id}`, {
            method: "DELETE"
        });
    },

    async salvar(imovel) {
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
        if (imovel.id) {
            await fetch(`${API}/${imovel.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(imovel)
            });
        } else {            
            await fetch(API, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(imovel)
            });
        }

        return true;
    }
};