import re
import numpy as np

data_file = open(r"C:\Users\Bogich\PycharmProjects\Advent-of-code\2\2.txt", "r")
data_lines = np.array(data_file.readlines())
safe_patterns = 0


def is_pattern_safe(patterns):
    global safe_patterns
    inner_list = patterns
    previous_pattern = "@"
    plus_count = 0
    minus_count = 0
    for pattern in inner_list:
        if previous_pattern == "@":
            previous_pattern = pattern
        else:
            x = int(pattern) - int(previous_pattern)
            if 3 >= x >= 1:
                previous_pattern = pattern
            else:
                plus_count += 1

    previous_pattern = "@"
    for pattern in patterns:
        if previous_pattern == "@":
            previous_pattern = pattern
        else:
            y = int(previous_pattern) - int(pattern)
            if 3 >= y >= 1:
                previous_pattern = pattern
            else:
                minus_count += 1

    if plus_count < 2 or minus_count < 2:
        safe_patterns += 1
    print(patterns)
    print(minus_count)
    print(plus_count)

for row in data_lines:
    row_data = re.findall(r'\d+', row)
    is_pattern_safe(row_data)

print(safe_patterns)
