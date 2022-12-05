import copy
import re

with open('python/05/05_input_stack.txt', 'r') as file:
    lines = file.readlines()
    stacks = {}
    length = len(lines.pop().split())
    [stacks.setdefault(i + 1, []) for i in range(length)]
    
    for line in lines:
        for i, val in enumerate(line[1::4]):
            if val != ' ':
                stacks[i+1].append(val)
                
    [stacks[i + 1].reverse() for i in range(length)]
    stacks_2 = copy.deepcopy(stacks)
                
with open('python/05/05_input.txt', 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        if line.strip() == "":
            continue
        
        numbers = [int(s) for s in re.findall(r'\d+', line)]
        
        # Part 1  
        for i in range(0, numbers[0]):
            stacks[numbers[2]].append(stacks[numbers[1]].pop())
            
        # Part 2
        stacks_2[numbers[2]].extend(stacks_2[numbers[1]][-numbers[0]:])
        stacks_2[numbers[1]] = stacks_2[numbers[1]][:-numbers[0]]

print(f'{stacks[1][-1]}{stacks[2][-1]}{stacks[3][-1]}{stacks[4][-1]}{stacks[5][-1]}\
    {stacks[6][-1]}{stacks[7][-1]}{stacks[8][-1]}{stacks[9][-1]}')
print(f'{stacks_2[1][-1]}{stacks_2[2][-1]}{stacks_2[3][-1]}{stacks_2[4][-1]}\
    {stacks_2[5][-1]}{stacks_2[6][-1]}{stacks_2[7][-1]}{stacks_2[8][-1]}{stacks_2[9][-1]}')