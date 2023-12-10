
FILE_PATH = 'input.txt'

direction  = {
    'SOUTH': ('|', 'S', '7', 'F'),
    'NORTH': ('|', 'S', 'L', 'J'),
    'EAST': ('-', 'S', 'L', 'F'),
    'WEST': ('-', 'S', 'J', '7')
}

def read_file(file_path):
    raw_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            raw_data.append(line.strip())

    return raw_data

def find_start_idx(data):
    m = len(data[0])
    n = len(data)
    start = None

    for j in range(n):
        for i in range(m):
            if data[j][i] == 'S':
                start = (j , i, 'S')

    return (m, n , start)

def find_furthest_pipe(pipe_map):
    m, n, start = find_start_idx(pipe_map)
    new_map = [['.' for i in range(m)] for j in range(n)]

    fy = start[0]
    fx = start[1]
    new_map[fy][fx] = '0'

    queue = [start]
    next_queue = []
    max_val = 0
    while queue:
        curr = queue.pop()

        x = curr[1]
        y = curr[0]
        char = curr[2]

        if y-1 >= 0 and char in direction['NORTH'] and pipe_map[y-1][x] in direction['SOUTH'] and new_map[y-1][x] == '.':
            next_queue.append((y-1, x, pipe_map[y-1][x]))
            new_map[y-1][x] = str(max_val + 1)

        if y+1 < n and char in direction['SOUTH'] and pipe_map[y+1][x] in direction['NORTH'] and new_map[y+1][x] == '.':
            next_queue.append((y+1, x, pipe_map[y+1][x]))
            new_map[y+1][x] = str(max_val + 1)

        if x-1 >= 0 and char in direction['WEST'] and pipe_map[y][x-1] in direction['EAST'] and new_map[y][x-1] == '.':
            next_queue.append((y, x-1, pipe_map[y][x-1]))
            new_map[y][x-1] = str(max_val + 1)

        if x+1 < m and char in direction['EAST'] and pipe_map[y][x+1] in direction['WEST'] and new_map[y][x+1] == '.':
            next_queue.append((y, x+1, pipe_map[y][x+1]))
            new_map[y][x+1] = str(max_val + 1)

        if not queue:
            queue = next_queue
            next_queue = []
            max_val += 1

    for line in new_map:
        print(line)
        
    return max_val - 1

if __name__ == '__main__':
    data = read_file(FILE_PATH)
    furthest = find_furthest_pipe(data)
    print(furthest)
    