import numpy as np
import pytest
from minhastats.desc import media, mediana, moda

def test_media_simple():
    dados = [5, 3, 7, 9, 10, 12, 15] # dados de entrada para teste

    expected = np.mean(dados) # media esperada, calculdada pela a lib de referência
    result = media(dados) # media calculada por implementação própria

    assert result == pytest.approx(expected, abs=1e-6) # comparação dos resultados com tolerância float

def test_validate(): # testa se a função de validação funciona
    with pytest.raises(ValueError):
        media([])

# testa a mediana por implementação própria quando a quantidade de elementos da listagem é ímpar
def test_mediana_odd():
    dados = [1, 3, 5, 7, 9]

    expected = np.median(dados)
    result = mediana(dados)

    assert result == pytest.approx(expected, abs=1e-6) 

# testa a mediana por implementação própria quando a quantidade de elementos da listagem é par
def test_mediana_even():
    dados = [1, 3, 5, 7]

    expected = np.median(dados)
    result = mediana(dados)

    assert result == pytest.approx(expected, abs=1e-6)

def test_moda_single(): # testa a moda por implementação própria, quando a moda for única
    dados = [1, 2, 2, 3, 3, 4, 1, 3, 2, 5, 2] # 2 é a moda pois aparece 4 vezes

    assert moda(dados) == [2]

def test_moda_multi(): # neste caso é quando a moda for multimodal
    dados = [1, 1, 2, 2, 3]

    result = moda(dados)
    assert sorted(result) == [1, 2]