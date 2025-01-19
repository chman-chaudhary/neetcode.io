class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a set which contains all the elements
        my_set = set()

        # create a map which contains index according to respective value like map[value] = index
        my_map = {}

        # check every index
        for i in range(len(nums)):
            # if target - nums[index] in set return array of index and index of target - nums[i] in map
            if target - nums[i] in my_set:
                return [my_map[target - nums[i]], i]
            # otherwise add value in set and add num[index] in map with index value
            else:
                my_map[nums[i]] = i
                my_set.add(nums[i])

        # return empty array which not possible
        return []
