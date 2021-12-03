fhand = open('Day 03.txt')

numbers = [line.rstrip() for line in fhand]
bits_on_positions = list(zip(*numbers))

# Part One
gamma_rate = ''
epsilon_rate = ''
for bits in bits_on_positions:
    most_common_bit = max(bits, key=bits.count)
    gamma_rate += most_common_bit
    least_common_bit = min(bits, key=bits.count)
    epsilon_rate += least_common_bit

print(int(gamma_rate, 2) * int(epsilon_rate, 2))