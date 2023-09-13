import os

# view task
def view(todo_list):
    os.system('cls')

    tasks_done = []
    tasks_peding = []

    # separas as tasks feitas das não feitas
    for task, status in todo_list:
        print(task)

        if status == True:
            tasks_done.append(task)
        else:
            tasks_peding.append(task)

    # print('Tarefas a fazer: ')
    # for task in tasks_peding:
    #     print(task)

    # print('Tarefas feitas: ')
    # for task in tasks_done:
    #     print(task)

    return None


# add task
def add(task_name, todo_list):

    todo_list.append((f' - [ ] {task_name}', False))

    return None


# remove task
def remove(task_name, todo_list):
    if task_name.isdigit():
        index = int(task_name) - 1
        todo_list.pop(index)

    elif isinstance(task_name, str):
        for i in todo_list:
            if task_name in i:
                todo_list.remove(i)
            else:
                continue
    
    return None


# update task
def update():
    ...
# help
def help():
    ...