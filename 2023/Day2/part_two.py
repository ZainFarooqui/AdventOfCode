from helpers import read_file_to_list, format_games

FILE_PATH =  'input.txt'

def find_power(cube_counts):
    result = 1
    has_non_zero = False
 
    for count in cube_counts.values():
        if count != 0:
            has_non_zero = True
            result *= count

    if not has_non_zero:
        return 0

    return result

def sum_powers(all_game):
    result = 0

    for game_rounds in all_game.values():
        fewest_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for each_round in game_rounds:
            all_cubes = each_round.split(',')
            for cube in all_cubes:
                count, colour = cube.split()
                count = int(count)
                if fewest_cubes[colour] < count:
                    fewest_cubes[colour] = count

        power = find_power(fewest_cubes)
        result += power

    return result

if __name__ == "__main__":
    raw_games = read_file_to_list(FILE_PATH)
    games = format_games(raw_games)
    total_sum = sum_powers(games)
    print(total_sum)
