import pygame
import random

def clear_sorting_array():
    for i in range(len(arr_comparing)):
        arr_comparing[i] = False

def clear_order_array():
    for i in range(len(arr_in_order)):
        arr_in_order[i] = False

def is_sorted(my_list: list[int]) -> bool:
    for i in range(1, len(my_list)):
        clear_sorting_array()
        arr_comparing[i] = True
        arr_comparing[i - 1] = True
        render_bars()
        pygame.display.flip()
        pygame.time.delay(TIME_BUFFER)
        if (my_list[i] < my_list[i - 1]):
            clear_order_array()
            return False
        arr_in_order[i] = True
        arr_in_order[i - 1] = True
    return True

def shuffle(my_list: list[int]):
    length: int = len(my_list)
    for i in range(0, length):
        random_int: int = random.randint(0, length-1)
        temp_val: int = my_list[i]
        my_list[i] = my_list[random_int]
        my_list[random_int] = temp_val
        clear_sorting_array()
        arr_comparing[i] = True
        arr_comparing[i - 1] = True
        render_bars()
        pygame.display.flip()
        pygame.time.delay(TIME_BUFFER)

def bogosort(my_list: list[int]) -> int:
    counter: int = 0
    while(not is_sorted(my_list)):
        shuffle(my_list)
        counter += 1
    return counter

def render_bars():
    screen.fill("black")
    for i in range(len(arr)):
        temp_rect = pygame.Rect(BUFFER_WIDTH + RECTANGLE_WIDTH * i, BUFFER_HEIGHT + RECTANGLE_UNIT_HEIGHT * (len(arr) - arr[i]), RECTANGLE_WIDTH - 1, RECTANGLE_UNIT_HEIGHT * arr[i])
        if (arr_comparing[i]):
            pygame.draw.rect(screen, "Red", temp_rect)
        elif (arr_in_order[i]):
            pygame.draw.rect(screen, "Green", temp_rect)
        else:
            pygame.draw.rect(screen, "White", temp_rect)

WIDTH = 1280
HEIGHT = 720
SORTING_WIDTH = round(WIDTH * 0.8)
BUFFER_WIDTH = (WIDTH - SORTING_WIDTH) / 2
SORTING_HEIGHT = round(HEIGHT * 0.8)
BUFFER_HEIGHT = (HEIGHT - SORTING_HEIGHT) / 2

TIME_BUFFER = 50

arr = [4, 3, 2, 1, 5, 6]
arr_comparing = [False, False, False, False, False, False]
arr_in_order = [False, False, False, False, False, False]
RECTANGLE_WIDTH = SORTING_WIDTH / len(arr)
RECTANGLE_UNIT_HEIGHT = SORTING_HEIGHT / len(arr)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

render_bars()
pygame.display.flip()
pygame.time.delay(1000)

bogosort(arr)

pygame.time.delay(1000)
pygame.quit()