from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                parent[y] = x

        emailsToIndex = {}
        i = 0
        for account in accounts:
            for email in account[1:]:
                if email not in emailsToIndex:
                    emailsToIndex[email] = i
                else:
                    if emailsToIndex[email] != i:
                        union(i, emailsToIndex[email])
            i += 1

        indexToEmails = defaultdict(list)
        for email in emailsToIndex:
            index = find(emailsToIndex[email])
            indexToEmails[index].append(email)

        res = []
        for index in indexToEmails:
            res.append([accounts[index][0]] + sorted(indexToEmails[index]))

        return res
