import sys
from collections import defaultdict
import math

data = sys.stdin.read().splitlines()

idx = 1
for _ in range(int(data[0])):
    num_cloth = int(data[idx])
    idx += 1
    cloth_dict = defaultdict(int)

    for i in range(num_cloth):
        cloth, category = data[idx].split()
        cloth_dict[category] += 1
        idx += 1
    
    result = math.prod([count + 1 for count in cloth_dict.values()]) - 1

    print(result)