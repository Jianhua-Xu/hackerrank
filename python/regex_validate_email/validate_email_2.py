import re

for _ in range(int(input())):
    name, email = input().split()
    # use () and | for character class
    if re.match(r"<[a-zA-Z](\w|_|\.|-)+@[a-zA-Z]+\.[a-zA-Z]{1,3}>", email):
        print(name, email)
    