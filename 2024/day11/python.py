import sys, time

file_name = 'input.csv' if len(sys.argv) < 2 else 'input-basic.csv'
nums = {}
with open(file_name, "r") as file:
  content = file.readlines()
  for y, line in enumerate(content):
      line = line.strip()
      for x, el in enumerate(line.split(' ')):
            nums[el] = 1
            
# number_of_days = 6
number_of_days = 75
for blink in range (1,1+number_of_days):
    new_nums = {}
    for num in nums.keys():
        if num == '0':
            if '1' not in new_nums:
                new_nums['1'] = 0
            new_nums['1'] += nums['0']
        elif len(num) % 2 == 0:
            mid_mark = len(num) // 2
            new_first = str(int(num[:mid_mark]))
            new_second = str(int(num[mid_mark:]))

            if new_first not in new_nums:
                new_nums[new_first] = 0
            new_nums[new_first] += nums[num]

            if new_second not in new_nums:
                new_nums[new_second] = 0
            new_nums[new_second] += nums[num]
        else:
            new_num = str(int(num) * 2024)
            if new_num not in new_nums:
                new_nums[new_num] = 0 
            new_nums[new_num] += nums[num]
    nums = new_nums

sum = 0
for key in nums:
    sum += nums[key]

print(sum)