class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a directory of list in which key: string and value will be list
        # Key: 'aet' (sorted version of "eat", "tea", "ate")
        # Value: ["eat", "tea", "ate"]
        res = defaultdict(list)

        for s in strs:
            # sort the string
            key = "".join(sorted(s))

            # append the string at end of sorted list value
            res[key].append(s)

        # convert the directory into list
        return list(res.values())
