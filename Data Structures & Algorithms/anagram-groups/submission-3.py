class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: list of strings ( lower char words ) 
        # output list of list of strings -> group by their anagram identity, group word with the occurrence of letters

        def word2count(w: str) -> Tuple[str]:
            count = [0] * 26
            for ch in w:
                count[ord(ch) - ord('a')] += 1
            return tuple(count)

        anagramMap = {} # count -> List[str]
        for s in strs:
            key = word2count(s)
            if key not in anagramMap:
                anagramMap[key] = []
            anagramMap[key].append(s)
        
        return list(anagramMap.values()) 
