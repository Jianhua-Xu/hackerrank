import datetime

def sub_generator(string):
    length = len(string)
    for i in range(1, length+1):
        for j in range(length-i+1):
            yield string[j:i+j]

def minion_game(string):
    # your code goes here
    vowel_score = {}
    consonant_score = {}
    sub_list = sub_generator(string)
    print(f"sub_list done. time is {datetime.datetime.now()}")
    for sub in sub_list:
        if start_with_vowels(sub):
            if sub in vowel_score:
                vowel_score[sub] +=1
            else:
                vowel_score[sub] = 1
        else:
            if sub in consonant_score:
                consonant_score[sub] += 1
            else:
                consonant_score[sub] = 1
    vowels = sum(vowel_score.values())
    consonants = sum(consonant_score.values())
    if vowels > consonants:
        print(f"Kevin {vowels}")
    elif vowels == consonants:
        print("Draw")
    else:
        print(f"Stuart {consonants}")
    
    print(f"{datetime.datetime.now()}")

def start_with_vowels(string):
    return string[0].lower() in ('a', 'e', 'i', 'o', 'u')
        

def find_occurence(string, substring):
    occurence = 0
    sub_len = len(substring)
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+sub_len] == substring:
            occurence +=1
    return occurence


if __name__ == '__main__':
    print(f'starting...{datetime.datetime.now()}')
    s = input()
    print(f'got input...len={len(s)}')
    minion_game(s)
