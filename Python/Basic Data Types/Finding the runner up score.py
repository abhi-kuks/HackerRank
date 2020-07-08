if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)
    arr1.remove(max(arr1))
    print(max(arr1))
