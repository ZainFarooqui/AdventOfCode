def read_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    
    stripped_lines = [line for line in lines if line != '']
    return stripped_lines

def format_data(data):
    output = {}
    seeds = data[0].split(':')[1].split()
    output['seeds'] = [int(seed) for seed in seeds]
    curr_key = ''

    for line in data[1:]:
        try:
            mappings_list = line.split()
            mapping = [int(num) for num in mappings_list]
            output[curr_key].append(mapping)
        except:
            curr_key = line
            output[curr_key] = []
    return output

def get_mapping(rules):
    mapping = {}
    
    for rule in rules:
        destination = rule[0]
        source = rule[1]
        range_length = rule[2] - 1
        
        mapping[(source, source + range_length)] = destination

    return mapping

def apply_conversion(prev, mapping):
    converted = []

    for e in prev:
        new_val = e
        for source, destination in mapping.items():
            if source[0] <= e <= source[1]:
                delta = e - source[0]
                new_val = destination + delta
        
        converted.append(new_val)
                
    return converted

def process_mappings(almanac):
    conversions = almanac['seeds']
    almanac.pop('seeds')
    
    for rules in almanac.values():
        mapping = get_mapping(rules)
        conversions = apply_conversion(conversions, mapping)
    
    return conversions
    
def process_mappings_part_two(almanac): 
    temp = almanac['seeds']
    almanac.pop('seeds')
    
    conversions = []
    for i in range(0, len(temp),2):
        print('hello')
        seeds = []
        for j in range(temp[i+1]):
            seeds.append(temp[i] + j)
        #seeds = [temp[i]+j for j in range(temp[i+1])]
        conversions.extend(seeds)

    for rules in almanac.values():
        mapping = get_mapping(rules)
        conversions = apply_conversion(conversions, mapping)
    
    return conversions

FILE_PATH = 'input.txt'
raw_data = read_file(FILE_PATH)
data = format_data(raw_data)
location = process_mappings_part_two(data)
print(min(location))