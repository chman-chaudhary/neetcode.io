class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        # compare if both sorted string equals return true else return false 
        return s == t
