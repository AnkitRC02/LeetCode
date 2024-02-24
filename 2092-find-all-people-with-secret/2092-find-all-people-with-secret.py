import collections

class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        meetings.sort(key=lambda x: x[2])
        result = {0, firstPerson}
        adj = collections.defaultdict(list)
        for i, (x, y, _) in enumerate(meetings):
            adj[x].append(y)
            adj[y].append(x)
            if i+1 != len(meetings) and meetings[i+1][2] == meetings[i][2]:
                continue
            q = [i for i in adj.iterkeys() if i in result]
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if v in result:
                            continue
                        result.add(v)
                        new_q.append(v)
                q = new_q
            adj = collections.defaultdict(list)
        return list(result)