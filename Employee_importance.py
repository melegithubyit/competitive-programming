"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        Emap = dict()
        for employee in employees:
            Emap[employee.id] = employee
        def DFS(e):
            imp = Emap[e].importance        
            for sub in Emap[e].subordinates:
                imp += DFS(sub)
                
            return imp
        return DFS(id)