"""
Merchants
Takes a list of merchants and locations from the data folder and sorts using quick sort or quick select based on the
user's input.
:Author: Zachary Gagnon
"""

from dataclasses import dataclass
from random import randrange
from typing import List
from typing import Tuple
import time
from os import path


@dataclass
class Merchant:
    name: str
    location: int


def read_merchant(filename: str) -> List[Merchant]:
    """
    Read merchants from a file into a list of Merchant dataclass objects.
    :param filename: The name of the file
    :return: A list of Merchants
    """
    merchants = list()
    with open(filename) as f:
        for line in f:
            fields = line.split(' ')
            merchants.append(Merchant(
                name=fields[0],
                location=int(fields[1]),
            ))
    return merchants


def _partition(data: List[Merchant], pivot: int) \
        -> Tuple[List[Merchant], List[Merchant], List[Merchant]]:
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


def quick_sort(data: List[Merchant]) -> List[Merchant]:
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


def partition(lst: List[Merchant], pivot_index=0):
    """
    Partition the data into a smaller list containing the target
    :param lst: The data to be partitioned (a list)
    :param pivot_index: The value to partition the data on
    :return: the partition that contains the target
    """
    i = 0
    # pivot
    if pivot_index != 0:
        lst[0], lst[pivot_index] = lst[pivot_index], lst[0]
    # sort
    for j in range(len(lst) - 1):
        # shift positions
        if lst[j + 1].location < lst[0].location:
            lst[j + 1], lst[i + 1] = lst[i + 1], lst[j + 1]
            i += 1
    # portion of list that was sorted
    lst[0], lst[i] = lst[i], lst[0]
    return lst, i


def quick_select(lst: List[Merchant], k):
    """
    Performs a quick select and returns the selected element
    :param lst: The data to be selected from
    :param k: the target location
    :return: the element at the target location
    """
    # if there's nothing to sort
    if len(lst) == 1:
        # return the only merchant
        return lst[0]
    else:
        # start partition
        lst_part = partition(lst, randrange(len(lst)))
        lst = lst_part[0]  # partitioned array
        j = lst_part[1]  # pivot index
        # target found
        if j == k:
            return lst[j]
        # search larger
        elif j > k:
            return quick_select(lst[:j], k)
        # Search smaller
        else:
            k = k - j - 1
            return quick_select(lst[(j + 1):], k)


def main():
    """
    main loop for control of the program, allows the user to perform multiple sorts/selects and specify the file
    location each time. When the user os finished they can type quit to exit the program. Handles erroneous input.
    :param: None
    :return: None
    """
    choice = True
    # main loop for program control
    while choice:
        # used for sum of distances
        distance = 0
        speed = input('Enter the search type [slow|fast] or "quit" to quit: ')
        # exit loop
        if speed == 'quit':
            choice = not choice
        # start sorting
        elif speed == 'slow' or speed == 'fast':
            # get the file
            filename = 'data\\' + input('Enter the file name: ')
            # check if it exists
            if path.exists(filename):
                # read merchants from file
                merchant = read_merchant(filename)
                print('Number of merchants: ', len(merchant))
                # quick sort
                if speed == 'slow':
                    # start timer
                    start_1 = time.perf_counter()
                    # call quick sort function
                    merchant = quick_sort(merchant)
                    # stop timer
                    stop_1 = time.perf_counter()
                    print('Elapsed time: ', stop_1 - start_1)
                    print('Optimal store location: ', merchant[len(merchant) // 2])
                    # calculate sum
                    for _ in range(len(merchant)):
                        distance += abs(merchant[_].location - merchant[len(merchant) // 2].location)
                    print(distance)
                # quick select
                elif speed == 'fast':
                    # start timer
                    start_2 = time.perf_counter()
                    # call quick select
                    optimal_merchant = quick_select(merchant, len(merchant) // 2)
                    # stop timer
                    stop_2 = time.perf_counter()
                    print('Elapsed time: ', stop_2 - start_2)
                    print('Optimal store location: ', optimal_merchant)
                    # calculate sum
                    for _ in range(len(merchant)):
                        distance += abs(merchant[_].location - optimal_merchant.location)
                    print(distance)
            else:
                print('File does not exist, try again.')
        else:
            print('Wrong input, must be "slow", "fast", or "quit". Try again.')


if __name__ == '__main__':
    main()
