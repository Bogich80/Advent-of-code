import re

file_path = r"C:\Users\bogna\PycharmProjects\Advent-of-code\3\3.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

sum_of_numbers = 0
row_data = re.findall(r'mul\(\d{1,3},\d{1,3}\)', file_content)
for row in row_data:
    numbers = re.findall(r'\d+', row)
    sum_of_numbers += int(numbers[0]) * int(numbers[1])
print(sum_of_numbers)
