from dataclasses import dataclass
from typing import List


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
