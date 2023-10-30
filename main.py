import functions

def main():
    todo_list = []
    user_input = user_input_split = command = task_name = '' 
    
    selector_function = {
        'add': functions.add,
        'remove': functions.remove,
        'clearall': functions.clearall,
        'update': functions.update,
        'ihelp': functions.ihelp,
        'save': functions.save,
        'quit': functions.quit,
 
    }

    ERROR_MSG = [
        'Erro. comando digitado não existe. Qualquer duvida digite ihelp', 
        'Você não digitou nada, por favor digite um comando validol. Qualquer Duvida digite o comando o ihelp'
        ]

    while True:
        # mostra as tasks
        functions.view(todo_list)
        
        # Pega e separa o comando do usuario
        user_input = str(input()).strip()

        if user_input == '':
            print(ERROR_MSG[1])
            input('Digite enter para continuar')
            continue

        user_input_split = user_input.split(' ')
        command = user_input_split[0]
        task_name = ' '.join(user_input_split[1:])

        # executa a funcao que o usuario digitou como comando
        selected_function = selector_function.get(command)

        if selected_function:
            if command == 'clearall' or command == 'save':
                selected_function(todo_list)
            elif command == 'exit' or command == 'ihelp' or command == 'quit':
                selected_function()
            else:
                selected_function(task_name, todo_list)
        else:
            print(ERROR_MSG[0])
            input('Pressione Enter para continuar.')

if __name__ == "__main__":
    main()
