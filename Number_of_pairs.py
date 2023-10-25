import bisect
t = int(input())
for _ in range(t):

    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = 0
    for i in range(n):
        result += bisect.bisect_right(arr, r - arr[i]) - \
            bisect.bisect_left(arr, l - arr[i])

        if (l <= (2 * arr[i])) and ((2 * arr[i]) <= r):
            result -= 1

    print(int(result / 2))
