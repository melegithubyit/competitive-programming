class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda cost: cost[0] - cost[1])
        min_cost = 0

        for i in range(len(costs)):
            if i < len(costs) / 2:
                min_cost +=  costs[i][0]
            else:
                min_cost +=  costs[i][1]
        return min_cost
