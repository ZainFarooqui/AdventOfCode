import math

def read_file(file_path):
	data = []
	with open(file_path, 'r') as file:
		for line in file:
			data.append(line.strip())
	
	return data


def format_data(data):
	instructions = data[0]
	network = {}
	start_nodes = []

	for node in data[2:]:
		if node[2] == 'A':
			start_nodes.append(node[0:3])
		network[node[0:3]] = (node[7:10], node[12:15])
	
	return instructions, network, start_nodes

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

def traverse_multiple(instruction, network, start_nodes):
	cycles = []
	in_length = len(instructions)

	for node in start_nodes:
		steps = 0
		while node[2] != 'Z':
			direction = 0
			if instruction[steps % in_length] == 'R':
				direction = 1

			node = network[node][direction]
			steps += 1
		cycles.append(steps)
	
	return math.lcm(*cycles)
	
FILE_PATH = 'input.txt'
data = read_file(FILE_PATH)
instructions, network, start_nodes  = format_data(data)
steps = traverse_multiple(instructions, network, start_nodes)
print(steps)
