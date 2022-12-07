import pprint
below_100000 = []
accounted_for = []
def append_dict(dict, keys, values):
    for key in keys[:-1]:
        dict = dict.setdefault(key, {})
    dict[keys[-1]] = values


with open('python/07/07_example.txt', 'r') as file:
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
            current_dir_list['size'] = current_dir_list['size'] + int(cmd_output[0])
    append_dict(directory_structure, current_dir, current_dir_list)
            
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(directory_structure)

size = {}

def walk_dictionary(node):
    for key, item in node.items():
        temp_size = 0
        if isinstance(item, dict):
            print(item)
            temp_size += item.get('size')
            temp_size += walk_dictionary(item)
    return temp_size
            #if size < 100000 and size > 0 and key != 'files' and key != 'size':
            #    accounted_for.append(key)
            #    below_100000.append(size)

def sum_elements(element):
    if isinstance(element, dict):
        walk_dictionary(element)
        sum_elements(element)
        
size['/'] = walk_dictionary(directory_structure)
sum_elements(directory_structure)
print(size)            

overall = 0
for key, value in size.items():
    if value < 100000:
        overall += value
print(f'ughhh: {overall}')
