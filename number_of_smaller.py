# m, n = map(int, input().split())
# first_lst = list(map(int, input().split()))
# second_lst = list(map(int, input().split()))
a = [1,6,9,13,18,18]
b = [2,3,8,13,15,21,25,45,87 ]


counts = []
n = 6
m = 7

for num in b:
    left = 0
    right = n - 1
    index = -1

    while left <= right:
        middle = (left + right) // 2
        if a[middle] < num:
            index = middle
            left = middle + 1
        else:
            right = middle - 1

    counts.append(index + 1)

print(*counts)
