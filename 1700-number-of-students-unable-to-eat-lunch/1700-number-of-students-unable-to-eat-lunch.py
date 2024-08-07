import collections

class Solution(object):
    def countStudents(self, students, sandwiches):
    
        count = collections.Counter(students)
        for i, s in enumerate(sandwiches):
            if not count[s]:
                break
            count[s] -= 1
        else:
            i = len(sandwiches)
        return len(sandwiches)-i
        