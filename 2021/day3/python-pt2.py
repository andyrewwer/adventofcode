import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

def get_most_frequent_returns(data):
    zeros = []
    ones = []
    for i in range(len(data)):
        row = data[i][0]
        for j in range(len(row)):
            if len(zeros) == j :
                zeros.append(0)
                ones.append(0)
            if row[j] == '0':
                zeros[j] = zeros[j] + 1
            else:
                ones[j] = ones[j] + 1
    return zeros, ones

def get_most_common_for_position(zeros, ones, index):
    return '0' if zeros[index] > ones[index] else '1'

def get_oxygen_data(data, zeros, ones, pos):
    if len(data) == 1:
        return data[0][0]
    most_common = get_most_common_for_position(zeros,ones,pos)
    new_data = []
    for i in range(len(data)):
        if data[i][0][pos] == most_common:
            new_data.append(data[i])
    zeros,ones = get_most_frequent_returns(new_data)
    return get_oxygen_data(new_data,zeros,ones,pos+1)
    
def get_co2_scrubber_data(data, zeros, ones, pos):
    if len(data) == 1:
        return data[0][0]
    most_common = get_most_common_for_position(zeros,ones,pos)
    new_data = []
    for i in range(len(data)):
        if data[i][0][pos] != most_common:
            new_data.append(data[i])
    zeros,ones = get_most_frequent_returns(new_data)
    return get_co2_scrubber_data(new_data,zeros,ones,pos+1)
    

with open(file_name) as csv_file:
    data = list(csv.reader(csv_file))
    
    zeros,ones = get_most_frequent_returns(data)
    oxygen_data = get_oxygen_data(data,zeros,ones,0) 
    co2_data = get_co2_scrubber_data(data,zeros,ones,0)  
    print(oxygen_data, int(oxygen_data, 2))
    print(co2_data, int(co2_data, 2))
    print('result', int(oxygen_data, 2) * int(co2_data, 2))
