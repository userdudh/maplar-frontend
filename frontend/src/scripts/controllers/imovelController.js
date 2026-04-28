const urlParams = new URLSearchParams(window.location.search);
const idParaEditar = urlParams.get('edit');

if (idParaEditar) {
    const imovel = imovelService.buscarPorId(idParaEditar); 
    
    if (imovel) {
        document.querySelector('.titulo-pagina').textContent = "Editar meu imóvel";
        document.querySelector('button[type="submit"]').textContent = "Salvar Alterações";

        document.getElementById('titulo').value = imovel.titulo;
        document.getElementById('valor').value = imovel.preco;
        document.getElementById('descricao').value = imovel.descricao;
        document.getElementById('quarto').value = imovel.quarto;
        document.getElementById('banheiro').value = imovel.banheiro;
        if (imovel.tipo) {
            document.getElementById(imovel.tipo).checked = true;
        }
    }
}
function capturarDados(event) {
    event.preventDefault();

    const dados = Object.fromEntries(new FormData(event.target));
    const novoImovel = new Imovel(
        idParaEditar || null,
        dados.titulo,
        dados.preco,
        dados.tipo,
        dados.imagem,
        dados.quarto,
        dados.banheiro,
        dados.descricao
    );

    const sucesso = imovelService.salvar(novoImovel);

    if (sucesso) {
        window.location.href = "./meus-anuncios.html";
    }
}