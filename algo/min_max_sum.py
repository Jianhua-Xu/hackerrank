"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
"""
import timeit

arr=[1,3,5,7,9]

# linear time, 4*n time
def min_max_sum1(arr):
    total = sum(arr)
    # comment out for timeit testing without output
    # print(total - max(arr), total - min(arr))
    return (total - max(arr), total - min(arr))

min_max_sum1(arr)

# linear, 1 * n time
def min_max_sum2(arr):
    total = 0
    max = min = arr[0]
    for e in arr:
        total += e
        if e > max:
            max = e
        if e < min:
            min =e

    # comment out for timeit testing without output
    # print(total - max, total - min)
    return (total - max, total - min)

min_max_sum2(arr)


# worst algo, sort first and then add up by slicing
def min_max_sum3(arr):
    arr.sort()
    # comment out for timeit testing without output
    # print(sum(arr[:4]), sum(arr[1:]))
    return (sum(arr[:4]), sum(arr[1:]))
min_max_sum3(arr)

print(timeit.repeat("min_max_sum1(arr)", "from __main__ import min_max_sum1, arr", number=100000))
print(timeit.repeat("min_max_sum2(arr)", "from __main__ import min_max_sum2, arr", number=100000))
print(timeit.repeat("min_max_sum3(arr)", "from __main__ import min_max_sum3, arr", number=100000))