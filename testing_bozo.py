import math
import random
import matplotlib.pyplot as plt

plotting: bool = True
sim_length: int = 100
max_list_length: int = 8
bozo_data: list[list[int]] = []

def is_sorted(my_list: list[int]) -> bool:
    for k in range(1, len(my_list)):
        if (my_list[k] < my_list[k - 1]):
            return False
    return True

def shuffle(my_list: list[int]):
    length: int = len(my_list)
    for k in range(0, length - 1):
        random_int: int = random.randint(k, length-1)
        temp_val: int = my_list[k]
        my_list[k] = my_list[random_int]
        my_list[random_int] = temp_val

def random_swap(my_list: list[int]):
    length: int = len(my_list)
    random_index1: int = random.randint(0, length - 1)
    random_index2: int = random.randint(0, length - 1)
    while (random_index1 == random_index2):
        random_index2 = random.randint(0, length - 1)
    temp_val: int = my_list[random_index1]
    my_list[random_index1] = my_list[random_index2]
    my_list[random_index2] = temp_val

def bozosort(my_list: list[int]) -> int:
    counter: int = 0
    while(not is_sorted(my_list)):
        random_swap(my_list)
        counter += 1
    return counter

def create_rng_array(list_length: int) -> list[int]:
    temp_arr = []
    for k in range(list_length):
        temp_arr.append(k+1)
    while(is_sorted(temp_arr) and len(temp_arr) > 1):
        shuffle(temp_arr)
    return temp_arr

if (plotting):

    pos = []
    expected_time = []
    for i in range(max_list_length):
        bozo_data.append([])
        pos.append(i + 1)
        expected_time.append((i + 1) * math.factorial(i + 1))
        for j in range(sim_length):
            unsorted_array = create_rng_array(i + 1)
            bozo_data[i].append(bozosort(unsorted_array))

    for item in bozo_data:
        print(item)

    fig, ax = plt.subplots(figsize=(8,5))
    box = ax.boxplot(bozo_data, positions=pos)

    ax.plot(pos, expected_time)
    ax.set_yscale("log")
    plt.show()

else:
    length_data = []
    for i in range(sim_length):
        unsorted_array = create_rng_array(max_list_length)
        length_data.append(bozosort(unsorted_array))
    print(sum(length_data) / len(length_data))
