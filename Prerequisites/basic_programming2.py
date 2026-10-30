import sys
from collections import Counter

n, t = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))


def action_sum_pair(A):
    # t = 1: "Yes" if two distinct elements x != y sum to 7777, else "No"
    seen = set(A)
    for i in A:
        if 7777 - i in seen and 7777 - i != i:
            return "Yes"
    return "No"


def action_uniqueness(A):
    # t = 2: "Unique" if all elements are distinct, else "Contains duplicate"
    seen = set()
    for i in A:
        if i in seen:
            return "Contains duplicate"
        seen.add(i)
    return "Unique"


def multiple_occurences(A):
    c = Counter(A)
    for i in c:
        if c[i] > n/2:
            return(i)
        else:
            return("-1")


def calc_median(A):
    sorted_A = sorted(A)
    n = len(sorted_A)
    if n % 2 == 1:
        return str(sorted_A[n // 2])
    else:
        return str(sorted_A[n // 2 - 1]) + " " + str(sorted_A[n // 2])


def sorted_array(A):
    sorted_A = sorted(A)
    for i in sorted_A:

        if i >= 100 and i <= 999:

            print(i, end=" ")


if t == 1:
    print(action_sum_pair(A))
elif t == 2:
    print(action_uniqueness(A))
elif t == 3:
    print(multiple_occurences(A))
elif t == 4:
    print(calc_median(A))
elif t == 5:
    sorted_array(A)
