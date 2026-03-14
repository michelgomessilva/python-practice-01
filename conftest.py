"""
conftest.py — raiz do projeto.
Garante que o diretório raiz está no sys.path para que
os módulos do projeto possam ser importados pelos testes.
"""

import sys
from pathlib import Path

# Adiciona a raiz do projeto ao path para importar main.py
sys.path.insert(0, str(Path(__file__).parent))
