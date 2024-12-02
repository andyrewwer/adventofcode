import csv
import sys
import re
   
file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as file:
    data = file.read().splitlines()
    _sum = 0
    for row in data:
        first_half = row.split('|')[0].split()
        second_half = row.split('|')[1].split()

        solved = False
        candidates = {'a': 'abcdefg', 'b': 'abcfedg', 'c': 'abcdefg', 'd': 'abcdefg', 'e': 'abcdefg', 'f': 'abcdefg', 'g': 'abcdefg'}
        confirmed_letters = ''
        
        one = ''
        seven = ''
        four = ''
        three = ''
        five = ''
        while not solved:
            if len(candidates['c']) > 2:
                for digit in first_half:
                    if len(digit) == 2:
                        candidates['c'] = digit
                        candidates['f'] = digit
                        one = set(digit)
                        if seven != '':
                            diff = list(one ^ seven)[0]
                            candidates['a'] = diff
                            confirmed_letters = confirmed_letters + candidates['a']

                            break
                    elif len(digit) == 3:
                        seven = set(digit)
                        if one != '':
                            diff = list(one ^ seven)[0]
                            candidates['a'] = diff
                            confirmed_letters = confirmed_letters + candidates['a']
                            break

            if len(candidates['b']) > 2:
                for digit in first_half:
                    if len(digit) == 4:
                        four = set(digit)
                        diff = list(one ^ four)
                        diff = diff[0] + diff[1]
                        candidates['b'] = diff
                        candidates['d'] = diff
            
            if len(five) < 5:
                for digit in first_half:
                    if len(digit) == 5:
                        diff = ''
                        for c in digit:
                            if c not in one:
                                diff = diff + c
                        if len(diff) == 3:
                            three = set(digit)
                            _diff = seven ^ three
                            candidates['d'] = list(_diff & four)[0]
                            candidates['g'] = list(_diff ^ set(candidates['d']))[0]
                            confirmed_letters = confirmed_letters + candidates['d']
                            confirmed_letters = confirmed_letters + candidates['g']
                            if five != '':
                                hack_to_get_b = list(five)
                                hack_to_get_b.append(candidates['c'])
                                candidates['b'] = list(set(hack_to_get_b) ^ three)[0]
                                confirmed_letters = confirmed_letters + candidates['b']
                                solved = True
                                break
                            continue
                            #toBeThrowIntoHelperFunctionMaybe

                        #check if 2 or 5
                        if len(diff) == 4:
                            _diff = ''
                            for c in diff:
                                if c not in four:
                                    _diff = _diff + c
                            #check if 5, trust me. 5-4=2.
                            if len(_diff) == 2:
                                five = set(digit)
                                for ch in _diff:
                                    if ch not in seven:
                                        candidates['g'] = ch
                                candidates['f'] = list(one & five)[0]
                                candidates['c'] = list(set(candidates['f']) ^ one)[0]
                                confirmed_letters = confirmed_letters + candidates['f']
                                confirmed_letters = confirmed_letters + candidates['c']
                                if three != '':
                                    hack_to_get_b = list(five)
                                    hack_to_get_b.append(candidates['c'])
                                    candidates['b'] = list(set(hack_to_get_b) ^ three)[0]
                                    confirmed_letters = confirmed_letters + candidates['b']
                                    solved = True
                                    break
        # set G
        pattern = r'[' + confirmed_letters + ']'
        candidates['e'] = re.sub(pattern, '', candidates['e'])

        #1,3,4,5,7 are now set
        #now to find, 0, 2, 6, 8, 9
        zero = ''
        two = ''
        six = ''
        eight = ''
        nine = ''
        print(candidates)
        for digit in first_half:
            if len(digit) == 5:
                if len(five & set(digit)) != 5 and len (three & set(digit)) != 5:
                    two = set(digit)
            if len(digit) == 7:
                eight = set(digit)
            if len(digit) == 6:
                if candidates['d'] not in digit:
                    zero = set(digit)
                if candidates['c'] not in digit:
                    six = set(digit)
                if candidates['e'] not in digit:
                    nine = set(digit)

        number = ''
        for digit in second_half:
            if zero == set(digit):
                number = number + '0'
                continue
            if one == set(digit):
                number = number + '1'
                continue
            if two == set(digit):
                number = number + '2'
                continue
            if three == set(digit):
                number = number + '3'
                continue
            if four == set(digit):
                number = number + '4'
                continue
            if five == set(digit):
                number = number + '5'
                continue
            if six == set(digit):
                number = number + '6'
                continue
            if seven == set(digit):
                number = number + '7'
                continue
            if eight == set(digit):
                number = number + '8'
                continue
            if nine == set(digit):
                number = number + '9'
                continue
        print('number', number, int(number))
        _sum = _sum + int(number)

    print(_sum)
