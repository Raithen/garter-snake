import math

def paintArea(length, width):
    coverage = 25
    area = length * width
    cans = math.ceil(area / coverage)
    print(f'Your paint area is {area} Sq.Ft. so you will need {cans} of paint.')

length = int(input('What is the length of your room?'))
width = int(input('What is the width of your room?'))
paintArea(length,width)