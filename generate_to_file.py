import json
import os
from dh_generator import generate_dh_parameters

filename = input('Filename: ')
iterations = int(input('Iterations: '))
for i in range(iterations):
    print(f'\n{i + 1}/{iterations}')
    parameters = generate_dh_parameters()
    print(parameters)
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump({'parameters': []}, file, indent=4)
    with open(filename, 'r') as file:
        data = json.load(file)
    with open(filename, 'w') as file:
        data['parameters'].append(parameters)
        json.dump(data, file, indent=4)
input('\nPress Enter to exit')
