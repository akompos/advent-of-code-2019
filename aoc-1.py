running_sum = 0

with  open('inputs/aoc-1.txt', 'r') as file:
    for module in file:
        mass = int(module)
        fuel = mass // 3 - 2
        running_sum += fuel



print(running_sum)

