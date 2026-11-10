"""
interface.py — TIME 1: PRINTS ESTÁTICOS (INTERFACE)

Responsabilidade: tudo o que aparece na tela. Menus, tabelas, recibo, mensagens.
NÃO lê teclado (isso é do Time 2) e NÃO altera dicionários.

Prefixo: exibir_
Depende de: calculos.py (formatar_moeda) e estoque.py (situacao_produto)
Usado por: coleta.py (T2, exibir_mensagem) e main.py (T6)

Regras do contrato:
- Toda função devolve None (só imprime).
- Toda função que mostra dinheiro usa formatar_moeda.
- Menus sempre têm a opção 0 (sair ou voltar).
"""

from calculos import formatar_moeda
from estoque import situacao_produto


def exibir_cabecalho():
    """Imprime o nome da loja e uma linha decorativa."""
    # TODO Time 1
    pass


def exibir_linha(tamanho=50):
    """Imprime uma linha de separação, ex.: '-' * tamanho."""
    # TODO Time 1
    pass


def exibir_menu_principal():
    """
    1 - Produtos
    2 - Clientes
    3 - Vendas
    4 - Compras (reposição)
    5 - Estoque
    6 - Relatórios
    0 - Sair
    """
    # TODO Time 1
    pass


def exibir_menu_produtos():
    """1 - Cadastrar | 2 - Listar | 3 - Atualizar | 4 - Remover | 0 - Voltar"""
    # TODO Time 1
    pass


def exibir_menu_clientes():
    """1 - Cadastrar | 2 - Listar | 3 - Atualizar | 4 - Remover | 0 - Voltar"""
    # TODO Time 1
    pass


def exibir_menu_vendas():
    """1 - Nova venda | 2 - Listar vendas | 0 - Voltar"""
    # TODO Time 1
    pass


def exibir_menu_compras():
    """1 - Nova compra (reposição) | 2 - Listar compras | 0 - Voltar"""
    # TODO Time 1
    pass


def exibir_menu_estoque():
    """1 - Relatório de estoque | 2 - Produtos em falta | 0 - Voltar"""
    # TODO Time 1
    pass


def exibir_menu_relatorios():
    """1 - Resumo financeiro | 2 - Valor do estoque | 0 - Voltar"""
    # TODO Time 1
    pass


def exibir_tabela_produtos(produtos):
    """
    Tabela alinhada com: código, nome, tamanho, cor, preço de venda, quantidade, situação.
    Dica: f"{texto:<20}" alinha à esquerda em 20 colunas; f"{numero:>8}" alinha à direita.
    Se o dicionário estiver vazio, imprime "Nenhum produto cadastrado."
    """
    # TODO Time 1
    pass


def exibir_tabela_clientes(clientes):
    """Tabela com: código, nome, telefone, cidade."""
    # TODO Time 1
    pass


def exibir_produto(codigo, produto):
    """Ficha completa de UM produto, um campo por linha (inclui custo e margem)."""
    # TODO Time 1
    pass


def exibir_recibo(venda, produtos, clientes):
    """
    Recibo da venda:
    - nome do cliente (buscar em clientes[venda["cliente"]])
    - uma linha por item: nome do produto, quantidade, preço unitário, subtotal
    - desconto (%), total final, forma de pagamento
    """
    # TODO Time 1
    pass


def exibir_relatorio_estoque(relatorio):
    """
    Recebe o dicionário de relatorio_estoque (Time 5) e imprime:
    total de produtos, total de peças, lista de produtos em falta e esgotados.
    """
    # TODO Time 1
    pass


def exibir_resumo_financeiro(resumo):
    """Recebe o dicionário de resumo_financeiro (Time 4) e imprime formatado."""
    # TODO Time 1
    pass


def exibir_mensagem(texto, tipo="info"):
    """
    Imprime uma mensagem com prefixo conforme o tipo:
    "ok" -> [OK]  | "erro" -> [ERRO] | "aviso" -> [AVISO] | "info" -> [INFO]
    """
    # TODO Time 1
    pass


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python interface.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()

    exibir_cabecalho()
    exibir_menu_principal()
    exibir_tabela_produtos(sistema["produtos"])
    exibir_tabela_clientes(sistema["clientes"])
    exibir_mensagem("Produto cadastrado com sucesso", "ok")
    exibir_mensagem("Código não encontrado", "erro")

    venda_exemplo = {"cliente": 1, "itens": {1: 2, 2: 1}, "desconto": 10.0,
                     "total": 197.91, "forma_pagamento": "pix"}
    exibir_recibo(venda_exemplo, sistema["produtos"], sistema["clientes"])
