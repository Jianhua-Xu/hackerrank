# solution 1
# sorted takes nlogn, so not the fast way
def merge_the_tools(string, k):
    # your code goes here
    for i in range(len(string)//k):
        sub = string[i*k:(i+1)*k]
        print(''.join([sub[j] for j in sorted([sub.index(c) for c in set(sub)])]))
        
# solution 2
# should be faster, O(n)
def merge_the_tools_2(string, k):
    for i in range(len(string)//k):
        sub = string[i*k:(i+1)*k]
        seen = set()
        # seen.add(x) does not return anything(None). It changes in-place. 
        print(''.join([c for c in sub if not(c in seen or seen.add(c)) ]))

# solution 3
# python3.7 up, dictionary key preserve the order. Take advantage of that
def merge_the_tools_3(string, k):
    for i in range(len(string)//k):
        # dict.fromkeys(x) create a dict such that x as key, value as 0  
        print(''.join(list(dict.fromkeys(string[i*k:(i+1)*k]))))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    merge_the_tools_2(string, k)
    merge_the_tools_3(string, k)