import re

vowels = "AEIOUaeiou"
consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
match = f"(?=[{consonants}]([{vowels}]{{2,}})[{consonants}])"
s = input()
# print(*re.findall(match, input()), sep="\n")
# print(*map(lambda x: x.group(1), re.finditer(match, input())), sep="\n")
m = list(re.finditer(match, s))
print("using finditer")
if not m:
    print(-1)
else:
    print(*map((lambda x: x.group(1)), m), sep="\n")

print("using findall")
print(*re.findall(match, s), sep='\n')