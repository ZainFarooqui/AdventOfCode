DIGITS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def read_file(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())
    file.close()

    return lines

def decoded_value(calibration):
    first = None
    last = None
    decoded = None

    for i, c in enumerate(calibration):
        if c.isnumeric():
            if not first:
                first = c
            last = c
        else:
            for key, value in DIGITS.items():
                if calibration[i:].startswith(key):
                    if not first:
                        first = value
                    last = value

    if first and last:
        decoded = first + last

    return decoded

def process_calibrations(encoded):
    true_values = []
    for calibration in encoded:
        decoded = decoded_value(calibration)
        true_values.append(decoded)

    return true_values

def sum_values(values):
    total_value = 0
    for val in values:
        total_value += int(val)

    return total_value

if __name__ == "__main__":
    FILE_PATH = 'day_1_input.txt'
    calibrations = read_file(FILE_PATH)
    decoded_values = process_calibrations(calibrations)
    sum_all = sum_values(decoded_values)

    print(sum_all)
