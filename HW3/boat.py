"""
file: boat.py
language: python3
author: Nithish Kumar, nk6825@g.rit.edu, Anikhet Mulky, am9559@g.rit.edu
"""
import sys


def quick_select(arr, left, right, min_pivot, min_diff):
    if len(arr) == 1:
        return min_pivot, min_diff
    pivot = arr[0]
    young = []
    old = []
    for stu in arr:
        if stu != pivot:
            if stu[0] <= pivot[0]:
                left += stu[1]
                young.append(stu)
            else:
                right += stu[1]
                old.append(stu)
    left += pivot[1]
    young.append(pivot)
    if abs(left - right) < min_diff:
        min_pivot = pivot
        min_diff = abs(left - right)

    if left > right:
        return quick_select(young, left - sum([stu[1] for stu in young]), right, min_pivot, min_diff)
    else:
        return quick_select(old, left, right - sum([stu[1] for stu in old]), min_pivot, min_diff)


def read_input():
    arr = []
    n = int(input())
    T1 = float(input())
    T2 = float(input())
    for _ in range(n):
        line = input()
        l = line.split()
        arr.append((float(l[0]), float(l[1])))
    return T1,T2,arr
    
    

def main():
    T1,T2,arr = read_input()
    pivot1, min1 = quick_select(arr, T1, T2, arr[0], sys.maxsize)
    T1, T2 = T2, T1
    pivot2, min2 = quick_select(arr, T1, T2, arr[0], sys.maxsize)
    if min1 < min2:
        pivot = pivot1
    else:
        pivot = pivot2
    ans = 0
    for stu in arr:
        if stu[0] <= pivot[0]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
