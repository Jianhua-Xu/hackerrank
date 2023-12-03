import re

# solution 2
# Use lookbehind to find the overlapping ' '
for _ in range(int(input())):
    print(re.sub(r'(?<= )&& ', r'and ', re.sub(r'(?<= )\|\| ', r'or ', input())))