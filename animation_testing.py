import random

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

def bogosort(my_list: list[int]) -> list[list[int]]:
    history: list[list[int]] = [[]]
    for item in my_list:
        history[0].append(item)
    while(not is_sorted(my_list)):
        shuffle(my_list)
        history.append([])
        for item in my_list:
            history[-1].append(item)
    return history