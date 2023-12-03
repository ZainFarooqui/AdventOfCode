FILE_PATH = 'input.txt'

def read_files(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

class PartNumbersCoordCache:
    def __init__(self):
        self.cache = set()
        
    def add(self, x1, x2, y):
        self.cache.add((x1, x2, y))
        
    def check_cache(self, x1, x2, y):
        return (x1, x2, y) in self.cache

class Schematic:
    def __init__(self, schematic):
        self.schematic = schematic
        self.cache = PartNumbersCoordCache()
        self.part_numbers = []
        self.n = len(schematic)
        self.m = len(schematic[0])
        self.symbols = set()
        self.any = set()
    
    def search_coord(self, x, y):
        x1 = x - 1
        x2 = x + 1
        part_number = self.schematic[y][x]
        
        while x1 > 0 and self.schematic[y][x1].isdigit():
            part_number = self.schematic[y][x1] + part_number
            x1 -= 1
        
        while x2 < self.m and self.schematic[y][x2].isdigit(): 
            part_number = part_number + self.schematic[y][x2]
            x2 += 1
        
        x1 += 1
        x2 -= 1
        if self.cache.check_cache(x1, x2, y):
            return -1
        else:
            self.cache.add(x1, x2, y)
            return int(part_number)
            
    def find_adjacent_numbers(self, i, j):
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if -1 < x < self.m and -1 < y < self.n and self.schematic[y][x].isdigit():
                    part_number = self.search_coord(x, y)
                    if part_number != -1:
                        self.part_numbers.append(part_number)

    def find_all_part_numbers(self):
        schematic = self.schematic
        n = self.n
        m = self.m
        
        for y in range(n):
            for x in range(m):
                curr_char = schematic[y][x]
                self.any.add(curr_char)
                if (not curr_char.isdigit() and curr_char != '.'):
                    self.symbols.add(curr_char)
                    self.find_adjacent_numbers(x, y)
                        
    
if __name__ == "__main__":
    data = read_files(FILE_PATH)
    schematic = Schematic(data)
    schematic.find_all_part_numbers()
    print(schematic.any)
    print(schematic.symbols)
    print(schematic.any.difference(schematic.symbols))