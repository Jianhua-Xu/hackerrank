from collections import Counter

# In python >3.7, dict keeps order. Counter is subclass of dict, so it should keep orders too
words = [input().strip() for _ in range(int(input()))]
counts = Counter(words)
print(len(counts))
print(*counts.values())
