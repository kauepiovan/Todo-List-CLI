import os

# view task
def view(todo_list):
    os.system('cls')
    c = 0

    for task in todo_list:
        c += 1
        print(c, task[0])

    return None


# add task
def add(task_name, todo_list):

    todo_list.append([f'- [ ] {task_name}', False])

    return None


# remove task
def remove(task_name, todo_list):
    
    flag = True
    if task_name.isdigit():
        index = int(task_name) - 1
        todo_list.pop(index)
        flag = False

    elif isinstance(task_name, str):
        task_name = f'- [ ] {task_name}'
        for i in todo_list:
            if task_name in i:
                todo_list.remove(i)
                flag = False
                break
            else:
                continue
    if flag:
        print('Erro digite o indice ou o nome de uma tarefa existente.')
        input('Aperte enter para continuar.')      

    return None


# update task
def update():
    ...
# help
def help():
    ...