

import ast

file_name = 'values.txt'

def save_value(input_value, filename):
    with open(filename, 'w') as f:
        f.write(input_value)

def load_value(filename):
    with open(filename, 'r') as f:
        read = f.read()
    return read


try:
    values = ast.literal_eval(load_value(file_name))
    print('Loaded values:', values)
except:
    print('Creating a new file...')
    values = {}


while True:
    user_input = input('item / count / print? >> ')

    if user_input == 'count':
        values['count'] = input('How many >>')
        save_value(str(values), file_name)
        print('Current values:', values)

    elif user_input == 'item':
        values['item'] = input('What item >>')
        save_value(str(values), file_name)
        print('Current values:', values)

    elif user_input == 'print':
        print(values['count'], values['item'])

    else:
        print('Unknown command...')