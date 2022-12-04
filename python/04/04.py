with open('python/04/04_input.txt', 'r') as file:
    lines = file.readlines()
    
    # Part 1
    fully_contained = 0
    for line in lines:
        sections = line.strip().split(',')
        first_elf = sections[0].split('-')
        second_elf = sections[1].split('-')
        
        if int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1]):
            fully_contained += 1
            continue
        if int(second_elf[0]) <= int(first_elf[0]) and int(second_elf[1]) >= int(first_elf[1]):
            fully_contained += 1
            continue
            
    print(fully_contained)
    
    # Part 2
    have_overlap = 0
    for line in lines:
        sections = line.strip().split(',')
        first_elf = sections[0].split('-')
        second_elf = sections[1].split('-')
        
        if int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[0]):
            have_overlap += 1
            continue
        if int(second_elf[0]) <= int(first_elf[0]) and int(second_elf[1]) >= int(first_elf[0]):
            have_overlap += 1
            continue
    print(have_overlap)