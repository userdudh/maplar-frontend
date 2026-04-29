const urlParams = new URLSearchParams(window.location.search);
const idParaEditar = urlParams.get('edit');

// 1. Envelopar o código de carregamento em uma função assíncrona
async function carregarEdicao() {
    if (idParaEditar) {
        // 2. Adicionar o await
        const imovel = await imovelService.buscarPorId(idParaEditar);
        
        // Verificar se os dados vieram corretamente (e não um erro da API)
        if (imovel && !imovel.erro) { 
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
} // 3. Fechar a função

// Chamar a função imediatamente
carregarEdicao();

async function capturarDados(event) {
    event.preventDefault();

    const dados = Object.fromEntries(new FormData(event.target));
    const novoImovel = new Imovel(
        idParaEditar || null,
        dados.titulo,
        dados.preco,
        dados.tipo,
        dados.imagem, // Nota: Input file não funciona direto com JSON.
        dados.quarto,
        dados.banheiro,
        dados.descricao
    );                                 

    const sucesso = await imovelService.salvar(novoImovel);

    if (sucesso) {
        window.location.href = "./meus-anuncios.html";
    }
} 