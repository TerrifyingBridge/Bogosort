import math
import random
import statistics
import matplotlib.pyplot as plt

plotting: bool = False
sim_length: int = 1000
max_list_length: int = 7
bogo_data: list[list[int]] = []

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

def bogosort(my_list: list[int]) -> int:
    counter: int = 0
    while(not is_sorted(my_list)):
        shuffle(my_list)
        counter += len(my_list)
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
        bogo_data.append([])
        pos.append(i + 1)
        expected_time.append((i + 1) * math.factorial(i + 1))
        for j in range(sim_length):
            unsorted_array = create_rng_array(i + 1)
            bogo_data[i].append(bogosort(unsorted_array))
    fig, ax = plt.subplots(figsize=(8,5))
    box = ax.boxplot(bogo_data, positions=pos)

    ax.plot(pos, expected_time)
    ax.set_yscale("log")
    plt.show()
else:
    temp_arr = create_rng_array(9)
    print(bogosort(temp_arr))