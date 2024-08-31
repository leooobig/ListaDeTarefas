import os

tarefas = []
def validando_opcao():
    while True:
        opcao = input('Digite a opção desejada: ')
        try:
            opcao = int(opcao)
            if opcao in (1, 2, 3, 4, 5):
                return opcao
        except ValueError:
            print('Opção inválida, tente novamente.')
        
def executaOpcao(opcao):
    if opcao == 1:
       adicionarTarefa()
    elif opcao == 2:
        visualizarTarefas()
    elif opcao == 3:
        tarefaConcluida()
    elif opcao == 4:
        deletarTarefa()
    elif opcao == 5:
        os.system('cls')
        print('FIM')
        exit()

def adicionarTarefa():
    tarefa = input('Digite sua tarefa: ')
    tarefas.append({'nome':tarefa , 'concluida':'Não Concluida'})
    os.system('cls')
    print(f'Tarefa "{tarefa}" adicionado a lista')

def visualizarTarefas():
    os.system('cls')
    print('LISTA DE TAREFAS')
    for i,tarefa in enumerate(tarefas):
            print(f'{i+1}. {tarefa['nome']} = {tarefa['concluida']}')
    print()

def deletarTarefa():
    visualizarTarefas()
    while True:
        try:
            opcaotarefa = int(input('Escolha qual tarefa deseja excluir (Por número)?'))
            opcaotarefa = opcaotarefa - 1
            if opcaotarefa >= 0 and opcaotarefa < len(tarefas):
                tarefas.remove(tarefas[opcaotarefa])
                os.system('cls')
                print(f'Tarefa removida com sucesso')
                break
            else:
                print('Número inválido. Escolha um número dentro do intervalo de tarefas.')
                continue
        except ValueError:
            print('A escolha deve ser de acordo com o número')
            continue
          
def tarefaConcluida():
    visualizarTarefas()
    while True:
        try:
            opcaotarefa = int(input('Qual tarefa você concluiu?'))
            opcaotarefa = opcaotarefa - 1
            if opcaotarefa >= 0 and opcaotarefa < len(tarefas):
                tarefas[opcaotarefa]['concluida'] = 'Concluida'
                os.system('cls')                
                break
            else:
                print('Número de escolha fora das opções.')
                continue
        except ValueError:
            print('A escolha deve ser de acordo com o número')
            continue