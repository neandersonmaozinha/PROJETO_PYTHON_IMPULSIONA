import os

restaurantes = ['Pizza', 'Feijoada']

def exibir_nome_programa():
    print("""
      S̳a̳b̳o̳r̳ V̳i̳t̳ó̳r̳i̳a̳             
""")
def exibir_opcoes():
    print('1. Cadatrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao Menu Principal')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar\n')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_menu_principal()

def listar_restaurantes():
     exibir_subtitulo('Listando restaurantes')
     
     for restaurante in restaurantes:
         print(f'.{restaurante}')
     voltar_menu_principal()
   
  

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
             
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    


