"""
cadastro.py — TIME 3: CADASTRO DE DADOS

Responsabilidade: guardar e localizar registros nos dicionários.
É o módulo BASE: não importa nenhum outro time.

Prefixos: cadastrar_, registrar_, buscar_
Depende de: ninguém
Usado por: calculos.py (T4), estoque.py (T5), main.py / atualizacao.py (T6)

Regras do contrato:
- Códigos são inteiros gerados por gerar_codigo (maior chave + 1, começando em 1).
- Funções cadastrar_/registrar_ devolvem o código gerado.
- Funções buscar_ devolvem o dicionário encontrado ou None.
"""


def gerar_codigo(dicionario):
    """Devolve o próximo código livre: maior chave + 1, ou 1 se o dicionário estiver vazio."""
    # TODO Time 3
    pass


def existe(dicionario, codigo):
    """Devolve True se o código é uma chave do dicionário."""
    # TODO Time 3
    pass


def cadastrar_produto(produtos, dados):
    """
    Gera um código e grava produtos[codigo] = dados.
    'dados' já vem pronto de coletar_dados_produto() (sem código).
    Devolve o código gerado.
    """
    # TODO Time 3
    pass


def cadastrar_cliente(clientes, dados):
    """Gera um código e grava clientes[codigo] = dados. Devolve o código gerado."""
    # TODO Time 3
    pass


def registrar_venda(vendas, venda):
    """
    Grava a venda montada pelo Time 6.
    venda = {"cliente": int, "itens": {codigo: qtd}, "desconto": float,
             "total": float, "forma_pagamento": str}
    Devolve o código gerado.
    """
    # TODO Time 3
    pass


def registrar_compra(compras, compra):
    """
    Grava a compra montada pelo Time 6.
    compra = {"fornecedor": str, "itens": {codigo: qtd}, "total": float}
    Devolve o código gerado.
    """
    # TODO Time 3
    pass


def buscar_produto(produtos, codigo):
    """Devolve o dicionário do produto ou None se o código não existir. (Função mais usada do sistema!)"""
    # TODO Time 3
    pass


def buscar_cliente(clientes, codigo):
    """Devolve o dicionário do cliente ou None se o código não existir."""
    # TODO Time 3
    pass


def buscar_produto_por_nome(produtos, trecho):
    """
    Devolve um subdicionário {codigo: produto} com os produtos cujo nome contém o trecho,
    sem diferenciar maiúsculas de minúsculas. Devolve {} se nada for encontrado.
    """
    # TODO Time 3
    pass


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python cadastro.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()
    produtos = sistema["produtos"]

    print("gerar_codigo ->", gerar_codigo(produtos), "(esperado: 3)")
    print("buscar_produto(1) ->", buscar_produto(produtos, 1))
    print("buscar_produto(99) ->", buscar_produto(produtos, 99), "(esperado: None)")

    novo = {
        "nome": "Vestido floral", "categoria": "Vestido", "tamanho": "P", "cor": "Rosa",
        "preco_custo": 50.0, "preco_venda": 120.0, "quantidade": 3,
    }
    codigo = cadastrar_produto(produtos, novo)
    print("cadastrar_produto ->", codigo, "(esperado: 3)")
    print("buscar_produto_por_nome('vest') ->", buscar_produto_por_nome(produtos, "vest"))
