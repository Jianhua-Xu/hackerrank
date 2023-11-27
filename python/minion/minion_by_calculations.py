import math
import datetime

def minion_game(string):
    length = len(string)
    vowels = ('a','e','i','o','u')
    total_score = math.comb(length+1,2)
    vowel_score = 0
    for i, c in enumerate(string):
        if c.lower() in vowels:
            vowel_score += length-i

    print(total_score, vowel_score, total_score - vowel_score)



if __name__ == '__main__':
    print(f'starting...{datetime.datetime.now()}')
    s = input()
    print(f'got input...len={len(s)}')
    minion_game(s)
    print(f'ending...{datetime.datetime.now()}')