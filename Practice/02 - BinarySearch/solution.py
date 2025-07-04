import sys

def binarySearch(arr,n,x):
    a = 0
    b = n-1
    while a<=b:
        k = (a+b)//2
        if arr[k] == x:
            print(f"Found At Index: {k}")
            return
        elif arr[k] < x:
            a = k+1
        else:
            b = k-1


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,2,3,4,5,6,7]
    binarySearch(arr,14,7)