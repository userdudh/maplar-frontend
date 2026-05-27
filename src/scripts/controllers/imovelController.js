const urlParams = new URLSearchParams(window.location.search);
const idParaEditar = urlParams.get('edit');

async function carregarEdicao() {
    if (idParaEditar) {
        const imovel = await imovelService.buscarPorId(idParaEditar);
        if (imovel && !imovel.erro) { 
            document.querySelector('.titulo-pagina').textContent = "Editar meu imóvel";
            document.querySelector('button[type="submit"]').textContent = "Salvar Alterações";
            
            document.getElementById('titulo').value = imovel.titulo;
            document.getElementById('valor').value = imovel.valor;
            document.getElementById('descricao').value = imovel.descricao;
            document.getElementById('quarto').value = imovel.quarto;
            document.getElementById('banheiro').value = imovel.banheiro;
            
            if (imovel.tipo) {
                document.getElementById(imovel.tipo).checked = true;
            }
        }
    }
}

carregarEdicao();

async function capturarDados(event) {
    event.preventDefault();

    const dados = Object.fromEntries(new FormData(event.target));
    const novoImovel = new Imovel(
        idParaEditar || null,
        dados.titulo,
        dados.valor,
        dados.tipo,
        dados.imagem,
        dados.quarto,
        dados.banheiro,
        dados.descricao
    );                                 

    const sucesso = await imovelService.salvar(novoImovel);

    if (sucesso) {
        window.location.href = "./meus-anuncios.html";
    }
} 