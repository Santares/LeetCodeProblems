class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = max(len(v1), len(v2))
        for i in range(n):
            if i >= len(v1):
                v1x = 0
            else:
                v1x = int(v1[i])
            if i >= len(v2):
                v2x = 0
            else:
                v2x = int(v2[i])
            if v1x > v2x:
                return 1
            elif v1x < v2x:
                return -1
        return 0
