class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        total = 1

        # if num == 0, increase zeros otherwise multiply the total of num
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total *= num
              
        # if there are more than one zeros in nums then always the total except self will be zero
        if zeros > 1:
            return [0] * len(nums)

        result = []
  
        for num in nums:
            # if one zero present
            if zeros == 1:
                # if number is zero then output that index will be total
                if num == 0:
                    result.append(total)
                # if there is one zero in array and that index in not zero, therefore product will be zero beacuse 0 * x = 0
                else:
                    result.append(0)
               
            # if there is no zeros in array
            else:
               # divide total by num to get product except self
                result.append(int(total/num))
                
        # return the result array
        return result
        
