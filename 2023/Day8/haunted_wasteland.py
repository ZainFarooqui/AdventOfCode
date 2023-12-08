def read_file(file_path):
	data = []
	with open(file_path, 'r') as file:
		for line in file:
			data.append(line.strip())
	
	return data


def format_data(data):
	instructions = data[0]
	network = {}

	for node in data[2:]:
		network[node[0:3]] = (node[7:10], node[12:15])
	
	return instructions, network

def traverse_network(instructions, network):
	count = 0
	node = 'AAA'
	end_node = 'ZZZ'
	in_length = len(instructions)

	while node != end_node:
		curr = count % in_length
		direction = 0
		if instructions[curr] == 'R':
			direction = 1
		
		node = network[node][direction]		
		count += 1

	return count
		
FILE_PATH = 'input.txt'
data = read_file(FILE_PATH)
instructions, network = format_data(data)
steps = traverse_network(instructions, network)
print(steps)
