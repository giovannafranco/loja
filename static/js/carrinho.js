function ligaCliqueBtnAtualizarItem() {
    $('[id^=idBtnAtualizar]').on('click', function(e) {
        atualizarValorItemCarrinho(e);
    });
}

//Função utilizada para atualizar o valor de um item do carrinho
function atualizarValorItemCarrinho(e) {
    var idProdutoSelecionado = e.target.id.split('-')[1];
    var quantidade = $('#quantidade-'+idProdutoSelecionado).val();

    if (quantidade < 1) { // se quantidade menor que 1 
         $('#blocoMensagem').empty();
        $('#blocoMensagem').append('<p class="alert alert-danger">Quantidade inválida, quantidade não pode ser '+ quantidade +'.</p>');
    } else { // senão 
        $.ajax({
            //url para atualizar quantidade
            url: 'atualizar/'+idProdutoSelecionado+'/'+quantidade+'/', 
            success:
                function(data) {
                    $('#valorItem-'+idProdutoSelecionado).text(data['item_valor']);
                    $('#valorTotal').text(data['total']);
                    $('#blocoMensagem').empty();
                    $('#blocoMensagem').append('<p class="alert alert-info">Produto atualizado com sucesso!</p>');
                },
            error: 
                function(textStatus, errorThrow) {
                    $('#blocoMensagem').empty();
                    $('#blocoMensagem').append('<p class="alert alert-danger">Quantidade indisponível.</p>');
                }
        });
    }
}
