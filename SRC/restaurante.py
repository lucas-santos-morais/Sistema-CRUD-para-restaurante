'''importação do módulo os da biblioteca padrão do Python'''

import os

'''Lista de dicionários que armazena os restaurantes cadastrados.
Cada dicionário contém o nome, a categoria e se o restaurante está ativo ou não.'''

restaurantes = [{'nome':'Bom Prato', 'categoria':'geral', 'ativo':True},
                {'nome':'Ragazzo', 'categoria':'italiana', 'ativo':False}]



def exibir_nome_do_programa():
    '''Funções para exibir o nome do programa'''
    
    print('-- ꧁༺ 几ㄖᐯㄖ 丂卂乃ㄖ尺 ༻꧂ --\n')



def opcoes_do_menu():
    '''Função para exibir as opções do menu'''
    
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Restaurante')
    print('4. Deletar Restaurante')
    print('5. Sair\n')

def finalizando_app():
    '''Função para finalizar a aplicação'''
    
    os.system('cls')
    print('Finalizando aplicação...')

def opcao_invalida():
    '''Função para exibir mensagem de opção inválida''' 
    
    print('Opção inválida.\n')
    pressione_enter_para_continuar()

def pressione_enter_para_continuar():
    '''Função para pausar a execução do programa até que o usuário pressione Enter'''
    
    input('\nPressione Enter para continuar...')
    main()

def cadastrar_restaurante():
    '''Função para cadastrar um novo restaurante
    
    Input: O usuário deve informar o nome e a categoria do restaurante.
    
    O restaurante será adicionado à lista de restaurantes com o status "ativo" como False.'''
    
    os.system('cls')
    print('Cadastrar Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}:  ')
    dados = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados)
    print(f'O restaurante {nome_restaurante} foi cadastrado\n')
    pressione_enter_para_continuar()

def listar_restaurantes():
    '''Listar os restaurantes cadastrados, mostrando o nome, a categoria e se está ativo ou não.
    
    Se não houver restaurantes cadastrados, exibir uma mensagem informando que não há restaurantes.'''                          
    
    os.system('cls')
    print('Listando os restaurantes\n') 
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante} | {categoria_restaurante} | {ativo_restaurante}')
    pressione_enter_para_continuar()
    

def alterando_restaurante():
    '''Função para ativar ou desativar um restaurante.
    
    Input: O usuário deve informar o nome do restaurante que deseja ativar ou desativar.
    
    Se o restaurante for encontrado, seu status será alternado entre ativo e inativo.''' 
    
    os.system('cls')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar:  ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante ['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
    
    pressione_enter_para_continuar()
    
    
def deletar_restaurante():
    '''Função para deletar um restaurante.
    
    Input: O usuário deve informar o nome do restaurante que deseja deletar.
    
    Se o restaurante for encontrado, ele será removido da lista de restaurantes.'''
    
    os.system('cls')
    nome_restaurante = input('Digite o nome do restaurante que deseja deletar: ')
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurantes.remove(restaurante)
            print(f'O restaurante {nome_restaurante} foi deletado com sucesso!')
            break
    else:
        print('Restaurante não encontrado.')
        
        
    pressione_enter_para_continuar()
      

def opcoes_de_escolha():
    '''Função para capturar a opção escolhida pelo usuário e chamar a função correspondente'''
    
    try:
        opcao_escolhida = int(input('Digite a opção escolhida:'))
        if opcao_escolhida == 1:
            os.system('cls')
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterando_restaurante()
        elif opcao_escolhida == 4:
            deletar_restaurante()
        elif opcao_escolhida == 5:
            finalizando_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

    
def main():
    '''Função principal que executa o programa'''
    
    os.system('cls')
    exibir_nome_do_programa()
    opcoes_do_menu()
    opcoes_de_escolha()
    
if __name__ == '__main__':
    '''Ponto de entrada do programa'''
    main()


""" Parte do código que será usado na pasta de TEST do projeto"""

""" GitHub Actions será usado verifique os logs do projeto na aba "Actions """

import pytest
from SRC import restaurante


def test_adicionar_restaurante():
    """"Testes para o módulo restaurante.py"""
    
    resultado = restaurante.adicionar_restaurante('Teste', 'Japonesa')
    assert resultado['nome'] == 'Teste'
    assert resultado['categoria'] == 'Japonesa'
    assert resultado['ativo'] is False

def test_buscar_restaurante_por_nome():
    """Testa a busca de um restaurante pelo nome"""
    
    restaurante.adicionar_restaurante('KFC', 'Fast Food')
    r = restaurante.buscar_restaurante_por_nome('KFC')
    assert r is not None
    assert r['categoria'] == 'Fast Food'

def test_alternar_status_restaurante():
    """Testa a alternância de status de um restaurante"""
    
    restaurante.adicionar_restaurante('StatusTest', 'Vegana')
    status_antes = restaurante.buscar_restaurante_por_nome('StatusTest')['ativo']
    status_depois = restaurante.alternar_status_restaurante('StatusTest')
    assert status_depois != status_antes  # status foi alternado

def test_excluir_restaurante():
    """Testa a exclusão de um restaurante"""
    
    restaurante.adicionar_restaurante('DeletarTest', 'Saudável')
    assert restaurante.excluir_restaurante('DeletarTest') is True
    assert restaurante.buscar_restaurante_por_nome('DeletarTest') is None