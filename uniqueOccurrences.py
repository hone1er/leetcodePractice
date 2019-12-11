class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        checker = {}
        occurred = {}
        for i in arr:
            if i in checker:
                checker[i] += 1
            else:
                checker[i] = 1
        for k, v in checker.items():
            if v in occurred:
                return False
            else:
                occurred[v] = k
        return True
        