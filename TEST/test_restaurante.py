import pytest
from SRC import restaurante

def test_lista_inicial_tem_dois_restaurantes():
    assert len(restaurante.restaurantes) == 2

def test_restaurante_tem_campos_esperados():
    r = restaurante.restaurantes[0]
    assert 'nome' in r
    assert 'categoria' in r
    assert 'ativo' in r

def test_ativar_e_desativar_restaurante():
    nome_alvo = 'Bom Prato'
    for r in restaurante.restaurantes:
        if r['nome'] == nome_alvo:
            status_inicial = r['ativo']
            r['ativo'] = not r['ativo']
            assert r['ativo'] != status_inicial
            break
    else:
        pytest.fail('Restaurante não encontrado')