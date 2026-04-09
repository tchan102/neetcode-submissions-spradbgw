class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        categories = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in categories:
                categories[key] = []
            categories[key].append(s)
        return [v for v in categories.values()]