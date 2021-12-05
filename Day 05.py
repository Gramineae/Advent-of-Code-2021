from collections import Counter
import re

fhand = open('Day 05.txt')
slines = [re.split(r'\W+', l.rstrip()) for l in fhand]
lines = [[int(s) for s in sline] for sline in slines]
coordinates = Counter() # points that all the lines go through

for line in lines:
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    if x1 == x2:    
        points = [(x1, y) for y in range(min(y1, y2), max(y1, y2)+1)] # points of the line
        coordinates += Counter(points)
    elif y1 == y2:
        points = [(x, y1) for x in range(min(x1, x2), max(x1, x2)+1)]
        coordinates += Counter(points)
    # Part Two
    elif (x1<x2) & (y1<y2):
        points = [(x1+i, y1+i) for i in range(x2-x1+1)]
        coordinates += Counter(points)
    elif (x1<x2) & (y1>y2):
        points = [(x1+i, y1-i) for i in range(x2-x1+1)]
        coordinates += Counter(points)
    elif (x1>x2) & (y1>y2):
        points = [(x1-i, y1-i) for i in range(x1-x2+1)]
        coordinates += Counter(points)
    elif (x1>x2) & (y1<y2):
        points = [(x1-i, y1+i) for i in range(x1-x2+1)]
        coordinates += Counter(points)

count = 0
for value in coordinates.values():
    if value >= 2:
        count += 1

print(count)   
