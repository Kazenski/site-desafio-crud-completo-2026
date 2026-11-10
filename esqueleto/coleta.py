"""
coleta.py — TIME 2: COLETA DE DADOS

Responsabilidade: todos os input() do sistema, com validação.
Repete a pergunta até o usuário digitar algo válido e devolve o valor já convertido.
NÃO altera dicionários.

Prefixos: ler_, coletar_
Depende de: interface.py (exibir_mensagem para avisar erro de digitação)
Usado por: main.py (T6)

Regras do contrato:
- ler_* devolve um valor simples (str, int, float, bool).
- coletar_* devolve um dicionário pronto para o cadastro.
- Nunca deixa o programa quebrar por causa de digitação errada (use try/except ValueError).
"""

from interface import exibir_mensagem


def ler_texto(mensagem, obrigatorio=True):
    """Lê um texto. Se obrigatório, repete enquanto vier vazio. Devolve sem espaços nas pontas (.strip())."""
    # TODO Time 2
    pass


def ler_inteiro(mensagem, minimo=None):
    """
    Lê um inteiro. Repete até ser número válido e, se 'minimo' for informado, >= minimo.
    Em caso de erro chama exibir_mensagem("Digite um número inteiro válido", "erro").
    """
    # TODO Time 2
    pass


def ler_decimal(mensagem, minimo=0.0):
    """Lê um número decimal. Aceita vírgula ou ponto (troque ',' por '.'). Repete até válido e >= minimo."""
    # TODO Time 2
    pass


def ler_opcao(mensagem, opcoes_validas):
    """
    Lê uma opção de menu. Repete até a resposta estar em opcoes_validas.
    Ex.: ler_opcao("Opção: ", ["0", "1", "2", "3"]) -> "2"
    Devolve a opção como string.
    """
    # TODO Time 2
    pass


def confirmar(mensagem):
    """Pergunta 'mensagem (s/n): ' e devolve True para s/S/sim, False para o resto."""
    # TODO Time 2
    pass


def coletar_dados_produto():
    """
    Pergunta todos os campos de um produto e devolve o dicionário (SEM código):
    {"nome", "categoria", "tamanho", "cor", "preco_custo", "preco_venda", "quantidade"}
    Se preco_venda < preco_custo, avisa (aviso), mas aceita.
    """
    # TODO Time 2
    pass


def coletar_dados_cliente():
    """Pergunta nome, telefone e cidade e devolve {"nome", "telefone", "cidade"}."""
    # TODO Time 2
    pass


def coletar_item():
    """
    Pergunta o código do produto e a quantidade (mínimo 1).
    Devolve {"codigo": int, "quantidade": int}.
    """
    # TODO Time 2
    pass


def coletar_desconto():
    """Pergunta o desconto em % (0 a 100). Enter vazio = 0. Devolve float."""
    # TODO Time 2
    pass


def coletar_forma_pagamento():
    """Pergunta a forma de pagamento entre pix / dinheiro / cartão. Devolve a string escolhida."""
    # TODO Time 2
    pass


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python coleta.py e digite valores errados de propósito)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Teste: digite letras onde pede número para ver se o programa aguenta.")
    n = ler_inteiro("Um inteiro >= 1: ", minimo=1)
    print("Você digitou:", n)
    v = ler_decimal("Um preço (pode usar vírgula): ")
    print("Você digitou:", v)
    op = ler_opcao("Escolha 0, 1 ou 2: ", ["0", "1", "2"])
    print("Opção:", op)
    print("Confirmou?", confirmar("Tudo certo"))
    print("Item:", coletar_item())
