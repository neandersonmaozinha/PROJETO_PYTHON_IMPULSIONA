import os

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
    print('Finalizando o app\n')

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

# código omitido

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        
        if opcao_escolhida == 1: 
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2: 
            print('Listar restaurantes')
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
    


