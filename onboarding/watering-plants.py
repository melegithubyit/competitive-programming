class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 1
        full = capacity
        for i in range(len(plants)):
            remaining = capacity - plants[i]
            capacity -= plants[i]
            if i + 1 < len(plants):
                if remaining < plants[i + 1]:
                    steps += (i + 1)
                    steps += (i + 2)
                    capacity = full
                else:
                    steps += 1
            else:
                break

        return steps