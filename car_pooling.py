# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true

def carPooling(trips, capacity):
    lst = []
    for ppl, pick, drop in trips:
        lst.append([pick, ppl, 1])
        lst.append([drop, ppl, 0])

    lst.sort(key=lambda x: (x[0], x[2]))
    # [[1, 2, 1], [3, 3, 1], [5, 2, 0], [7, 3, 0]]
    
    current_people = 0

    for _, ppl, condition in lst:
        if condition == 1:
            current_people += ppl

        else:
            current_people -= ppl
        if current_people > capacity:
            return False

    return True


print(carPooling(trips=[[2,1,5],[3,3,7]], capacity=5))

