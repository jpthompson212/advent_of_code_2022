def check_unique(values):
    if len(values) > len(set(values)):
        return False
    return True

with open('python/06/06_input.txt', 'r') as file:
    lines = file.readlines()

# Part 1
    for line in lines:
        last_4 = []
        for index, character in enumerate(line):
            if len(last_4) < 4:
                last_4.append(character)
            else:
                last_4.pop(0)
                last_4.append(character)
                if check_unique(last_4):
                    answer = index + 1
                    print(answer)
                    break

with open('python/06/06_input.txt', 'r') as file:
    lines = file.readlines()
# Part 2
    for line in lines:
        last_14 = []
        for index, character in enumerate(line):
            if len(last_14) < 14:
                last_14.append(character)
            else:
                last_14.pop(0)
                last_14.append(character)
                if check_unique(last_14):
                    answer = index + 1
                    print(answer)
                    break
