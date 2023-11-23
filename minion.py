import datetime


def minion_game(string):
    # your code goes here
    length = len(string)
    sub_list = []
    vowel_score = 0
    consonant_score = 0
    for i in range(1, length+1):
        for j in range(length-i+1):
            sub_list.append(string[j:i+j])
    sub_list = set(sub_list)
    print(f"sub_list has {len(sub_list)} elements. time is {datetime.datetime.now()}")
    for sub in sub_list:
        if start_with_vowels(sub):
            vowel_score += find_occurence(string, sub)
        else:
            consonant_score += find_occurence(string, sub)
    if vowel_score > consonant_score:
        print(f"Kevin {vowel_score}")
    elif vowel_score == consonant_score:
        print("Draw")
    else:
        print(f"Stuart {consonant_score}")
    
    print(f"{datetime.datetime.now()}")

def start_with_vowels(string):
    return string[0].lower() in ('a', 'e', 'i', 'o', 'u')
        

def find_occurence(string, substring):
    occurence = 0
    for i in range(len(string)-len(substring)+1):
        if string[i:].startswith(substring):
            occurence += 1
    
    return occurence

if __name__ == '__main__':
    print(f'starting...{datetime.datetime.now()}')
    s = input()
    print(f'got input...len={len(s)}')
    minion_game(s)
