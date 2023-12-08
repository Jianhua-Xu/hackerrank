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


# solution 2, copied from discussion
l,u,o,e=[],[],[],[]
for i in sorted(input()):
    if i.isalpha():
        x = u if i.isupper() else l
    else:
        x = o if int(i)%2 else e
    x.append(i)
print("".join(l+u+o+e))

# other solutions from discussion
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')