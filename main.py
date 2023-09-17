import functions

def main():
    todo_list = []
    user_input = user_input_split = ''
    command = task_name = '' 

    while True:
        # Mostra na tela todas as task adicionadas
        functions.view(todo_list)
        
        # Armazena a entrada do usuario
        user_input = str(input()).strip()
        user_input_split = user_input.split(' ')

        # Tira somente comando e guarda na variavel
        command = user_input_split.pop(0)

        # guarda na variavel o nome da task
        task_name = ' '.join(user_input_split[:])

        # seleciona o comando desejado pelo usuario
        if command == 'add':
            functions.add(task_name, todo_list)
        elif command == 'remove':
            functions.remove(task_name, todo_list)
        elif command == 'clearall':
            functions.clearall(todo_list)
        elif command == 'update':
            functions.update(task_name, todo_list)
        elif command == 'ihelp':
            functions.ihelp()
        elif command == 'exit':
            break
        else:
            print('Erro. comando não indentificado!')
            print('Duvidas digite o comando ihelp.')
            input('aperte enter para continuar.')

    print('programa finalizado.')
    return None


if __name__ == "__main__":
    main()