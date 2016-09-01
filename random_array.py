import random

random_arr = []

for x in range(0, 100):
    random_num = random.randrange(0, 100)
    rounded_num = round(random_num)
    random_arr.append(rounded_num)

print(random_arr)