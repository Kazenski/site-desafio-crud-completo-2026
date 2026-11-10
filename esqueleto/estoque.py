"""
estoque.py — TIME 5: CONTROLE DE ESTOQUE

Responsabilidade: a quantidade de cada produto. Confere disponibilidade,
dá baixa na venda, repõe na compra e aponta produtos em falta.
É o ÚNICO módulo que altera produtos[codigo]["quantidade"].

Prefixos: verificar_, baixar_, repor_, situacao_, produtos_, relatorio_
Depende de: cadastro.py (buscar_produto)
Usado por: main.py (T6) e interface.py (T1, situacao_produto)

Regras do contrato:
- A quantidade NUNCA fica negativa.
- Operações devolvem True/False.
- "minimo" padrão é 3: com quantidade <= 3 o produto está "BAIXO".
"""

from cadastro import buscar_produto


def verificar_disponibilidade(produtos, codigo, quantidade):
    """Devolve True se o produto existe e tem quantidade em estoque >= quantidade pedida."""
    # TODO Time 5
    pass


def baixar_estoque(produtos, codigo, quantidade):
    """
    Subtrai 'quantidade' do estoque do produto.
    Devolve False (e NÃO altera nada) se o produto não existe ou se ficaria negativo.
    """
    # TODO Time 5
    pass


def repor_estoque(produtos, codigo, quantidade):
    """Soma 'quantidade' ao estoque do produto. Devolve False se o produto não existe."""
    # TODO Time 5
    pass


def baixar_estoque_itens(produtos, itens):
    """
    Aplica baixar_estoque a cada item de uma venda.
    itens = {codigo: quantidade}
    Devolve True se todos foram baixados.
    """
    # TODO Time 5
    pass


def repor_estoque_itens(produtos, itens):
    """Aplica repor_estoque a cada item de uma compra. Devolve True se todos foram repostos."""
    # TODO Time 5
    pass


def situacao_produto(produto, minimo=3):
    """
    Devolve o estado do produto no estoque:
    "ESGOTADO" se quantidade == 0
    "BAIXO"    se 0 < quantidade <= minimo
    "OK"       se quantidade > minimo
    """
    # TODO Time 5
    pass


def produtos_em_falta(produtos, minimo=3):
    """Devolve um subdicionário {codigo: produto} com os produtos em situação BAIXO."""
    # TODO Time 5
    pass


def produtos_esgotados(produtos):
    """Devolve um subdicionário {codigo: produto} com os produtos com quantidade 0."""
    # TODO Time 5
    pass


def relatorio_estoque(produtos, minimo=3):
    """
    Devolve um dicionário resumo:
    {
        "total_produtos": quantos produtos diferentes,
        "total_pecas": soma de todas as quantidades,
        "em_falta": produtos_em_falta(...),
        "esgotados": produtos_esgotados(...),
    }
    Quem imprime é exibir_relatorio_estoque (Time 1).
    """
    # TODO Time 5
    pass


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python estoque.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()
    produtos = sistema["produtos"]

    print("verificar_disponibilidade(1, 5) ->", verificar_disponibilidade(produtos, 1, 5), "(esperado: True)")
    print("verificar_disponibilidade(2, 5) ->", verificar_disponibilidade(produtos, 2, 5), "(esperado: False)")
    print("baixar_estoque(1, 8) ->", baixar_estoque(produtos, 1, 8), "| qtd agora:", produtos[1]["quantidade"], "(esperado: 2)")
    print("baixar_estoque(1, 5) ->", baixar_estoque(produtos, 1, 5), "(esperado: False, qtd continua 2)")
    print("situacao_produto(1) ->", situacao_produto(produtos[1]), "(esperado: BAIXO)")
    print("repor_estoque(1, 10) ->", repor_estoque(produtos, 1, 10), "| qtd agora:", produtos[1]["quantidade"], "(esperado: 12)")
    print("relatorio_estoque ->", relatorio_estoque(produtos))
