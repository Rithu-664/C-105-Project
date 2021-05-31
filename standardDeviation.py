import csv
from numpy import sqrt

total_entries = 0
total_numbers = 0

with open("C:/Users/JAYASANKAR/Desktop/Python/C-105/data.csv",newline='') as f:
    reader = csv.reader(f)
    new_list = list(reader)

total_entries = len(new_list[0])
for num in new_list:
    for p in num:
        total_numbers = total_numbers + float(p)

mean = total_numbers / total_entries
print(mean)

squared_list= []
for i in new_list:
    a = int(i[0]) - mean
    a = a * a
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum + i

result = sum / (len(new_list))

standardDeviation = sqrt(result)
print(standardDeviation)




