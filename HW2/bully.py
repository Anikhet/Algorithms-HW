"""
file: bully.py
language: python3
author: Anikhet Mulky , am9559@g.rit.edu
"""


def merge_count(data):
    """
    Merges and counts the number of inversions.
    :param data: list of integers
    :return: list of integers, number of inversions
    """
    if len(data) <= 1:
        return data, 0
    mid = len(data) // 2
    first, temp = merge_count(data[:mid])
    second, temp2 = merge_count(data[mid:])
    inversions = temp + temp2 # adding inversions from every recursive call
    result = []
    index_one = index_two = 0

    while index_one < len(first) and index_two < len(second):
        if first[index_one] >= second[index_two]:
            result.append(first[index_one])
            index_one += 1
        else:
            inversions += len(first) - index_one # Counting inversions
            result.append(second[index_two])
            index_two += 1

    if index_one < len(first):
        result.extend(first[index_one:])
    else:
        result.extend(second[index_two:])

    return result, inversions


def read_input():
    """
    Reads input.
    """
    num = int(input())
    lst = list(map(int, input().split()))
    return lst


def main():
    """
    Main function.
    """
    data = read_input()
    bookmark = 0
    inversion = 0
    for index in range(len(data)):
        if data[index] == -1:
            tp, temp = merge_count(data[bookmark:index])
            inversion += temp # Adding inversions from every sub-array.
            bookmark = index + 1 # index from where the next sub-array should start from
            continue
        if index == len(data) - 1:
            tp, temp = merge_count(data[bookmark:len(data)])
            inversion += temp

    print(inversion)


if __name__ == '__main__':
    main()