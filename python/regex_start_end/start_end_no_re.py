# solution 1 -- did not use module re
s, k = input(), input()
length = len(k)
res = set()
for i in range(len(s)-length+1):
    if k == s[i:length+i]:
        res.add((i, length-1+i))

if not res:
    print((-1, -1))
else:
    for pair in sorted(list(res)):
        print(pair)