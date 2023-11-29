from collections import Counter, OrderedDict

# the solution works even for python < 3.7, where dict does not keep key order
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())