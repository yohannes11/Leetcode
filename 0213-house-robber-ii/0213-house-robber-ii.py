class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n <=2:
            return max(nums)
        def robing(input_array):
            n = len(input_array)
            if n <=2:
                return max(input_array)
            current = input_array[0]
            current_max = max(input_array[:2])
            for i in range(2,n):
                temp = current_max
                current_max = max(current_max,input_array[i]+current)
                current = temp
            return current_max
        without_first_house = robing(nums[1:])
        with_first_house = robing(nums[:len(nums)-1])
        return max(without_first_house,with_first_house)

            
        