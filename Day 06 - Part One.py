file = open('Day 06.txt').read()
numbers = [int(n) for n in file.rstrip().split(',')]

# Part One 
n = 1
while n<=80:
    appendant = []
    if 0 in numbers:
        appendant = [8] * (numbers.count(0))
    numbers = [n-1 if n != 0 else 6 for n in numbers]
    numbers.extend(appendant)
    n += 1

print(len(numbers))