
function ligaCliqueBtnAtualizarItem() {
    $('[id^=idBtnAtualizar]').on('click', function(e) {
        atualizarValorItemCarrinho(e);
    });
}

function atualizarValorItemCarrinho(e) {
    var idProdutoSelecionado = e.target.id.split('-')[1];
    var quantidade = $('#quantidade-'+idProdutoSelecionado).val();

    $.get('atualizar/'+idProdutoSelecionado+'/'+quantidade+'/', function(data) {
        $('#valorItem-'+idProdutoSelecionado).text(data['item_valor']);
        $('#valorTotal').text(data['total']);
    });
}