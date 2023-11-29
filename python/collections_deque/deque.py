from collections import deque

if __name__ == "__main__":
    d = deque()
    for _ in range(int(input())):
        f, *args = input().split()
        getattr(d, f)(*list(map(int, args)))

    print(*d)