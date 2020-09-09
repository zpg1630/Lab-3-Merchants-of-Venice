from random import randrange
from typing import List
from typing import Tuple
import merchants
import time
from os import path


def main():
    choice = True
    while choice:
        distance = 0
        speed = input('Enter the search type [slow|fast] or "quit" to quit: ')
        if speed == 'quit':
            choice = not choice
        elif speed == 'slow' or speed == 'fast':
            filename = 'data\\' + input('Enter the file name: ')
            if path.exists(filename):
                merchant = merchants.read_merchant(filename)
                print('Number of merchants: ', len(merchant))
                if speed == 'slow':
                    # quick sort
                    start_1 = time.perf_counter()
                    merchant = quick_sort(merchant)
                    stop_1 = time.perf_counter()
                    print('Elapsed time: ', stop_1 - start_1)
                    print('Optimal store location: ', merchant[len(merchant) // 2])
                    for _ in range(len(merchant)):
                        distance += abs(merchant[_].location-merchant[len(merchant) // 2].location)
                    print(distance)
                elif speed == 'fast':
                    # quick select
                    start_2 = time.perf_counter()
                    optimal_merchant = quick_select(merchant, len(merchant) // 2)
                    stop_2 = time.perf_counter()
                    print('Elapsed time: ', stop_2 - start_2)
                    print('Optimal store location: ', optimal_merchant)
                    for _ in range(len(merchant)):
                        distance += abs(merchant[_].location-optimal_merchant.location)
                    print(distance)
            else:
                print('File does not exist, try again.')
        else:
            print('Wrong input, must be "slow", "fast", or "quit". Try again.')


def _partition(data: List[merchants.Merchant], pivot: int) \
        -> Tuple[List[merchants.Merchant], List[merchants.Merchant], List[merchants.Merchant]]:
    """
    Three way partition the data into smaller, equal and greater lists,
    in relationship to the pivot
    :param data: The data to be sorted (a list)
    :param pivot: The value to partition the data on
    :return: Three list: smaller, equal and greater
    """
    less, equal, greater = [], [], []
    for element in data:
        if element.location < pivot:
            less.append(element)
        elif element.location > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater


def quick_sort(data: List[merchants.Merchant]) -> List[merchants.Merchant]:
    """
    Performs a quick sort and returns a newly sorted list
    :param data: The data to be sorted (a list)
    :return: A sorted list
    """
    if len(data) == 0:
        return []
    else:
        pivot = data[0].location
        less, equal, greater = _partition(data, pivot)
        return quick_sort(less) + equal + quick_sort(greater)


def partition(lst: List[merchants.Merchant], pivot_index=0):
    i = 0
    if pivot_index != 0:
        lst[0], lst[pivot_index] = lst[pivot_index], lst[0]
    for j in range(len(lst) - 1):
        if lst[j + 1].location < lst[0].location:
            lst[j + 1], lst[i + 1] = lst[i + 1], lst[j + 1]
            i += 1
    lst[0], lst[i] = lst[i], lst[0]
    return lst, i


def quick_select(lst: List[merchants.Merchant], k):
    # if there's nothing to sort
    if len(lst) == 1:
        # return the only merchant
        return lst[0]
    else:
        lst_part = partition(lst, randrange(len(lst)))
        lst = lst_part[0]  # partitioned array
        j = lst_part[1]  # pivot index
        if j == k:
            return lst[j]
        elif j > k:
            return quick_select(lst[:j], k)
        else:
            k = k - j - 1
            return quick_select(lst[(j + 1):], k)


if __name__ == '__main__':
    main()
