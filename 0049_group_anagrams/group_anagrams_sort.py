from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())