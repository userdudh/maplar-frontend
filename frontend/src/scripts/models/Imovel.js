class Imovel {
    constructor(id, titulo, preco, tipo, imagem, quarto, banheiro, descricao) {
        this.id = id;
        this.titulo = titulo;
        this.preco = Number(preco);
        this.tipo = tipo;
        this.imagem = imagem;
        this.descricao = descricao;
        this.quarto = Number(quarto);
        this.banheiro = Number(banheiro);
    }
}