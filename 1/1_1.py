import numpy as np
import re
import math

data_file = open('data_1.txt', 'r')
data_lines = np.array(data_file.readlines())
first_column_data = []
second_colum_data = []
for row in data_lines:
    row_data = re.findall(r'\d+', row)
    first_column_data.append(int(row_data[0]))
    second_colum_data.append(int(row_data[1]))
first_column_data.sort()
second_colum_data.sort()
diff = 0
for i in range(len(first_column_data)):
    x = math.fabs(first_column_data[i] - second_colum_data[i])
    diff += x
print(diff)
