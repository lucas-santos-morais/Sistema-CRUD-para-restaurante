import restaurante

def test_lista_inicial_tem_dois_restaurantes():
    assert len(restaurante.restaurantes) == 2

def test_adicionar_restaurante():
    novo = {'nome': 'Outback', 'categoria': 'Churrasco', 'ativo': False}
    restaurante.restaurantes.append(novo)
    assert len(restaurante.restaurantes) == 3
    assert restaurante.restaurantes[-1]['nome'] == 'Outback'

def test_alterar_status():
    for r in restaurante.restaurantes:
        if r['nome'] == 'Ragazzo':
            status_inicial = r['ativo']
            r['ativo'] = not r['ativo']
            assert r['ativo'] != status_inicial

def test_deletar_restaurante():
    nome = 'Bom Prato'
    restaurante.restaurantes = [r for r in restaurante.restaurantes if r['nome'] != nome]
    assert not any(r['nome'] == nome for r in restaurante.restaurantes)
