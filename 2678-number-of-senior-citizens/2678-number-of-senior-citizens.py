class Solution(object):
    def countSeniors(self, details):
        return sum(1 for detail in details if int(detail[11:13]) > 60)

        