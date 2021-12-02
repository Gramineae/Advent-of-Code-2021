with open('Day 01.txt') as f:
    lines = f.readlines()

depths = [int(m.strip()) for m in lines]
count = 0

# Part One
for i, depth in enumerate(depths):
    if i == 0:
        continue
    if depth > depths[i-1]:
            count += 1
        
print(count)

# Part Two
# for i, depth in enumerate(depths[:-2]):
#     if i == 0:
#         previous = depth + depths[i+1] + depths[i+2]
#         continue
#     sum_of_three = depth + depths[i+1] + depths[i+2]
#     if sum_of_three > previous:
#         count += 1
#     previous = sum_of_three

# print(count)
    
    
    