from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = Counter(chars)
        ret = 0
        for word in words:
            counter = 0
            for char in word:
                if char not in d or d[char] < word.count(char):
                    counter = 0
                    break
                else:
                    counter += 1
            ret += counter
        return ret