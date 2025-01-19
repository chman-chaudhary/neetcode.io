class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create empty set
        my_set = set()

        # check every element of array
        for num in nums:
            # if num present in set return True
            if num in my_set:
                return True
            # other wise add element in set
            else:
                my_set.add(num)

        # if all elements are single than return False
        return False
