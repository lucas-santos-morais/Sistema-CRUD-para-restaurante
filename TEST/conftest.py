import pytest
import restaurante

@pytest.fixture(autouse=True)
def resetar_restaurantes():
    restaurante.restaurantes.clear()
    restaurante.restaurantes.extend([
        {'nome': 'Bom Prato', 'categoria': 'geral', 'ativo': True},
        {'nome': 'Ragazzo', 'categoria': 'italiana', 'ativo': False}
    ])
