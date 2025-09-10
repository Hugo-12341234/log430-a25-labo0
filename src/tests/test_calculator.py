"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import math
import pytest
from src.calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5