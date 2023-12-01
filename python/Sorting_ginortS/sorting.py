s = input()

digits = []
uppers = []
lowers = []
for c in s:
    if c.isdigit():
        digits.append(c)
    elif c.isupper():
        uppers.append(c)
    elif c.islower():
        lowers.append(c)

digits_sorted = sorted(sorted(digits), key=lambda x: int(x) % 2 == 0)
print("".join(sorted(lowers) + sorted(uppers) + digits_sorted))