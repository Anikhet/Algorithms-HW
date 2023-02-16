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
    """
    Using priority queue(heap) to check if the food is finished before time.
    """
    time = x= 0
    bound = cumulative[-1] # Summation of the hour the last food came in and the time it takes to perish is the bound.
    while x <= bound:
        if not heap:
            if count == len(data): # If all the food has arrived and heap is empty
                return heap
            x = data[count][0] # Skip to the index where the next food comes in
            time = x - 1
        if heap and time < heap[0]:  # If the food with the highest priority has not perished, pop it.
            heapq.heappop(heap)
        time += 1

        temp_count = 0
        if count != len(data) and time == data[count][0]:  # counting how much food has arrived at a certain time
            for index in range(count, len(data)):
                if time < data[index][0]:
                    break

                if time == data[index][0]:
                    temp_count += 1

            for index in range(count, count + temp_count): # Pushing all the food that arrived into the heap.
                heapq.heappush(heap, cumulative[index])
            count += temp_count

        if heap and time >= heap[0]: # If the next food in line has perished, print No and exit the program.
            print("NO")
            quit()
        x += 1

    return heap


def main():
    num_length, data = read_input()
    count = 0
    data = [tuple(x) for x in data]
    temp = data[0][0]
    for x in range(len(data)):
        if data[x][0] == temp:
            count += 1

    cumulative = [0] * len(data)

    for x in range(len(data)): # Addition of the time it came in and the time it takes to perish.
        cumulative[x] = data[x][0] + data[x][1]

    heap = cumulative[0:count]
    heapq.heapify(heap) # heapify all the elements which came at the 0th index time.
    heap = priority(heap, data, count, cumulative)
    if heap:
        print("NO")  # If heap is not empty, the food was not finished on time.
    else:
        print("YES")


if __name__ == '__main__':
    main()
