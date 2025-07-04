# Normal I/O
# n = int(input())
# arr = list(map(int, input().split()))
# s = 0
# b = 0
# for aval in arr:
#     s = max(aval,s+aval)
#     b = max(b,s)
# print(b)


import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    s = 0
    b = 0
    for aval in arr:
        s = max(aval, s+aval)
        b = max(b,s)
    print(b)

if __name__ == "__main__":
    main()

