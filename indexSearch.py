"""
file: indexSearch.py
language: python3
author: Anikhet Mulky , am9559@g.rit.edu
"""
"""_summary_: This program takes in a list of numbers and checks if the index of the number is equal to the number itself.
If it is, it prints TRUE, else it prints FALSE.
"""
def bin_search(data, left, right):
    """
    Binary search algorithm.
    :param data: Array to search on.
    :param left: leftmost index
    :param right: rightmost index
    """

    if left > right:  # A[k] = k was not found in the array.
        print("FALSE")
        quit()
    mid_index = (left + right) // 2

    if data[mid_index] == mid_index:
        print("TRUE")
        quit()
    if data[mid_index] > mid_index:
        return bin_search(data, left, mid_index - 1)  # Half of the array is discarded every time.
    else:
        return bin_search(data, mid_index + 1, right)


def read_input():
    """
    Reads input.
    """
    num = int(input())
    lst = list(map(int, input().split()))
    data = [0] * (len(lst) + 1)
    indexing = 1
    for index in lst: # Indexing it to start from 1
        data[indexing] = index
        indexing += 1
    return data


def main():
    """
    Main function.
    """
    data = read_input()
    bin_search(data, 1, len(data) - 1)
    print("FALSE")


if __name__ == '__main__':
    main()
