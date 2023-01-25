import pytest
from src.funciones_maths import es_par, es_impar

def test_espar_con_par():
    valor = 2
    esperado = True
    assert es_par(valor) == esperado

def test_espar_con_impar():
    valor = 3
    esperado = False
    assert es_par(valor) == esperado

def test_esimpar_con_par():
    valor = 2
    esperado = False
    assert es_impar(valor) == esperado

def test_esimpar_con_impar():
    valor = 3
    esperado = True
    assert es_impar(valor) == esperado



