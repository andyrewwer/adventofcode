import sys

file_name = 'input.csv' if len(sys.argv) < 2 else 'input-basic.csv'

data = []
with open(file_name) as file:
    count_1 = 0
    count_2 = 0
    m = []
    for row in file:
        if "|" in row:
            left,right = row.split("|")
            m.append((left.strip(),right.strip()))
        if "," in row:
            nums = row.split(",")
            valid = False
            swap_happened = False
            while valid == False:
                valid = True
                for i in range (0, len(nums)):
                    for j in range (0, len(nums)):
                        if i == j:
                            continue
                        if i > j:
                            if (nums[i].strip(),nums[j].strip()) in m:
                                nums[i], nums[j] = nums[j], nums[i]
                                valid = False
                                swap_happened = True
                        if i < j:
                            if (nums[j].strip(),nums[i].strip()) in m:
                                nums[i], nums[j] = nums[j], nums[i]
                                valid = False
                                swap_happened = True
                if valid and not swap_happened:
                    count_1 += int(nums[int((len(nums) - 1)/2)])
                if swap_happened and valid:
                    count_2 += int(nums[int((len(nums) - 1)/2)])
                
                        
    print('Part 1: The total sum is ' + str(count_1))
    print('Part 2: The total sum is ' + str(count_2))