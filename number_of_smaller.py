n, m = map(int, input().split())
first_lst = list(map(int, input().split()))
second_lst = list(map(int, input().split()))

counts = []

for num in second_lst:
    left = 0
    right = n - 1
    index = -1

    while left <= right:
        middle = (left + right) // 2
        if first_lst[middle] < num:
            index = middle
            left = middle + 1
        else:
            right = middle - 1

    counts.append(index + 1)

print(*counts)
