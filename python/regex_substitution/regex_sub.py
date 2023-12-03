# Problem:
# change "&&" to "and", "||" to "or"
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

# solution 1
# bug -- input "x&& &&& && && x || | ||\|| x"
# output -- 'x&& &&& and && x or | ||\\|| x'
# should be 'x&& &&& and and x or | ||\\|| x'
# overlapping issue, functions in re do not do overlapping
import re

for _ in range(int(input())):
    print(re.sub(r' && ', r' and ', re.sub(r' \|\| ', r' or ', input())))
