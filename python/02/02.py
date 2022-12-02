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