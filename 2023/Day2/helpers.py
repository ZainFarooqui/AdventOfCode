def read_file_to_list(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())
    file.close()

    return lines


def format_games(raw_data):
    output = {}
    for each in raw_data:
        game_instance, raw_game_results = each.split(':')
        game_id = int(game_instance.split()[1])

        game_results = raw_game_results.split(';')

        output[game_id] = game_results

    return output
