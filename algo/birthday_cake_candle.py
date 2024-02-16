"""Given a list of candle heights, return the number of tallest candles(how many tallest candles)"""


def birthdayCakeCandles(candles):
    # Write your code here
    max = 0
    counts = 0
    for e in candles:
        if e > max:
            max = e
            counts = 1
        elif e == max:
            counts += 1
           
    return counts

def f2(arr):
    return arr.count(max(arr))