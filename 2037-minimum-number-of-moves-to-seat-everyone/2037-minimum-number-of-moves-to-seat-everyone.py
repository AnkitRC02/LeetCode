import itertools

class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        return sum(abs(a-b) for a, b in itertools.izip(seats, students))