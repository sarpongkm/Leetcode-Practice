class Solution(object):
    def groupAnagrams(self, strs):
        def isAnagram(w1, w2):
            return sorted(w1) == sorted(w2)

        groups = []
        for word in strs:
            placed = False
            for g in groups:
                if isAnagram(g[0], word):
                    g.append(word)
                    placed = True
                    break
            if not placed:
                groups.append([word])
        return groups