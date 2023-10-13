def partitionLabels(s):
    
    last_pos = dict()
    
    for counter, cr in enumerate(s):
        last_pos[cr] = counter
        
    # print(last_pos)
    # {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11,'g': 13, 'h': 19, 'counter': 22, 'j': 23, 'k': 20, 'l': 21}

    ans = []
    left, right = 0, 0
    
    for counter, cr in enumerate(s):
        right = max(right, last_pos[cr])
        if counter == right:
            ans.append(right - left + 1)
            left = right + 1

    return ans

