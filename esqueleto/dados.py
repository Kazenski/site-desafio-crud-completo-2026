"""
dados.py — COMPARTILHADO POR TODOS OS TIMES

Dados de exemplo para todo mundo testar com o mesmo cenário.
Este arquivo já está pronto: NÃO precisa alterar.

Uso em qualquer arquivo:
    from dados import criar_sistema
    sistema = criar_sistema()
    print(sistema["produtos"][1]["nome"])
"""


def criar_sistema():
    """Devolve o dicionário 'sistema' completo, com dados de exemplo."""
    return {
        "produtos": {
            1: {
                "nome": "Camiseta básica",
                "categoria": "Camiseta",
                "tamanho": "M",
                "cor": "Preta",
                "preco_custo": 20.0,
                "preco_venda": 45.0,
                "quantidade": 10,
            },
            2: {
                "nome": "Calça jeans",
                "categoria": "Calça",
                "tamanho": "38",
                "cor": "Azul",
                "preco_custo": 60.0,
                "preco_venda": 129.9,
                "quantidade": 4,
            },
        },
        "clientes": {
            1: {
                "nome": "Maria Silva",
                "telefone": "(11) 99999-0000",
                "cidade": "São Paulo",
            },
        },
        "vendas": {},
        "compras": {},
        "caixa": 0.0,
    }


def criar_sistema_vazio():
    """Devolve o dicionário 'sistema' sem nenhum registro (útil para testar cadastro do zero)."""
    return {
        "produtos": {},
        "clientes": {},
        "vendas": {},
        "compras": {},
        "caixa": 0.0,
    }


if __name__ == "__main__":
    sistema = criar_sistema()
    print("Produtos cadastrados:", len(sistema["produtos"]))
    print("Clientes cadastrados:", len(sistema["clientes"]))
    print("Caixa inicial:", sistema["caixa"])
