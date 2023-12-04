import math

FILE_PATH = 'input.txt'

def read_files(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

class Schematic:
    def __init__(self, input_schematic):
        self.schematic = input_schematic
        self.cache = set()
        self.n = len(input_schematic)
        self.m = len(input_schematic[0])
        self.sum_of_parts = 0
        self.gear_ratio = 0

    def __search_coord(self, x, y):
        x1 = x - 1
        x2 = x + 1
        part_number = self.schematic[y][x]

        while x1 >= 0 and self.schematic[y][x1].isdigit():
            part_number = self.schematic[y][x1] + part_number
            x1 -= 1

        while x2 < self.m and self.schematic[y][x2].isdigit(): 
            part_number = part_number + self.schematic[y][x2]
            x2 += 1

        x1 += 1
        x2 -= 1

        if (x1, x2, y) in self.cache:
            return -1
        else:
            self.cache.add((x1, x2, y))
            return int(part_number)

    def __find_adjacent_numbers(self, i, j):
        adjacent_numbers = []
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if -1 < x < self.m and -1 < y < self.n and self.schematic[y][x].isdigit():
                    part_number = self.__search_coord(x, y)
                    if part_number != -1:
                        adjacent_numbers.append(part_number)
        return adjacent_numbers

    def search_schematic(self):
        n = self.n
        m = self.m

        for y in range(n):
            for x in range(m):
                curr_char = self.schematic[y][x]
                if (not curr_char.isdigit() and curr_char != '.'):
                    extension = self.__find_adjacent_numbers(x, y)
                    self.sum_of_parts += sum(extension)
                    if curr_char == '*' and len(extension) == 2:
                        self.gear_ratio += math.prod(extension)

if __name__ == "__main__":
    data = read_files(FILE_PATH)
    schematic = Schematic(data)
    schematic.search_schematic()

    print(f'The sum of all part numbers is: {schematic.sum_of_parts}')
    print(f'The gear ratio is: {schematic.gear_ratio}')
