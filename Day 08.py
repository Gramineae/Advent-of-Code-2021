file = open('Day 08.txt')
from collections import defaultdict

# Part One
# output = [line.rstrip().split(' | ')[1] for line in file]
# values = []
# for o in output:
#     values.extend(o.split())

# counter = list(map(len, values))
# ones = counter.count(2)
# fours = counter.count(4)
# sevens = counter.count(3)
# eights = counter.count(7)
# print(ones + fours + sevens + eights)

# Part Two
lines = [line.rstrip().split() for line in file]
output = []

for line in lines:
    line.remove('|')
    connection = dict()
    widths = defaultdict(list)
    for signal in line[:10]:
        widths[len(signal)].append(signal)
    connection[1] = set(widths[2][0])
    connection[4] = set(widths[4][0])
    connection[7] = set(widths[3][0])
    connection[8] = set(widths[7][0])
    for w in widths[5]:
        if len(set(w) & (connection[4])) == 2:
            connection[2]= set(w)
        elif len(set(w) & (connection[7])) == 3:
            connection[3] = set(w)
        else:
            connection[5] = set(w)
    for w in widths[6]:
        if len(set(w) & (connection[3])) == 5:
            connection[9]= set(w)
        elif len(set(w) & (connection[5])) == 4:
            connection[0] = set(w)
        else:
            connection[6] = set(w)
    number = ''
    for value in line[10:]:
        value = set(value)
        for digit, signal in connection.items():
            if value == signal:
                number += str(digit)
                break
    output.append(int(number))
    
print(sum(output))