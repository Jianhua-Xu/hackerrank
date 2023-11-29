from collections import defaultdict

# In python >3.7, dict keeps order. defaultdict is subclass of dict, so it should keep orders too
d = defaultdict(int)
for _ in range(int(input())):
    d[input()] += 1

print(len(d))
print(*d.values())


