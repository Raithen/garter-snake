import math

heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0

for height in heights:
    total_height += height
avg_height = math.ceil(total_height / len(heights))
print(f'The Average height is {avg_height}')