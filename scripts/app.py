import os

#Tratando com variável global
restaurantes = [
    {'nome': 'x', 'categoria':'Pizzaria', 'ativo':False},
    {'nome': 'y', 'categoria': 'Sorveteria', 'ativo':False}
                ]

def exibir_msg():
    
    x = input('Deseja seguir para o menu principal? \n').strip().lower()
    return x

def exibir_nome_programa():
    print('Larry Foods')

def exibir_funcionalidades_do_programa():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar status do restaurante ')
    print('4. Sair')

def exibir_titulos_programa(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * len(texto)) 
    print(texto)
    print('*' * len(texto)) 
## Finalizando APP
def finalizar_app():
    exibir_titulos_programa('Finalizando APP...')

def retorno_programa():
    retorno_programa = input('Deseja retornar ao programa? sim/não ').strip().lower()
    return retorno_programa

def cadastra_restaurante():
    #Obtendo informações do restaurante.
    cadastro_nome = input('Qual o nome do restaurante que você deseja cadastrar? ').strip().lower()
    cadastro_categoria = input(f'Qual a categoria pertence o restaurante {cadastro_nome}? Ex: Pizzaria, Sorveteria... ').strip().lower()
    ativo = False
    
    dados_restaurante = {'nome': cadastro_nome,
                         'categoria': cadastro_categoria,
                         'ativo': ativo}
    
    
    restaurantes.append(dados_restaurante)
    
    
    print(f'Restaurante {cadastro_nome} que pertence a categoria de {cadastro_categoria} cadastrado com sucesso.')
    return restaurantes

def lista_restaurantes():
    print('Listando restaurantes...: \n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        # Ternário: conv_vdd if x else cond_fals
        status = 'Sim' if ativo else 'Não'
        print(f'Restaurante: {nome_restaurante} - Categoria: {categoria} - Aberto: {status}')

def altera_status_restaurante():
    exibir_titulos_programa('Bem-vindo a funcionalidade de ativação/inativação de restaurantes')
    encontrado = False
    
    r_escolhido = input('Qual o nome do restaurante que você deseja alterar? ').strip().lower()
    
    try:
        for r in restaurantes:
            if r['nome'].lower() == r_escolhido.lower():
                r['ativo'] = not r['ativo']
                status = 'Ativo' if r['ativo'] == True else 'Inativo'
                print(f'O restaurante {r_escolhido} teve o seu status atualizado com sucesso para {status}')
                encontrado = True
                break
        
        if not encontrado:
            print('O restaurante não foi encontrado na base de dados. Favor, apontar um dos restaurantes listados abaixo:')
            lista_restaurantes()
            retorno_programa()
    except ValueError:
        print('O código não foi compilado com sucesso!')
                      
def perguntar_continuar():
    while True:
        resposta = input('Deseja voltar ao menu principal? (s/n): ').strip().lower()
        match resposta:
            case 's' | 'sim':
                main()
                return
            case 'n' | 'nao' | 'não':
                finalizar_app()
                return
            case _:
                print('Opção inválida. Tente novamente.\n')

  
def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção. Obs: 1,2,3,4 '))
        
        match opcao_escolhida:
            case 1:
                print('Bem-vindo ao cadastro de restaurantes...\n')
                cadastra_restaurante()
                
                while True:
                    outro = input('Deseja cadastrar outro restaurante? \n')
                    match outro: 
                        case 'sim' | 's':
                            cadastra_restaurante()
                            continue
                        case 'não' | 'nao' | 'n':
                            while True:
                                x = input('Deseja encerrar a aplicação? (s/n) \n')
                                match x:
                                    case 'sim' | 's':
                                        finalizar_app()
                                        return
                                    case 'não' | 'nao' | 'n':
                                        print('Voltando ao menu...\n')
                                        main()
                                        return 
                                    case _:
                                        print('Opção inválida!')
                        case _:
                            print('Opção inválida! Tente novamente.\n')
            case 2:
                lista_restaurantes()
                #voltando ao menu ou saindo do app;
                perguntar_continuar()
            case 3:
                altera_status_restaurante()
                #voltando ao menu ou saindo do app;
                perguntar_continuar()
            case 4:
                finalizar_app()   
    except ValueError:
        print('Opção Inválida! Escolha uma opção dentre: (1,2,3,4)')
        perguntar_continuar()
 
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_programa()
    exibir_funcionalidades_do_programa()
    escolher_opcao()
    
if __name__ == '__main__':
    main()
    