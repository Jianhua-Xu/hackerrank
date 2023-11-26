import itertools
import datetime

def minion_game(string):
    vowel = 0
    consonant = 0
    for x,y in itertools.combinations(range(len(string)+1),2):
        if string[x].lower() in ('a','e','i','o','u'):
            vowel += 1
        else:
            consonant += 1
    if vowel > consonant:
        print(f"Kevin {vowel}")
    elif vowel == consonant:
        print("draw")
    else:
        print(f"Stuart {consonant}")

 
        


if __name__ == '__main__':
    print(f'starting...{datetime.datetime.now()}')
    s = input()
    print(f'got input...len={len(s)}')
    minion_game(s)