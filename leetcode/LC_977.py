class LC_977:
    def __init__(self):  # Constructor to initialize instance variable
        self.results = []

    def sortedSquares(self, nums):
            """
            Given an integer array nums sorted in non-decreasing order, 
            return an array of the squares of each number sorted in non-decreasing order.
            :type nums: List[int]
            :rtype: List[int]
            """
            left, right = 0, len(nums) - 1
            i = len(nums) - 1
            ans = [0] * len(nums)

            while left <= right:
                if abs(nums[left]) > abs(nums[right]):
                    ans[i] = nums[left] ** 2
                    left += 1
                else:
                    ans[i] = nums[right] ** 2
                    right -= 1
                i -= 1

            return ans                      

# lc_977 = LC_977()
nums = [-4, -1, 0, 3, 10]
# result = lc_977.sortedSquares(nums)
# print(result)       

sol: LC_977 = LC_977() #create object sol of the class
print(sol.sortedSquares(nums))       