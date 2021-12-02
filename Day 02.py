fhand = open('Day 02.txt')
x = 0
y = 0

# Part One
# for line in fhand:
#     ins, distance = line.split()
#     distance = int(distance)
#     if ins == 'forward':
#         x += distance
#     elif ins == 'up':
#         y += distance
#     elif ins == 'down':
#         y -= distance

# print(abs(x * y))

# Part Two
aim = 0
for line in fhand:
    ins, distance = line.split()
    distance = int(distance)
    if ins == 'down':
        aim += distance
    elif ins == 'up':
        aim -= distance
    elif ins == 'forward':
        x += distance
        y += abs(aim * distance)

print(x * y)
    
    