"""
atualizacao.py — TIME 6 (parte 1): ATUALIZAÇÕES

Responsabilidade: alterar e remover registros existentes e controlar o caixa.
A parte de integração (menus e fluxos) fica em main.py.

Prefixos: atualizar_, remover_
Depende de: cadastro.py (existe / buscar_)
Usado por: main.py (T6)

Regras do contrato:
- Operações devolvem True/False.
- 'quantidade' de produto NÃO se altera aqui — só por venda/compra (Time 5).
"""

from cadastro import existe

CAMPOS_PRODUTO_EDITAVEIS = ["nome", "categoria", "tamanho", "cor", "preco_custo", "preco_venda"]
CAMPOS_CLIENTE_EDITAVEIS = ["nome", "telefone", "cidade"]


def atualizar_produto(produtos, codigo, campo, novo_valor):
    """
    Altera produtos[codigo][campo] = novo_valor.
    Devolve False se o código não existe ou se o campo não está em CAMPOS_PRODUTO_EDITAVEIS.
    """
    # TODO Time 6
    pass


def atualizar_cliente(clientes, codigo, campo, novo_valor):
    """Altera clientes[codigo][campo]. Devolve False se código ou campo inválidos."""
    # TODO Time 6
    pass


def remover_produto(produtos, codigo):
    """Remove o produto (del produtos[codigo]). Devolve False se não existe."""
    # TODO Time 6
    pass


def remover_cliente(clientes, codigo):
    """Remove o cliente. Devolve False se não existe."""
    # TODO Time 6
    pass


def atualizar_caixa(sistema, valor):
    """
    Soma 'valor' em sistema["caixa"] (positivo na venda, negativo na compra).
    Devolve o novo saldo.
    """
    # TODO Time 6
    pass


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python atualizacao.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()
    produtos = sistema["produtos"]

    print("atualizar_produto(1, preco_venda, 49.9) ->", atualizar_produto(produtos, 1, "preco_venda", 49.9), "(esperado: True)")
    print("preço agora:", produtos[1]["preco_venda"])
    print("atualizar_produto(1, quantidade, 99) ->", atualizar_produto(produtos, 1, "quantidade", 99), "(esperado: False)")
    print("remover_produto(2) ->", remover_produto(produtos, 2), "(esperado: True)")
    print("remover_produto(2) de novo ->", remover_produto(produtos, 2), "(esperado: False)")
    print("atualizar_caixa(+189) ->", atualizar_caixa(sistema, 189.0), "(esperado: 189.0)")
    print("atualizar_caixa(-500) ->", atualizar_caixa(sistema, -500.0), "(esperado: -311.0)")
