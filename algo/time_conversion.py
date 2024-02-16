

def timeConversion(s):
    # Write your code here
    if s[-2] == 'A' and s[:2] == '12':
        s = '00' + s[2:]
    # breakpoint()
    if s[-2] == 'P' and int(s[:2]) < 12:
        s = str(int(s[:2]) + 12) + s[2:]
    return s[:-2]

print(timeConversion('07:05:45PM'))
print(timeConversion('07:05:45AM'))
print(timeConversion('12:05:45PM'))
print(timeConversion('12:05:45AM'))



def timeConversion2(s):
    if s[-2].lower() == 'a':
        s = '0' + str(int(s[:2]) % 12) + s[2:-2]
    else:
        s = str((int(s[:2]) % 12 + 12) % 24) + s[2:-2]

    return s

print(timeConversion2('07:05:45PM'))
print(timeConversion2('07:05:45AM'))
print(timeConversion2('12:05:45PM'))
print(timeConversion2('12:05:45AM'))


def timeConversion3(s):
    hh = str(int(s[:2]) % 12 + (s[-2].lower() == 'p') * 12).zfill(2)
    return hh + s[2:-2]


print(timeConversion3('07:05:45PM'))
print(timeConversion3('07:05:45AM'))
print(timeConversion3('12:05:45PM'))
print(timeConversion3('12:05:45AM'))