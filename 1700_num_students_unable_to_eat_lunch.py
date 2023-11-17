# from collections import deque
from collections import Counter

students, sandwiches = [1,1,0,0], [0,1,0,1]
# students, sandwiches = [1,1,1,0,0,1], [1,0,0,0,1,1]




class Solution:
    def countStudents(self, students, sandwiches):
        count = Counter(students)
        n, k = len(students), 0
        while k < n and count[sandwiches[k]]:
            count[sandwiches[k]] -= 1
            k += 1
        return n - k





        # students_d = deque(students)
        # sandwiches_d = deque(sandwiches)
        #
        # students_circ = len([student for student in students if student == 0])
        # students_square = len([student for student in students if student == 1])
        #
        #
        # #cur_student = students_d.popleft()
        # while students_d:
        #     cur_student = students_d.popleft()
        #     cur_sandwich = sandwiches_d.popleft()
        #
        #     if cur_sandwich != cur_student:
        #         students_d.append(cur_student)
        #         sandwiches_d.appendleft(cur_sandwich)
        #
        #     if len(students_d) == 0 and len(sandwiches_d) == 0:
        #         return 0
        #
        #
        #     if students_circ != students_square:
        #         if not 0 in students_d and cur_sandwich == 0:
        #             return len(students_d)
        #         if not 1 in students_d and cur_sandwich == 1:
        #             return len(students_d)
        #         if 0 in students_d and not 0 in sandwiches_d:
        #             return len(students_d)
        #         if 1 in students_d and not 1 in sandwiches_d:
        #             return len(students_d)
        #
        #
        #
        #
        # return 0

s = Solution()
print(s.countStudents(students, sandwiches))
