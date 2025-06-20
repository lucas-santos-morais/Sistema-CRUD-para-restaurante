from restaurante import (
    adicionar_restaurante,
    buscar_restaurante_por_nome,
    alternar_status_restaurante,
    excluir_restaurante
)

def test_adicionar_restaurante():
    resultado = adicionar_restaurante('Teste', 'Japonesa')
    assert resultado['nome'] == 'Teste'
    assert resultado['categoria'] == 'Japonesa'
    assert resultado['ativo'] is False

def test_buscar_restaurante_por_nome():
    adicionar_restaurante('KFC', 'Fast Food')
    r = buscar_restaurante_por_nome('KFC')
    assert r is not None
    assert r['categoria'] == 'Fast Food'

def test_alternar_status_restaurante():
    adicionar_restaurante('StatusTest', 'Vegana')
    status_antes = buscar_restaurante_por_nome('StatusTest')['ativo']
    status_depois = alternar_status_restaurante('StatusTest')
    assert status_depois != status_antes

def test_excluir_restaurante():
    adicionar_restaurante('DeletarTest', 'Saudável')
    assert excluir_restaurante('DeletarTest') is True
    assert buscar_restaurante_por_nome('DeletarTest') is None
