calories_per_elf = {}
elf_counter = 1
temp_val = 0

# Part 1
with open('python/01/01_input.txt', 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        if not line.strip():
            calories_per_elf[f'elf{elf_counter}'] = temp_val
            temp_val = 0
            elf_counter = elf_counter + 1
        else:
            temp_val = temp_val + int(line)
    calories_per_elf[f'elf{elf_counter}'] = temp_val

print(f'Max calories: {max(calories_per_elf.values())}')

# Part 2
calories_per_elf_top = sorted(calories_per_elf, key=calories_per_elf.get, reverse=True)[:3]
print(f'Top 3 calories summed: \
    {calories_per_elf[calories_per_elf_top[0]] + calories_per_elf[calories_per_elf_top[1]] + calories_per_elf[calories_per_elf_top[2]]}')