"""
calculos.py — TIME 4: MANIPULAÇÕES MATEMÁTICAS

Responsabilidade: toda conta do sistema. Funções puras: recebem, calculam, devolvem.
Nunca alteram dicionários e nunca usam print/input.

Prefixos: calcular_, formatar_
Depende de: cadastro.py (buscar_produto)
Usado por: interface.py (T1, formatar_moeda) e main.py (T6)

Regras do contrato:
- Dinheiro é float arredondado a 2 casas (round(valor, 2)).
- Percentual de desconto vai de 0 a 100.
"""

from cadastro import buscar_produto


def calcular_subtotal(preco_unitario, quantidade):
    """Devolve preco_unitario * quantidade arredondado a 2 casas."""
    # TODO Time 4
    pass


def calcular_total_itens(itens, produtos):
    """
    Soma preco_venda * quantidade de cada item de uma venda.
    itens = {codigo_produto: quantidade}
    Usa buscar_produto para achar o preço. Itens com código inexistente são ignorados.
    """
    # TODO Time 4
    pass


def calcular_total_compra(itens, produtos):
    """Igual a calcular_total_itens, mas usando preco_custo (compra do fornecedor)."""
    # TODO Time 4
    pass


def aplicar_desconto(valor, percentual):
    """Devolve valor * (1 - percentual / 100), arredondado a 2 casas."""
    # TODO Time 4
    pass


def calcular_troco(total, valor_pago):
    """Devolve valor_pago - total (pagamento em dinheiro). Pode ser negativo se faltou dinheiro."""
    # TODO Time 4
    pass


def calcular_margem(preco_custo, preco_venda):
    """Devolve a margem em % = (preco_venda - preco_custo) / preco_custo * 100. Se custo for 0, devolve 0."""
    # TODO Time 4
    pass


def calcular_lucro_venda(itens, produtos):
    """Soma (preco_venda - preco_custo) * quantidade de cada item."""
    # TODO Time 4
    pass


def calcular_valor_estoque(produtos):
    """
    Devolve {"custo": X, "venda": Y, "lucro_potencial": Y - X}
    somando preco * quantidade de todos os produtos em estoque.
    """
    # TODO Time 4
    pass


def resumo_financeiro(vendas, compras):
    """
    Devolve um dicionário:
    {
        "total_vendas": soma dos totais de vendas,
        "total_compras": soma dos totais de compras,
        "saldo": total_vendas - total_compras,
        "qtd_vendas": quantas vendas,
        "qtd_compras": quantas compras,
        "ticket_medio": total_vendas / qtd_vendas (0 se não houver vendas),
    }
    """
    # TODO Time 4
    pass


def formatar_moeda(valor):
    """Devolve o valor no formato brasileiro: 1234.5 -> 'R$ 1.234,50'."""
    # TODO Time 4
    # Dica: f"{valor:,.2f}" gera '1,234.50'; depois troque ',' por 'X', '.' por ',' e 'X' por '.'
    pass


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python calculos.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()
    produtos = sistema["produtos"]
    itens = {1: 2, 2: 1}  # 2 camisetas (45) + 1 calça (129.9) = 219.9

    print("calcular_subtotal(45, 2) ->", calcular_subtotal(45, 2), "(esperado: 90.0)")
    print("calcular_total_itens ->", calcular_total_itens(itens, produtos), "(esperado: 219.9)")
    print("calcular_total_compra ->", calcular_total_compra(itens, produtos), "(esperado: 100.0)")
    print("aplicar_desconto(219.9, 10) ->", aplicar_desconto(219.9, 10), "(esperado: 197.91)")
    print("calcular_margem(20, 45) ->", calcular_margem(20, 45), "(esperado: 125.0)")
    print("calcular_lucro_venda ->", calcular_lucro_venda(itens, produtos), "(esperado: 119.9)")
    print("calcular_valor_estoque ->", calcular_valor_estoque(produtos))
    print("formatar_moeda(1234.5) ->", formatar_moeda(1234.5), "(esperado: R$ 1.234,50)")
