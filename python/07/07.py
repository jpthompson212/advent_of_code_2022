import pprint
import flatdict

def append_dict(dict, keys, values):
    for key in keys[:-1]:
        dict = dict.setdefault(key, {})
    dict[keys[-1]] = values

with open('python/07/07_input.txt', 'r') as file:
    lines = file.readlines()

    directory_structure = {}
    init = False
    list_dir = False
    for line in lines:
        cmd_output = line.split()
        if cmd_output[0] == '$':
            if cmd_output[1] == 'cd':
                if list_dir:
                    if not init:
                        directory_structure['/'] = current_dir_list
                        init = True
                    else:
                        append_dict(directory_structure, current_dir, current_dir_list)

                if cmd_output[2] == '/':
                    current_dir = ['/']
                elif cmd_output[2] == '..':
                    current_dir.pop()
                else:
                    current_dir.append(cmd_output[2])

                list_dir = False
            if cmd_output[1] == 'ls':
                list_dir = True
                current_dir_list = {}
        elif cmd_output[0] == 'dir':
            current_dir_list[cmd_output[1]] = {}
            if not current_dir_list.get('files'):
                current_dir_list['files'] = []
                current_dir_list['size'] = 0
        else:
            if not current_dir_list.get('files'):
                current_dir_list['files'] = []
                current_dir_list['size'] = 0
            current_dir_list['files'].append((cmd_output[0], cmd_output[1]))
            current_dir_list['size'] += int(cmd_output[0])
    append_dict(directory_structure, current_dir, current_dir_list)

size = {}
flattened = flatdict.FlatDict(directory_structure, '.')

for key, value in flattened.items():
    string_key = str(key).split('.')
    if string_key[-1] == 'size':
        for i, item in enumerate(string_key):
            if item == 'size':
                break
            new_key = ''.join(map(str,string_key[:-(i+1)]))
            if not size.get(new_key):
                size[new_key] = 0
            size[new_key] += value

overall = 0
over_size = []

max_size = 70_000_000
size_needed = 30_000_000
current_available = max_size - size['/']
directory_size_to_delete = size_needed - current_available

for key, value in size.items():
    # Part 1
    if value < 100_000:
        overall += value

    # Part 2
    if value > directory_size_to_delete:
        print(key, value)
        over_size.append(value)

print(f'Part 1: {overall}')
print(f'Part 2: {min(over_size)}')
