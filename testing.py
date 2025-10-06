import random
from numpy.ma.extras import average

list_size: int = 4
sim_length: int = 10000
arr: list[int] = []

def is_sorted(my_list: list[int]) -> bool:
    for i in range(1, len(my_list)):
        if (my_list[i] < my_list[i - 1]):
            return False
    return True

def shuffle(my_list: list[int]):
    length: int = len(my_list)
    for i in range(0, length):
        random_int: int = random.randint(0, length-1)
        temp_val: int = my_list[i]
        my_list[i] = my_list[random_int]
        my_list[random_int] = temp_val

def bogosort(my_list: list[int]) -> int:
    counter: int = 0
    while(not is_sorted(my_list)):
        shuffle(my_list)
        counter += 1
    return counter

data_arr = []
for sim in range(sim_length):
    arr = []
    for num in range(list_size):
        arr.append(num)
    shuffle(arr)
    data_arr.append(bogosort(arr))

print(data_arr)
print(average(data_arr), min(data_arr), max(data_arr))