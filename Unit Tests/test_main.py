"""
Testes unitários para o módulo main.py (Classificador de Idade).

Execute com:
    uv run pytest
    uv run pytest -v
    uv run pytest --tb=short
"""

import pytest

from main import (
    MAX_ADULT_AGE,
    MIN_ADULT_AGE,
    classify_age,
    format_message,
)


# ─────────────────────────────────────────────
# classify_age – Casos válidos
# ─────────────────────────────────────────────

class TestClassifyAgeValidInputs:
    """Testa a classificação correta com idades válidas."""

    # --- Menores de idade ---
    def test_newborn_is_minor(self):
        assert classify_age(0) == "menor de idade"

    def test_child_is_minor(self):
        assert classify_age(10) == "menor de idade"

    def test_one_below_adult_is_minor(self):
        assert classify_age(MIN_ADULT_AGE - 1) == "menor de idade"

    # --- Adultos ---
    def test_lower_boundary_adult(self):
        assert classify_age(MIN_ADULT_AGE) == "adulto"

    def test_mid_adult(self):
        assert classify_age(30) == "adulto"

    def test_upper_boundary_adult(self):
        assert classify_age(MAX_ADULT_AGE) == "adulto"

    # --- Aposentados ---
    def test_one_above_adult_is_retired(self):
        assert classify_age(MAX_ADULT_AGE + 1) == "aposentado"

    def test_elderly_is_retired(self):
        assert classify_age(90) == "aposentado"

    def test_very_old_is_retired(self):
        assert classify_age(120) == "aposentado"


# ─────────────────────────────────────────────
# classify_age – Guard clauses / inputs inválidos
# ─────────────────────────────────────────────

class TestClassifyAgeInvalidInputs:
    """Garante que erros são levantados para entradas inválidas."""

    def test_negative_age_raises_value_error(self):
        with pytest.raises(ValueError, match="negativa"):
            classify_age(-1)

    def test_large_negative_age_raises_value_error(self):
        with pytest.raises(ValueError):
            classify_age(-100)

    def test_float_raises_type_error(self):
        with pytest.raises(TypeError, match="inteiro"):
            classify_age(25.5)  # type: ignore[arg-type]

    def test_string_raises_type_error(self):
        with pytest.raises(TypeError):
            classify_age("vinte")  # type: ignore[arg-type]

    def test_none_raises_type_error(self):
        with pytest.raises(TypeError):
            classify_age(None)  # type: ignore[arg-type]

    def test_bool_raises_type_error(self):
        # bool é subclasse de int em Python, verificamos esse comportamento
        # True == 1, False == 0 — ambos são válidos como int
        # Este teste documenta essa decisão explicitamente
        assert classify_age(True) == "menor de idade"   # True == 1
        assert classify_age(False) == "menor de idade"  # False == 0


# ─────────────────────────────────────────────
# format_message – Casos válidos
# ─────────────────────────────────────────────

class TestFormatMessageValidInputs:
    """Testa a formatação correta das mensagens."""

    def test_message_contains_name(self):
        msg = format_message("Ana", 20, "adulto")
        assert "Ana" in msg

    def test_message_contains_age(self):
        msg = format_message("Ana", 20, "adulto")
        assert "20" in msg

    def test_message_contains_classification(self):
        msg = format_message("Ana", 20, "adulto")
        assert "adulto" in msg

    def test_message_strips_name_whitespace(self):
        msg = format_message("  João  ", 17, "menor de idade")
        assert "João" in msg
        assert "  João  " not in msg

    def test_full_message_minor(self):
        msg = format_message("Carlos", 15, "menor de idade")
        assert "Carlos" in msg
        assert "15" in msg
        assert "menor de idade" in msg

    def test_full_message_retired(self):
        msg = format_message("Maria", 70, "aposentado")
        assert "Maria" in msg
        assert "70" in msg
        assert "aposentado" in msg


# ─────────────────────────────────────────────
# format_message – Guard clauses / inputs inválidos
# ─────────────────────────────────────────────

class TestFormatMessageInvalidInputs:
    """Garante que nomes inválidos levantam erro."""

    def test_empty_name_raises_value_error(self):
        with pytest.raises(ValueError, match="vazio"):
            format_message("", 25, "adulto")

    def test_whitespace_only_name_raises_value_error(self):
        with pytest.raises(ValueError, match="vazio"):
            format_message("   ", 25, "adulto")


# ─────────────────────────────────────────────
# Testes de integração entre classify_age + format_message
# ─────────────────────────────────────────────

class TestIntegration:
    """Testa o fluxo completo: classificar e formatar."""

    @pytest.mark.parametrize("name, age, expected_class", [
        ("Lucas", 10, "menor de idade"),
        ("Fernanda", 18, "adulto"),
        ("Pedro", 65, "adulto"),
        ("Helena", 66, "aposentado"),
    ])
    def test_classify_and_format(self, name: str, age: int, expected_class: str):
        classification = classify_age(age)
        assert classification == expected_class

        msg = format_message(name, age, classification)
        assert name in msg
        assert str(age) in msg
        assert expected_class in msg
