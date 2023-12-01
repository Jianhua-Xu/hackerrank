def fibonacci_1(n):
    '''return a list of fibonacci numbers'''
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    # This is clever, remove the need to write special case for 
    # n == 0 or n == 1
    return(lis[0:n])

def fibonacci_2(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

# N only goes up to 15 so just pre-generate the first 15 fib numbers and take a slice as needed.
def fibonacci_3(n):
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    return fib[:n]

def main():
    print("solutions for 3 different methods on 0,1,2,3,10")
    [print(lis) for lis in map(fibonacci_1, [0,1,2,3,10])]
    for lis in  map(fibonacci_2, [0,1,2,3,10]):
        print("[", end="")
        for lis2 in lis:
            print(lis2, end = ", ")
        print("]")
    [print(lis) for lis in map(fibonacci_3, [0,1,2,3,10])]

if __name__ == "__main__":
    main()