from defs import executaOpcao, validando_opcao

validando_programa = True
while validando_programa:
    print(f'To Do List: \n1. Adicionar Tarefa\n2. Visualizar Tarefas\n3. Marcar tarefa como concluida\n4. Remover tarefa\n5. Sair')
    print()
    opcao = validando_opcao()
    executaOpcao(opcao)