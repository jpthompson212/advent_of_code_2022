import math

# Part 1
with open('python/03/03_input.txt', 'r') as file:
    lines = file.readlines()
    
    overall_priority = 0
    matches = []
    for line in lines:
        length = len(line)
        first_half = line[0:math.floor(length/2)].strip()
        second_half = line[math.floor(length/2):].strip()

        line_matches = []
        for character in first_half:
            if second_half.find(character) > -1:
                if character not in line_matches:
                    line_matches.append(character)
        matches.extend(line_matches)

    for letter in matches:
        if letter.isupper():
            overall_priority += ord(letter) - 38
        else: 
            overall_priority += ord(letter) - 96

print(overall_priority)

# Part 2
with open('python/03/03_input.txt', 'r') as file:
    lines = file.readlines()
    
    groups = {}
    group_num = 0
    temp_list = []
    count = 0
    for line in lines:
        if count == 3:
            groups[group_num] = temp_list
            group_num += 1
            count = 1
            temp_list = []
            temp_list.append(line.strip())
        else:
            temp_list.append(line.strip())
            count += 1
    groups[group_num] = temp_list


    badges = []
    badge_priority = 0
    for group in groups.values():
        group_match = []
        for character in group[0]:
            if group[1].find(character) > -1 and group[2].find(character) > -1:
                if character not in group_match:
                    group_match.append(character)
        badges.extend(group_match)
    for letter in badges:
        if letter.isupper():
            badge_priority += ord(letter) - 38
        else: 
            badge_priority += ord(letter) - 96
        
print(badge_priority)