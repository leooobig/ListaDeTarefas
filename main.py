import json
import os

def ler(tarefas,caminho_arquivo):
    dados = tarefas
    try:
        with open(caminho_arquivo,'r',encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não encontrado, criando um novo...')
        salvar(tarefas,caminho_arquivo)
    return dados

def salvar(tarefas,caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo,'w',encoding='utf8') as arquivo:
        dados = json.dump(tarefas,arquivo,indent=2,ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'ToDoListDADOS.json'
tarefas = ler([],CAMINHO_ARQUIVO)

def validando_opcao():
    while True:
        opcao = input('Digite a opção desejada: ')
        if opcao in ['1', '2', '3','4', '5']:
            return opcao
        else:
            print('Opção inválida, tente novamente.')
            continue     

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
    os.system('cls')
    if len(tarefas) == 0:
        print('Não há tarefas a ser deletadas')
        print()
        return
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
    os.system('cls')
    if len(tarefas) == 0:
        print('Não há tarefas a ser concluidas')
        print()
        return
    visualizarTarefas()
    while True:
        try:
            opcaotarefa = int(input('Qual tarefa você concluiu?'))
            opcaotarefa = opcaotarefa - 1
            if 0 <= opcaotarefa <= len(tarefas):
                tarefas[opcaotarefa]['concluida'] = 'Concluida'
                os.system('cls')                
                break
            else:
                print('Número de escolha fora das opções.')
                continue
        except ValueError:
            print('A escolha deve ser de acordo com o número')
            continue

def sair():
    os.system('cls')
    salvar(tarefas,CAMINHO_ARQUIVO)
    print('FIM')
    exit()

opcoes = {
        '1':lambda: adicionarTarefa(),
        '2':lambda: visualizarTarefas(),
        '3':lambda: tarefaConcluida(),
        '4':lambda: deletarTarefa(),
        '5':lambda: sair()  
}

validando_programa = True
while validando_programa:
    print(f'To Do List: \n1. Adicionar Tarefa\n2. Visualizar Tarefas\n3. Marcar tarefa como concluida\n4. Remover tarefa\n5. Sair')
    print()
    opcao = validando_opcao()
    comando = opcoes.get(opcao)
    comando()




