from utils import adicionarTarefa, visualizarTarefas,tarefaConcluida,deletarTarefa,sair,validando_opcao

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




