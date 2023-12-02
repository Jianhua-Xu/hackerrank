import re

s, k = input(), input()
pattern = re.compile(k)
m = pattern.search(s)
if not m:
    print((-1, -1))
while m:
    print(f"({m.start()}, {m.end()-1})")
    m = pattern.search(s, m.start()+1)

