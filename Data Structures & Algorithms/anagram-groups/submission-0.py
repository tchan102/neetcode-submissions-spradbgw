class Solution:
    def helper(self, s):
        letters = [0] * 26
        for ch in s:
            letters[ord(ch) - ord('a')] += 1
        return tuple(letters)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            hashMap[self.helper(s)].append(s)
        return hashMap.values()
