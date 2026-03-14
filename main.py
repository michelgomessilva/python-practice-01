"""
Classificador de Idade
Determina se uma pessoa é menor de idade, adulta ou aposentada
com base no nome e na idade fornecidos.
"""

MIN_ADULT_AGE = 18
MAX_ADULT_AGE = 65


def classify_age(age: int) -> str:
    """
    Classifica uma pessoa de acordo com a sua idade.

    Args:
        age: Idade da pessoa (deve ser um inteiro não-negativo).

    Returns:
        Uma string com a classificação: 'menor de idade', 'adulto' ou 'aposentado'.

    Raises:
        TypeError: Se a idade não for um inteiro.
        ValueError: Se a idade for negativa.
    """
    if not isinstance(age, int):
        raise TypeError(f"Idade deve ser um inteiro, recebeu: {type(age).__name__!r}")
    if age < 0:
        raise ValueError(f"Idade não pode ser negativa, recebeu: {age}")

    if age < MIN_ADULT_AGE:
        return "menor de idade"
    if age <= MAX_ADULT_AGE:
        return "adulto"
    return "aposentado"


def format_message(name: str, age: int, classification: str) -> str:
    """
    Formata a mensagem de resultado para exibição ao utilizador.

    Args:
        name: Nome da pessoa.
        age: Idade da pessoa.
        classification: Classificação retornada por `classify_age`.

    Returns:
        String formatada com a mensagem de resultado.

    Raises:
        ValueError: Se o nome for uma string vazia ou composta apenas de espaços.
    """
    if not name or not name.strip():
        raise ValueError("O nome não pode ser vazio.")

    return (
        f"\nOlá, {name.strip()}! "
        f"Como você tem {age} anos, você é {classification}."
    )


def get_validated_age(prompt: str) -> int:
    """
    Solicita e valida a idade via entrada do utilizador.

    Args:
        prompt: Texto exibido ao utilizador.

    Returns:
        Idade como inteiro não-negativo.
    """
    raw = input(prompt).strip()

    if not raw.lstrip("-").isdigit():
        raise ValueError(f"Entrada inválida para idade: {raw!r}. Informe um número inteiro.")

    age = int(raw)

    if age < 0:
        raise ValueError(f"A idade não pode ser negativa: {age}")

    return age


def main() -> None:
    """Ponto de entrada principal do programa."""
    print("--- Classificador de Idade ---\n")

    name = input("Digite o seu nome: ").strip()
    if not name:
        print("Erro: o nome não pode estar vazio.")
        return

    try:
        age = get_validated_age("Digite a sua idade: ")
    except ValueError as exc:
        print(f"Erro: {exc}")
        return

    classification = classify_age(age)
    message = format_message(name, age, classification)
    print(message)


if __name__ == "__main__":
    main()
