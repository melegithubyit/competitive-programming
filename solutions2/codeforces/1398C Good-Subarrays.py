tests = int(input())

for _ in range(tests):
    n = int(input())
    string = input()
    lst = []
    
    for i in string:
        lst.append(int(i) - 1)
    
    store = {0:1}
    count = 0
    
    for i in range(1, n):
        lst[i] += lst[i-1]
    
    for i in lst:
        if i not in store:
            store[i] = store.get(i, 0) + 1
        
        else:
            count += store[i]
            store[i] = store.get(i, 0) + 1
    
    print(count)
            
    
        