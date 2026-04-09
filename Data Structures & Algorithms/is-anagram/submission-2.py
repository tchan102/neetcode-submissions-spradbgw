class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input: string won't come with special char ? only lowercase english letters
        # output: bool -> tell whether a two string matches each other when one's reading backward
        # quickway compared two's counter -> 
        # im gonna do a hashmap actually using an array to rep
        # index 0 as a 1 as b, so on and so on, 25 as z
        # then value as the occurance to count the s string occurance and minus t string occruance, and check if the array is zero
        # one thing that can check ahead is if s and t string is in different length, if yes return false, as they have to be same length to compare

        # 1 check if they are in the same length
        if len(s) != len(t):
            return False

        # build a shared hashmap for s and t to count the occurance
        letters = [0] * 26 
        q = lambda x: ord(x) - ord('a')
        # iterate s and t tgt
        for a, b in zip(s, t):
            letters[q(a)] += 1
            letters[q(b)] -= 1
        
        for occurance in letters: 
            if occurance != 0:
                return False
        return True
