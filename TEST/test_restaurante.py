import pytest
from SRC import restaurante

def test_adicionar_restaurante():
    resultado = restaurante.adicionar_restaurante('Teste', 'Japonesa')
    assert resultado['nome'] == 'Teste'
    assert resultado['categoria'] == 'Japonesa'
    assert resultado['ativo'] is False

def test_buscar_restaurante_por_nome():
    restaurante.adicionar_restaurante('KFC', 'Fast Food')
    r = restaurante.buscar_restaurante_por_nome('KFC')
    assert r is not None
    assert r['categoria'] == 'Fast Food'

def test_alternar_status_restaurante():
    restaurante.adicionar_restaurante('StatusTest', 'Vegana')
    status_antes = restaurante.buscar_restaurante_por_nome('StatusTest')['ativo']
    status_depois = restaurante.alternar_status_restaurante('StatusTest')
    assert status_depois != status_antes  # status foi alternado

def test_excluir_restaurante():
    restaurante.adicionar_restaurante('DeletarTest', 'Saudável')
    assert restaurante.excluir_restaurante('DeletarTest') is True
    assert restaurante.buscar_restaurante_por_nome('DeletarTest') is None
