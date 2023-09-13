import functions

user_input = user_input_split = command = task_name = ''

# Armazena a entrada do usuario
user_input = str(input()).strip()
user_input_split = user_input.split(' ')

# Tira somente comando e guarda na variavel
command = user_input_split.pop(0)

# guarda na variavel o nome da task
task_name = ' '.join(user_input_split[:])
