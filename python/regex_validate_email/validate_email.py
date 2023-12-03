import re

for _ in range(int(input())):
    name, email = input().split()
    # because "-" is used as range like a-z, A-Z, "-" has to be the last one in character class
    # "." dont need to escape in character class
    if re.match(r"<[a-zA-Z][\w_.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>", email):
        print(name, email)
    