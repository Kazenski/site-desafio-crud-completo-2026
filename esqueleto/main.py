"""
main.py — TIME 6 (parte 2): INTEGRAÇÃO

Responsabilidade: ligar tudo. Menu principal, submenus e os fluxos completos
(venda, compra, CRUD) que chamam as funções dos outros cinco times.

Prefixos: fluxo_, menu_, executar_
Depende de: TODOS os módulos
Para rodar:  python main.py

Os menus já estão prontos para mostrar o encaixe.
Os fluxos estão com o passo a passo em comentários — siga os diagramas
de sequência do site (seção 8) e troque os comentários por código.
"""

from dados import criar_sistema

import interface as ui
import coleta as col
import cadastro as cad
import calculos as calc
import estoque as est
import atualizacao as atu


# ===========================================================================
# PRODUTOS
# ===========================================================================

def fluxo_cadastrar_produto(sistema):
    """Sequência 8.3 do site."""
    # 1. dados = col.coletar_dados_produto()
    # 2. codigo = cad.cadastrar_produto(sistema["produtos"], dados)
    # 3. ui.exibir_mensagem(f"Produto {codigo} cadastrado", "ok")
    pass  # TODO Time 6


def fluxo_listar_produtos(sistema):
    # 1. ui.exibir_tabela_produtos(sistema["produtos"])
    pass  # TODO Time 6


def fluxo_atualizar_produto(sistema):
    """Sequência 8.4 do site."""
    # 1. ui.exibir_tabela_produtos(produtos)
    # 2. codigo = col.ler_inteiro("Código do produto: ", minimo=1)
    # 3. produto = cad.buscar_produto(produtos, codigo)
    # 4. se None -> ui.exibir_mensagem("Produto não encontrado", "erro") e return
    # 5. ui.exibir_produto(codigo, produto)
    # 6. campo = col.ler_opcao("Campo: ", atu.CAMPOS_PRODUTO_EDITAVEIS)
    # 7. novo_valor = col.ler_decimal(...) se campo começa com "preco_", senão col.ler_texto(...)
    # 8. atu.atualizar_produto(produtos, codigo, campo, novo_valor)
    # 9. ui.exibir_mensagem("Produto atualizado", "ok")
    pass  # TODO Time 6


def fluxo_remover_produto(sistema):
    # 1. ui.exibir_tabela_produtos(produtos)
    # 2. codigo = col.ler_inteiro("Código do produto: ", minimo=1)
    # 3. produto = cad.buscar_produto(produtos, codigo) -> se None, erro e return
    # 4. ui.exibir_produto(codigo, produto)
    # 5. if col.confirmar("Remover este produto?"): atu.remover_produto(...) e mensagem ok
    pass  # TODO Time 6


# ===========================================================================
# CLIENTES
# ===========================================================================

def fluxo_cadastrar_cliente(sistema):
    # igual ao de produto, com coletar_dados_cliente / cadastrar_cliente
    pass  # TODO Time 6


def fluxo_listar_clientes(sistema):
    pass  # TODO Time 6


def fluxo_atualizar_cliente(sistema):
    # igual ao de produto, com buscar_cliente / atu.CAMPOS_CLIENTE_EDITAVEIS / atualizar_cliente
    pass  # TODO Time 6


def fluxo_remover_cliente(sistema):
    pass  # TODO Time 6


# ===========================================================================
# VENDAS
# ===========================================================================

def fluxo_realizar_venda(sistema):
    """Sequência 8.1 e atividade 9.2 do site. O fluxo que cruza todos os times."""
    produtos = sistema["produtos"]
    clientes = sistema["clientes"]

    # --- 1. Cliente -------------------------------------------------------
    # ui.exibir_tabela_clientes(clientes)
    # codigo_cliente = col.ler_inteiro("Código do cliente: ", minimo=1)
    # cliente = cad.buscar_cliente(clientes, codigo_cliente)
    # if cliente is None: ui.exibir_mensagem("Cliente não encontrado", "erro"); return

    # --- 2. Itens (repete até responder não) -------------------------------
    # itens = {}
    # continuar = True
    # while continuar:
    #     ui.exibir_tabela_produtos(produtos)
    #     item = col.coletar_item()
    #     if est.verificar_disponibilidade(produtos, item["codigo"], item["quantidade"]):
    #         itens[item["codigo"]] = item["quantidade"]
    #     else:
    #         ui.exibir_mensagem("Sem estoque suficiente ou código inválido", "erro")
    #     continuar = col.confirmar("Adicionar outro item?")
    # if not itens: ui.exibir_mensagem("Venda cancelada: nenhum item", "aviso"); return

    # --- 3. Valores --------------------------------------------------------
    # total_bruto = calc.calcular_total_itens(itens, produtos)
    # desconto = col.coletar_desconto()
    # total = calc.aplicar_desconto(total_bruto, desconto)
    # forma = col.coletar_forma_pagamento()
    # ui.exibir_mensagem(f"Total: {calc.formatar_moeda(total)}", "info")

    # --- 4. Confirmação e efeitos -----------------------------------------
    # if not col.confirmar("Finalizar venda?"): ui.exibir_mensagem("Venda cancelada", "aviso"); return
    # est.baixar_estoque_itens(produtos, itens)
    # venda = {"cliente": codigo_cliente, "itens": itens, "desconto": desconto,
    #          "total": total, "forma_pagamento": forma}
    # cad.registrar_venda(sistema["vendas"], venda)
    # atu.atualizar_caixa(sistema, total)
    # ui.exibir_recibo(venda, produtos, clientes)
    pass  # TODO Time 6


