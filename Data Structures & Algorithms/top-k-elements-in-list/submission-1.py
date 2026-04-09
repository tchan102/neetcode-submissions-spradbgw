class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        x = sorted([(y, z) for y, z in d.items()], key=lambda x: -x[1])
        return [x[_][0] for _ in range(k)] if k <= len(x) else [y for y,z in x]