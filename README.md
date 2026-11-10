# Desafio CRUD Completo 2026 — Loja de Roupas Online

Modelagem UML de um sistema de **compra, venda e estoque** para uma vendedora de roupas online,
construído pelos alunos em Python usando **apenas funções e dicionários**, rodando no terminal.

O site apresenta o sistema em várias visões (casos de uso, componentes, dependências, dados,
sequência, atividade, estado e jornada do usuário), o contrato de funções de cada time e o plano
de integração. A pasta `esqueleto/` traz os arquivos `.py` já com nomes, parâmetros e docstrings
para cada time preencher.

## Estrutura

```
site-desafio-crud-completo-2026/
├── index.html          # o site (página única com todas as visões)
├── css/style.css
├── js/main.js          # renderiza os diagramas Mermaid e o zoom
├── img/                # coloque aqui a foto do quadro como quadro.jpg (opcional)
├── esqueleto/          # contrato de funções em código, um arquivo por time
│   ├── dados.py        # compartilhado: dados de exemplo (pronto)
│   ├── interface.py    # Time 1 — prints estáticos
│   ├── coleta.py       # Time 2 — coleta de dados
│   ├── cadastro.py     # Time 3 — cadastro de dados
│   ├── calculos.py     # Time 4 — manipulações matemáticas
│   ├── estoque.py      # Time 5 — controle de estoque
│   ├── atualizacao.py  # Time 6 — atualizações
│   └── main.py         # Time 6 — integração (menus prontos, fluxos a preencher)
└── README.md
```

## Ver o site localmente

Os diagramas são renderizados pela biblioteca Mermaid carregada via CDN, então basta abrir
`index.html` no navegador. Se o navegador bloquear o módulo JS em `file://`, suba um servidor simples:

```bash
python -m http.server 8000
# abra http://localhost:8000
```

## Publicar no GitHub Pages

```bash
cd site-desafio-crud-completo-2026
git init
git add .
git commit -m "Site do desafio CRUD 2026: modelagem UML e esqueleto"
git branch -M main
git remote add origin https://github.com/Kazenski/site-desafio-crud-completo-2026.git
git push -u origin main
```

Depois, no GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch →
Branch: `main` / `(root)` → Save**. Em alguns minutos o site estará em
`https://kazenski.github.io/site-desafio-crud-completo-2026/`.

## Rodar o esqueleto

```bash
cd esqueleto
python main.py          # menu principal (os fluxos ainda estão vazios)
python cadastro.py      # testes isolados do Time 3 (idem para os outros arquivos)
```

Cada arquivo tem um bloco `if __name__ == "__main__":` com testes e os valores esperados,
para o time conferir a própria entrega antes da integração.

## Times

| Time | Arquivo | Prefixos | Depende de |
|------|---------|----------|------------|
| 1 · Prints estáticos | `interface.py` | `exibir_` | T4, T5 |
| 2 · Coleta de dados | `coleta.py` | `ler_`, `coletar_` | T1 |
| 3 · Cadastro | `cadastro.py` | `cadastrar_`, `registrar_`, `buscar_` | — |
| 4 · Matemática | `calculos.py` | `calcular_`, `formatar_` | T3 |
| 5 · Estoque | `estoque.py` | `verificar_`, `baixar_`, `repor_`, `relatorio_` | T3 |
| 6 · Atualização e Integração | `atualizacao.py`, `main.py` | `atualizar_`, `remover_`, `fluxo_`, `menu_` | todos |
