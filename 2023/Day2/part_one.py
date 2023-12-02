from helpers import read_file_to_list, format_games

FILE_PATH = 'input.txt'
CUBE_MAXES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def sum_valid_game_ids(all_games):
    result = 0

    for game_id, game_rounds in all_games.items():
        is_valid_game = True
        for each in game_rounds:
            all_cubes = each.split(',')
            for cube in all_cubes:
                count, colour = cube.split()
                if int(count) > CUBE_MAXES[colour]:
                    is_valid_game = False

        if is_valid_game:
            result += game_id

    return result

if __name__ == "__main__":
    raw_games = read_file_to_list(FILE_PATH)
    games = format_games(raw_games)
    game_id_sum = sum_valid_game_ids(games)
    print(game_id_sum)
