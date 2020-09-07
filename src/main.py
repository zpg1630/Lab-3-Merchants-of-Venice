import merchants
from typing import List
from typing import Tuple


def main():
    filename = 'data\\test-10.txt'
    merchant = merchants.read_merchant(filename)
    for i in range(len(merchant)):
        print(merchant[i])
    sort_merch = quick_sort(merchant)
    print(len(sort_merch)//2)


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


if __name__ == '__main__':
    main()
