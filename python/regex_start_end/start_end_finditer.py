import re

s, k = input(), input()
# turn it into list?? why
# finditer always returns an iterator yielding Match object
# even if there is no match. By converting to list, we can test
# with if matches
matches = list(re.finditer(r'(?='+k+')', s))
if not matches:
    print((-1, -1))
for m in matches:
    print(f"({m.start()}, {m.end()+len(k)-1})")
