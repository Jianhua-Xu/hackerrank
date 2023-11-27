1. python
    a. brutal force way
    b. use itertools.combination to generate all substring
    c. use math
2. q

Python scripts use different methods
1. brutal force way to generate substring and count, and keep improving but all too slow
2. math way. All the substrings are simply [string[x:y] for x, y in itertools.combinations(len(string)+1,2)].
    the total number of substring is math.comb(len(string)+1, 2)
3. math way. The problem can be viewed as chopping chars from the string as we go. 
    starting 1st char, all the substrings that starting 1st char are -- (1),(1,2)(1,3)(1,4)...(1,len(string))
    then chop off the 1st char. Now get the all the substrings starting 2nd char (2)(2,3)(2,4)...(2,len(string))
    chop off 2nd, start from 3rd....
    for kth char, the count of substrings starting kth char is len(string) - k(index)