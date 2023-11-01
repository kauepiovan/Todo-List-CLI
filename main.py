import functions
import os 

def main():
    todo_list = []
    user_input = user_input_split = command = command_params = '' 
    
    selector_function = {
        'add': functions.add,
        'remove': functions.remove,
        'clearall': functions.clearall,
        'update': functions.update,
        'ihelp': functions.ihelp,
        'read': functions.read,
        'save': functions.save,
        'quit': functions.quit,
 
    }

    WARNINGS_MSG = [
        'Prosseguir com esta ação resultara na perda do todo-list atual caso nao tenha salvado, deseja continuar? [yes/no]'
    ]

    ERROR_MSG = [
        'Erro. comando digitado não existe. Qualquer duvida digite ihelp', 
        'Você não digitou nada, por favor digite um comando validol. Qualquer Duvida digite o comando o ihelp'
        'ERRO INESPERADO!'
        ]

    while True:
        # mostra as tasks
        functions.view(todo_list)
        
        # Pega e separa o comando do usuario
        user_input = str(input()).strip()

        if user_input == '':
            print(ERROR_MSG[1])
            os.system('pause')
            continue

        user_input_split = user_input.split(' ')
        command = user_input_split[0]
        command_params = ' '.join(user_input_split[1:])

        # executa a funcao que o usuario digitou como comando
        selected_function = selector_function.get(command)

        if selected_function:
            if command == 'clearall' or command == 'save':
                selected_function(todo_list)
            elif command == 'exit' or command == 'ihelp' or command == 'quit':
                selected_function()
            elif command == 'read':
                print(WARNINGS_MSG[0])
                flag = input().lower()
                if flag == 'yes':
                    todo_list = selected_function(command_params).copy()
                elif flag == 'no':
                    continue
                else:
                    print(ERROR_MSG[2])
            else:
                selected_function(command_params, todo_list)
        else:
            print(ERROR_MSG[0])
            os.system('pause')

if __name__ == "__main__":
    main()
