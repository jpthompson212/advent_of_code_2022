# Part 1
with open('python/02/02_input.txt', 'r') as file:
    lines = file.readlines()
    total_score = 0
    for line in lines:
        round = line.strip().split(' ')
        round_score = 0
        if round[0] == 'A':
            if round[1] == 'X':
                round_score = 3 + 1
            if round[1] == 'Y':
                round_score = 6 + 2
            if round[1] == 'Z':
                round_score = 0 + 3
        if round[0] == 'B':
            if round[1] == 'X':
                round_score = 0 + 1
            if round[1] == 'Y':
                round_score = 3 + 2
            if round[1] == 'Z':
                round_score = 6 + 3
        if round[0] == 'C':
            if round[1] == 'X':
                round_score = 6 + 1
            if round[1] == 'Y':
                round_score = 0 + 2
            if round[1] == 'Z':
                round_score = 3 + 3
        total_score += round_score
        
print(f'Total Score is: {total_score}')

# Part 2
with open('python/02/02_input.txt', 'r') as file:
    lines = file.readlines()
    total_score = 0
    for line in lines:
        round = line.strip().split(' ')
        round_score = 0
        if round[0] == 'A':
            if round[1] == 'X':
                round_score = 0 + 3
            if round[1] == 'Y':
                round_score = 3 + 1
            if round[1] == 'Z':
                round_score = 6 + 2
        if round[0] == 'B':
            if round[1] == 'X':
                round_score = 0 + 1
            if round[1] == 'Y':
                round_score = 3 + 2
            if round[1] == 'Z':
                round_score = 6 + 3
        if round[0] == 'C':
            if round[1] == 'X':
                round_score = 0 + 2
            if round[1] == 'Y':
                round_score = 3 + 3
            if round[1] == 'Z':
                round_score = 6 + 1
        total_score += round_score
        
print(f'Total Score is: {total_score}')

# Clean up by using dictionaries

# rock paper scisors
values = {'X': 1,
          'Y': 2,
          'Z': 3}

# lose draw win
values_part2 = {'X': 0,
                'Y': 3,
                'Z': 6}

result = {'AX': 3 + values['X'],
          'AY': 6 + values['Y'],
          'AZ': 0 + values['Z'],
          'BX': 0 + values['X'],
          'BY': 3 + values['Y'],
          'BZ': 6 + values['Z'],
          'CX': 6 + values['X'],
          'CY': 0 + values['Y'],
          'CZ': 3 + values['Z']}

result_part2 = {'AX': 3 + values_part2['X'],
                'AY': 1 + values_part2['Y'],
                'AZ': 2 + values_part2['Z'],
                'BX': 1 + values_part2['X'],
                'BY': 2 + values_part2['Y'],
                'BZ': 3 + values_part2['Z'],
                'CX': 2 + values_part2['X'],
                'CY': 3 + values_part2['Y'],
                'CZ': 1 + values_part2['Z']}

with open('python/02/02_input.txt', 'r') as file:
    lines = file.readlines()
    total_score = 0
    # Part 1
    for line in lines:
        round = line.strip().replace(' ', '')
        total_score += result[round]
    print(f'Total Score is: {total_score}')
    
    total_score = 0
    # Part 2
    for line in lines:
        round = line.strip().replace(' ', '')
        total_score += result_part2[round]
    print(f'Total Score is: {total_score}')