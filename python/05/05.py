import pandas as pd
import re

hard_code = {1: ['W','R','F'],
             2: ['T','H','M','C','D','V','W','P'],
             3: ['P','M','Z','N','L'],
             4: ['J','C','H','R'],
             5: ['C','P','G','H','Q','T','B'],
             6: ['G','C','W','L','F','Z'],
             7: ['W','V','L','Q','Z','J','G','C'],
             8: ['P','N','R','F','W','T','V','C'],
             9: ['J','W','H','G','R','S','V']}

hard_code_2 = {1: ['W','R','F'],
             2: ['T','H','M','C','D','V','W','P'],
             3: ['P','M','Z','N','L'],
             4: ['J','C','H','R'],
             5: ['C','P','G','H','Q','T','B'],
             6: ['G','C','W','L','F','Z'],
             7: ['W','V','L','Q','Z','J','G','C'],
             8: ['P','N','R','F','W','T','V','C'],
             9: ['J','W','H','G','R','S','V']}

with open('python/05/05_input.txt', 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        if line.strip() == "":
            continue
        
        numbers = [int(s) for s in re.findall(r'\d+', line)]
        
        # Part 1
        for i in range(0, numbers[0]):
            hard_code[numbers[2]].append(hard_code[numbers[1]].pop())
            
        # Part 2
        hard_code_2[numbers[2]].extend(hard_code_2[numbers[1]][-numbers[0]:])
        hard_code_2[numbers[1]] = hard_code_2[numbers[1]][:-numbers[0]]

print(f'{hard_code[1][-1]}{hard_code[2][-1]}{hard_code[3][-1]}{hard_code[4][-1]}{hard_code[5][-1]}{hard_code[6][-1]}{hard_code[7][-1]}{hard_code[8][-1]}{hard_code[9][-1]}')
print(f'{hard_code_2[1][-1]}{hard_code_2[2][-1]}{hard_code_2[3][-1]}{hard_code_2[4][-1]}{hard_code_2[5][-1]}{hard_code_2[6][-1]}{hard_code_2[7][-1]}{hard_code_2[8][-1]}{hard_code_2[9][-1]}')