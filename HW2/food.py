"""
file: food.py
language: python3
author: Anikhet Mulky , am9559@g.rit.edu
"""

import heapq


def read_input():
    """
    Reads input.
    """

    num = int(input())
    grp_one = [[] for i in range(num)]

    for index in range(num):
        grp_one[index] = list(map(int, input().split()))
    return num, grp_one


def priority(heap, data, count, cumulative):
    time = 0
    bound = cumulative[-1]
    x = 0
    while x <= bound:
        if not heap:
            if count == len(data):
                return heap
            x = data[count][0]
            time = x - 1
        if heap and time < heap[0]:
            heapq.heappop(heap)
        time += 1

        temp_count = 0
        if count != len(data) and time == data[count][0]:
            for index in range(count, len(data)):
                if time < data[index][0]:
                    break

                if time == data[index][0]:
                    temp_count += 1

            for index in range(count, count + temp_count):
                heapq.heappush(heap, cumulative[index])
            count += temp_count

        if heap and time >= heap[0]:
            print("NO")
            quit()
        x += 1

    return heap


def main():
    num_length, data = read_input()
    bound = data[-1][0]
    count = 0

    cumulative = [0] * len(data)
    data = [tuple(x) for x in data]
    lookup_heap = {}

    heapq.heapify(data)
    # for x in range(len(data)):
    #     print(data[x], lookup_heap[data[x]])

    temp = data[0][0]

    for x in range(len(data)):
        if data[x][0] == temp:
            count += 1

    cumulative = [0] * len(data)

    for x in range(len(data)):
        cumulative[x] = data[x][0] + data[x][1]

    heap = cumulative[0:count]

    heapq.heapify(heap)
    heap = priority(heap, data, count, cumulative)
    if heap:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()

# 11
# 0 3
# 0 3
# 1 9
# 1 15
# 7 3
# 7 3
# 8 2
# 8 2
# 9 20
# 10 20
# 11 20
