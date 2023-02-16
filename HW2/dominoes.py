"""
file: dominoes.py
language: python3
author: Anikhet Mulky , am9559@g.rit.edu
"""


def count_sort(data, n, indexing):
    """
    Performs counting sort on array based on a 0th or 1st index of the 2d list.
    """
    sorted_data = [[0] for _ in range(len(data))]
    array_count = [0] * (n + 1)

    for index in range(len(data)):
        array_count[data[index][indexing]] += 1

    cumulative = 0
    for index in range(len(array_count)):
        cumulative += array_count[index]
        array_count[index] = cumulative

    for index in range(len(data) - 1, -1, -1):
        sorted_data[array_count[data[index][indexing]] - 1] = data[index]
        array_count[data[index][indexing]] -= 1

    return sorted_data


def read_input():
    """
    Reads input.
    """

    num = int(input())
    grp_one = [[] for i in range(num)]
    threshold = int(input())
    for index in range(num):
        grp_one[index] = list(map(int, input().split()))
    return num, threshold, grp_one


def combo(data, index, index1, index2, threshold):
    """
    Performs the calculation of |a1-b1| + |a2-b2|
    """
    a1 = data[index][index1]
    a2 = data[index][index2]
    b1 = data[index + 1][index1]
    b2 = data[index + 1][index2]
    temp = abs(a1 - b1) + abs(a2 - b2)
    if temp <= threshold:
        return "YES"
    temp = abs(a1 - b2) + abs(a2 - b1)
    if temp <= threshold:
        return "YES"


def domino(data, num_length, threshold):
    """
    Finds if there is a pair that satisfies the equation.
    """
    data_sort_two = count_sort(data, num_length, 1)
    data_sort_one = count_sort(data, num_length, 0)
    data_sort_two_one = count_sort(data_sort_two, num_length, 0)
    data_sort_one_two = count_sort(data_sort_one, num_length, 1)

    for index in range(len(data)):
        if index + 1 == len(data):
            return "NO"

        combo1 = combo(data_sort_one, index, 0, 1, threshold)
        combo2 = combo(data_sort_two, index, 0, 1, threshold)
        combo3 = combo(data_sort_two_one, index, 0, 1, threshold)
        combo4 = combo(data_sort_one_two, index, 0, 1, threshold)

        if combo1 or combo2 or combo3 or combo4:
            return "YES"


def main():
    num_length, threshold, data = read_input()
    for x in range(len(data)): # Sorting the integers on the domino
        if data[x][0] > data[x][1]:
            data[x][0], data[x][1] = data[x][1], data[x][0]

    print(domino(data, num_length, threshold))


if __name__ == '__main__':
    main()



