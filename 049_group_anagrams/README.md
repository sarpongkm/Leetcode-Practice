# 0049. Group Anagrams

## Problem

You’re given an array of strings `strs`. The goal is to group all the **anagrams** together.
Return the grouped anagrams in any order.

**Examples**

```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]  
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]  

Input:  strs = [""]  
Output: [[""]]  

Input:  strs = ["a"]  
Output: [["a"]]
```

**Constraints**

* 1 <= strs.length <= 10⁴
* 0 <= strs\[i].length <= 100
* Each string consists of lowercase English letters


## Solutions

### Approach 1: Sort Each Word (Dictionary Key = Sorted String)

* Anagrams share the same sorted sequence of characters.
* Sort each word, use it as a key, and group words in a dictionary.
* **Time Complexity:** O(n · k log k), where k = max word length
* **Space Complexity:** O(nk)

```python
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
```


### Approach 2: Character Count as Key

* Instead of sorting (O(k log k)), build a frequency count for each word (26 letters).
* Convert the count to a tuple and use it as the key.
* **Time Complexity:** O(n · k)
* **Space Complexity:** O(nk)

```python
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
```


### Approach 3: Brute Force (Naive Grouping)

* For each word, check all existing groups to see if it’s an anagram of the first word inside.
* If yes, add it; otherwise, start a new group.
* **Time Complexity:** O(n² · k) (very slow)
* **Space Complexity:** O(nk)

```python
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
```


### Why Character Count Is Best

* Sorting is simple and works well for small/medium input sizes.
* Character count avoids sorting overhead and runs in **O(n·k)**, making it faster for very large datasets.


### Key Takeaways

* Anagrams can be detected by either **sorting characters** or **counting characters**.
* Hashmaps (dictionaries) are powerful for grouping problems.
* Brute force is good for learning but not practical at scale.