def fluxo_listar_vendas(sistema):
    # para cada codigo, venda em sistema["vendas"].items(): ui.exibir_recibo(venda, produtos, clientes)
    pass  # TODO Time 6


# ===========================================================================
# COMPRAS (reposição)
# ===========================================================================

def fluxo_realizar_compra(sistema):
    """Sequência 8.2 do site."""
    # 1. fornecedor = col.ler_texto("Fornecedor: ")
    # 2. laço de itens igual ao da venda, mas validando com cad.buscar_produto (não precisa ter estoque)
    # 3. total = calc.calcular_total_compra(itens, produtos)
    # 4. if not col.confirmar(f"Confirmar compra de {calc.formatar_moeda(total)}?"): return
    # 5. est.repor_estoque_itens(produtos, itens)
    # 6. cad.registrar_compra(sistema["compras"], {"fornecedor": fornecedor, "itens": itens, "total": total})
    # 7. atu.atualizar_caixa(sistema, -total)
    # 8. ui.exibir_mensagem("Compra registrada e estoque atualizado", "ok")
    pass  # TODO Time 6


def fluxo_listar_compras(sistema):
    pass  # TODO Time 6


# ===========================================================================
# ESTOQUE E RELATÓRIOS
# ===========================================================================

def fluxo_relatorio_estoque(sistema):
    # relatorio = est.relatorio_estoque(sistema["produtos"])
    # ui.exibir_relatorio_estoque(relatorio)
    pass  # TODO Time 6


def fluxo_produtos_em_falta(sistema):
    # em_falta = est.produtos_em_falta(sistema["produtos"])
    # ui.exibir_tabela_produtos(em_falta)
    pass  # TODO Time 6


def fluxo_relatorio_financeiro(sistema):
    # resumo = calc.resumo_financeiro(sistema["vendas"], sistema["compras"])
    # ui.exibir_resumo_financeiro(resumo)
    # ui.exibir_mensagem(f"Caixa atual: {calc.formatar_moeda(sistema['caixa'])}", "info")
    pass  # TODO Time 6


def fluxo_valor_estoque(sistema):
    # valores = calc.calcular_valor_estoque(sistema["produtos"])
    # imprimir custo, venda e lucro potencial com formatar_moeda
    pass  # TODO Time 6


# ===========================================================================
# MENUS (já prontos — mostram como as peças se encaixam)
# ===========================================================================

def menu_produtos(sistema):
    while True:
        ui.exibir_menu_produtos()
        opcao = col.ler_opcao("Opção: ", ["0", "1", "2", "3", "4"])
        if opcao == "1":
            fluxo_cadastrar_produto(sistema)
        elif opcao == "2":
            fluxo_listar_produtos(sistema)
        elif opcao == "3":
            fluxo_atualizar_produto(sistema)
        elif opcao == "4":
            fluxo_remover_produto(sistema)
        else:
            return


def menu_clientes(sistema):
    while True:
        ui.exibir_menu_clientes()
        opcao = col.ler_opcao("Opção: ", ["0", "1", "2", "3", "4"])
        if opcao == "1":
            fluxo_cadastrar_cliente(sistema)
        elif opcao == "2":
            fluxo_listar_clientes(sistema)
        elif opcao == "3":
            fluxo_atualizar_cliente(sistema)
        elif opcao == "4":
            fluxo_remover_cliente(sistema)
        else:
            return


def menu_vendas(sistema):
    while True:
        ui.exibir_menu_vendas()
        opcao = col.ler_opcao("Opção: ", ["0", "1", "2"])
        if opcao == "1":
            fluxo_realizar_venda(sistema)
        elif opcao == "2":
            fluxo_listar_vendas(sistema)
        else:
            return


def menu_compras(sistema):
    while True:
        ui.exibir_menu_compras()
        opcao = col.ler_opcao("Opção: ", ["0", "1", "2"])
        if opcao == "1":
            fluxo_realizar_compra(sistema)
        elif opcao == "2":
            fluxo_listar_compras(sistema)
        else:
            return


def menu_estoque(sistema):
    while True:
        ui.exibir_menu_estoque()
        opcao = col.ler_opcao("Opção: ", ["0", "1", "2"])
        if opcao == "1":
            fluxo_relatorio_estoque(sistema)
        elif opcao == "2":
            fluxo_produtos_em_falta(sistema)
        else:
            return


def menu_relatorios(sistema):
    while True:
        ui.exibir_menu_relatorios()
        opcao = col.ler_opcao("Opção: ", ["0", "1", "2"])
        if opcao == "1":
            fluxo_relatorio_financeiro(sistema)
        elif opcao == "2":
            fluxo_valor_estoque(sistema)
        else:
            return


def executar_sistema(sistema):
    """Laço do menu principal (atividade 9.1 do site)."""
    ui.exibir_cabecalho()
    while True:
        ui.exibir_menu_principal()
        opcao = col.ler_opcao("Opção: ", ["0", "1", "2", "3", "4", "5", "6"])
        if opcao == "1":
            menu_produtos(sistema)
        elif opcao == "2":
            menu_clientes(sistema)
        elif opcao == "3":
            menu_vendas(sistema)
        elif opcao == "4":
            menu_compras(sistema)
        elif opcao == "5":
            menu_estoque(sistema)
        elif opcao == "6":
            menu_relatorios(sistema)
        else:
            ui.exibir_mensagem("Até logo!", "info")
            return


if __name__ == "__main__":
    sistema = criar_sistema()
    executar_sistema(sistema)
