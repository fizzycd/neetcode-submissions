from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        sandwiches = sandwiches[::-1]

        for sw in reversed(sandwiches):
            for i in range(len(students_queue)):
                student = students_queue.popleft()
                if student == sw:
                    sandwiches.pop()
                    break
                students_queue.append(student)
            else:
                return len(students_queue)
        return 0
