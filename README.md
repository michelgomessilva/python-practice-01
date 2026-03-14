# 🎂 Classificador de Idade

Programa Python que classifica uma pessoa como **menor de idade**, **adulto** ou **aposentado** com base no nome e na idade fornecidos via terminal.

---

## 📁 Estrutura do projeto

```
Practice 1/
├── main.py              # Lógica principal
├── conftest.py          # Configuração do pytest (sys.path)
├── pyproject.toml       # Dependências e configuração do projeto
├── uv.lock              # Lockfile gerado pelo uv
└── Unit Tests/
    └── test_main.py     # Suite de testes com pytest (27 testes)
```

---

## ⚙️ Pré-requisitos

- [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado globalmente
- Python 3.10+

---

## 🚀 Primeiros passos

### 1. Instalar dependências

```bash
uv sync --group dev
```

> Cria o ambiente virtual `.venv` e instala todas as dependências, incluindo `pytest`.

---

### 2. Rodar a aplicação

```bash
uv run main.py
```

**Exemplo de execução:**

```
--- Classificador de Idade ---

Digite o seu nome: Maria
Digite a sua idade: 72

Olá, Maria! Como você tem 72 anos, você é aposentado.
```

---

## 🧪 Testes

A suite cobre fronteiras, guard clauses e integração — **27 testes no total**.

### Rodar todos os testes

```bash
uv run --group dev pytest
```

### Saída detalhada (recomendado)

```bash
uv run --group dev pytest -v
```

### Saída resumida (ideal para CI)

```bash
uv run --group dev pytest -q
```

### Filtrar por classe de teste

```bash
# Apenas testes de classify_age
uv run --group dev pytest -v -k "TestClassifyAge"

# Apenas testes de format_message
uv run --group dev pytest -v -k "TestFormatMessage"

# Apenas testes de integração
uv run --group dev pytest -v -k "TestIntegration"
```

### Parar na primeira falha

```bash
uv run --group dev pytest -x
```

---

## 🏗️ Arquitetura

| Função | Descrição |
|--------|-----------|
| `classify_age(age)` | Classifica a idade; pura e sem I/O |
| `format_message(name, age, classification)` | Formata a mensagem final |
| `get_validated_age(prompt)` | Valida a entrada do utilizador |
| `main()` | Ponto de entrada, orquestra o fluxo |

### Regras de negócio

| Faixa de idade | Classificação |
|----------------|---------------|
| 0 – 17 | Menor de idade |
| 18 – 65 | Adulto |
| 66+ | Aposentado |

---

## 🧰 Comandos de referência rápida

| Ação | Comando |
|------|---------|
| Instalar dependências | `uv sync --group dev` |
| Rodar aplicação | `uv run main.py` |
| Rodar testes | `uv run --group dev pytest` |
| Rodar testes (verbose) | `uv run --group dev pytest -v` |
| Rodar testes (silencioso) | `uv run --group dev pytest -q` |
| Filtrar testes | `uv run --group dev pytest -k "NomeDaClasse"` |
