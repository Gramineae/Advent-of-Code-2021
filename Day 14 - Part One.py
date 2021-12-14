first, second = open('Day 14.txt').read().rstrip().split('\n\n')
template = list(first)
rules = dict()
for line in second.split('\n'):
    pair, res = line.split(' -> ')
    rules[pair] = res

# Part One
n = 1
while n <= 10:
    new_temp = []
    for i, s in enumerate(template[:-1]):
        new_temp.append(s)
        pair = s + template[i+1]
        if pair in rules.keys():
            new_temp.append(rules[pair])
    new_temp.append(template[-1])        
    template = new_temp
    n += 1

cnt = dict()
for s in template:
    cnt[s] = cnt.get(s, 0) + 1

most_common = max(cnt.values())
least_common = min(cnt.values())
print(most_common - least_common)