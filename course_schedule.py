class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degrees = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degrees[course] += 1
        queue = deque()
        for course in range(numCourses):
            if in_degrees[course] == 0:
                queue.append(course)
        while queue:
            curr_course = queue.popleft()
            for next_course in graph[curr_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)
        return sum(in_degrees) == 0

        


        