import merchants
import sys


def main():
    filename = 'data\\test-10.txt'
    merchant = merchants.read_merchant(filename)
    for i in range(len(merchant)):
        print(merchant[i])


if __name__ == '__main__':
    main()
