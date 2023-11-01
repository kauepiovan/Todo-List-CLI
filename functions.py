import os

# view task
def view(todo_list):
    if len(todo_list) == 0:
        os.system('cls')
        print('-'*20, 'ToDo-List python', '-'*20)
        print('\nNenhuma tarefa encontrada. use o comando add para adicionar uma tarefa\nCaso tenha duvida digite ihelp.')

        os.system('pause')
    os.system('cls')
    
    c = 0
    print('-'*20, 'ToDo-List python', '-'*20)
    
    for task in todo_list:
        c += 1
        check = '✔' if task[1] else ' '
        print(c, f'[{check}] {task[0]}')

    return None


# add task
def add(task_name, todo_list):

    todo_list.append([task_name, False])

    return None


# remove task
def remove(task_name, todo_list):

    flag = True # flag para verificar se o usuario digitou corretamente

    # caso o usuario digite o indice da task
    if task_name.isdigit():
        index = int(task_name) - 1
        todo_list.pop(index)
        flag = False
    # caso o usuario digite o nome da task
    elif isinstance(task_name, str):
        for i in todo_list:
            if task_name in i:
                todo_list.remove(i)
                flag = False
                break
            else:
                continue
    if flag:
        print('Erro digite o indice ou o nome de uma tarefa existente.')
        os.system('pause')

    return None


# remove todos os itens da lista
def clearall(todo_list):
    todo_list.clear()
    os.system('cls')
    print('Itens removidos com sucesso.')
    os.system('pause')
    return None


# update task
def update(task_name, todo_list):

    flag = True # flag para verificar se o usuario digitou corretamente

    # caso o usuario digite o indice da task
    if task_name.isdigit():
        index = int(task_name) - 1
        if todo_list[index][1] == False:
            todo_list[index][1] = True
            flag = False
        else:
            todo_list[index][1] = False
            flag = False
    # caso o usuario digite o nome da task
    elif isinstance(task_name, str):
        for i in todo_list:
            if task_name in i:
                if i[1] == False:
                    i[1] = True
                    flag = False
                    break
                else:
                    i[1] = False
                    flag = False
                    break
    
    if flag:
        print('Erro digite o indice ou o nome de uma tarefa existente.')
        os.system('pause')

    return None


# help
def ihelp():
    print(
'''

    -adicionar uma tarefa:
        add <nome da tarefa>

    -remover uma tarefa:
        remove <nome da tarefa> 
        ou 
        remove <indice da tarefa>

    -atualizar uma tarefa:
        update <nome da tarefa> 
        ou 
        remove <indice da tarefa>

    -Remover todos os itens:
        clearall

    -Ler um arquivo todolist:
        read <path do arquivo>
    
    -Salvar um arquivo todolist feito:
        save

''')
    input('Aperte enter para continuar')


def save(todo_list):
    new_todo_list = [[i, j + '\n'] for i, j in todo_list]
    file = open('todolist1.txt', 'w')

    for i, j in new_todo_list:
        file.writelines(f'{i}, {j}')


def read(file_path):
    todo_list = []

    file = open(file_path, 'r')

    for i in file:
    
        line = i
        child_list = line.split(',')
        child_list[1] = child_list[1].replace('\n', '').replace(' ', '')
    
        if child_list[1] == 'False':
            child_list[1] = False
        else:
            child_list[1] = True

        todo_list.append(child_list)

    return todo_list


def quit():
    exit()
