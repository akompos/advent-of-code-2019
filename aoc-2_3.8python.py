import math
module = 1969
running_sum = 0

while (module := module // 3 - 2) > 0:
    module = module // 3 - 2
    running_sum += module
    #print(running_sum)

print(running_sum)
