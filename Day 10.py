from collections import Counter
import numpy as np

file = open('Day 10.txt')
mapping = {'(': ')',
           '[': ']',
           '{': '}',
           '<': '>'}
crpt = Counter() # list of all corrupted characters
scores = []
cmplt = [] # completion strings of an incomplete line

for line in file:
    left = []
    line = line.rstrip()
    flag = True
    for char in line:
        if char in '([{<':
            left.append(char)
        elif char in ')]}>':
            if char == mapping[left[-1]]:
                left.pop()
            else:
                crpt += Counter(char)
                flag = False
                break
    if flag:
        cmplt = [mapping[char] for char in reversed(left)]
        score = 0
        for c in cmplt:
            score *= 5
            if c == ')':
                score += 1
            elif c == ']':
                score += 2
            elif c == '}':
                score += 3
            elif c == '>':
                score += 4
        scores.append(score)
        
print(3*crpt[')'] + 57*crpt[']'] + 1197*crpt['}'] + 25137*crpt['>'])
print(np.median(scores))