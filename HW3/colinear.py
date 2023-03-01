"""
file: colinear.py
language: python3
author: Anikhet Mulky , am9559@g.rit.edu, Nithish Kumar, nk6825@g.rit.edu
"""

import time


def merge_sort(data, index):
    """
    Merge Sort algorithm.
    :param index:
    :param data: Array to be sorted
    :return: Sorted array.
    """
    if len(data) == 1:
        return data
    mid_index = len(data) // 2
    first = merge_sort(data[0:mid_index], index)
    second = merge_sort(data[mid_index:], index)
    result = []
    index_one = index_two = 0
    while index_one < len(first) and index_two < len(second):
        if first[index_one][index] <= second[index_two][index]:
            result.append(first[index_one])
            index_one += 1
        else:
            result.append(second[index_two])
            index_two += 1

    if index_one < len(first):
        result.extend(first[index_one:])
    else:
        result.extend(second[index_two:])
    return result


def bin_search(data, left, right, target):
    """
    Binary search algorithm.
    :param target:
    :param data: Array to search on.
    :param left: leftmost index
    :param right: rightmost index
    """

    if left > right:
        return False

    mid_index = (left + right) // 2

    if data[mid_index][0] == target[0]:
        if data[mid_index][1] == target[1]:
            return True
        elif data[mid_index][1] > target[1]:
            return bin_search(data, left, mid_index - 1, target)
        else:
            return bin_search(data, mid_index + 1, right, target)

    if data[mid_index][0] > target[0]:
        return bin_search(data, left, mid_index - 1, target)  # Half of the array is discarded every time.
    else:
        return bin_search(data, mid_index + 1, right, target)


def algorithm(data):
    for index in range(len(data)):

        for inside_index in range(index + 1, len(data)):
            x_one = data[index][0]
            y_one = data[index][1]
            x_two = data[inside_index][0]
            y_two = data[inside_index][1]

            coordinates = ((x_one + x_two) / 2, (y_one + y_two) / 2)
            if bin_search(data, index, inside_index, coordinates):
                slope_one = (y_two - y_one) / (x_two - x_one)
                slope_two = (coordinates[1] - y_one) / (coordinates[0] - x_one)
                if slope_one == slope_two:
                    return True

                
def algorithm_optimal(data):
    table = {}
    for index in range(len(data)):
        table[tuple(data[index])] = table.get(tuple(data[index]),0)
    for index in range(len(data)):

        for inside_index in range(index + 1, len(data)):
            x_one = data[index][0]
            y_one = data[index][1]
            x_two = data[inside_index][0]
            y_two = data[inside_index][1]

            coordinates = ((x_one + x_two) / 2, (y_one + y_two) / 2)

            if not (coordinates[0].is_integer() and coordinates[1].is_integer()):
                continue
            if tuple(coordinates) in table:
                slope_one = (y_two - y_one) / (x_two - x_one)
                slope_two = (coordinates[1] - y_one) / (coordinates[0] - x_one)
                if slope_one == slope_two:
                    return True


def read_input():
    """
    Reads input.
    """

    num = int(input())
    grp_one = [[] for i in range(num)]
    for index in range(num):
        grp_one[index] = list(map(int, input().split()))
    return num, grp_one


def main():
    start = time.time()
    num_length, data = read_input()
    first_sort = merge_sort(data, 1)
    first_sort = merge_sort(data, 0)

    if algorithm(first_sort):  # O(n2 Log n)
        print("YES")
    else:
        print("NO")
        
    # if algorithm_optimal(first_sort):  # This one uses hash-table to make it O(n2)
    #     print("YES")
    # else:
    #     print("NO")

    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
