const container = document.getElementById("containerAnuncios");

function carregarAnuncios() {
    container.innerHTML = ""; 
    
    const listaExibicao = imovelService.buscarParaListagem(); 

    if (listaExibicao.length === 0) {
        container.innerHTML = "<p>Nenhum anúncio encontrado.</p>";
        return;
    }

    listaExibicao.forEach((imovel) => {
        const card = document.createElement("div");
        card.className = "card-imovel";
        
        card.innerHTML = `
            <div class="info-imovel">
                <p><strong>${imovel.titulo}</strong> | ${imovel.tipo || 'Não definido'} | R$ ${imovel.preco},00 </p>
            </div>
            <div class="acoes">
                <button onclick="window.location.href='../pages/anunciar.html?edit=${imovel.id}'">Editar</button>
                <button onclick="deletarAnuncio('${imovel.id}')">Excluir</button>
            </div>
        `;
        container.appendChild(card);
    });
}

function deletarAnuncio(id) {
    const confirmar = confirm("Tem a certeza que deseja excluir este anúncio?");
    if (confirmar) {
        imovelService.excluir(id);
        carregarAnuncios();
    }
}

document.addEventListener("DOMContentLoaded", carregarAnuncios);