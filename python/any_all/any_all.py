def check_palindromic(number):
    return number == int(str(number)[::-1])

n = int(input())
lis = list(map(int, input().split()))

res = False
if all([i>0 for i in lis]):
    if any([check_palindromic(j) for j in lis]):
        res = True

print(res)