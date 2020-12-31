#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:

    # this problem can not be solved by backtracking
    '''
    def __init__(self):
        """
        docstring
        """
        self.result = set([])

    def __backtrack(self, candidates, path, temp_sum, target):
        """
        docstring
        """
        if temp_sum > target:
            return

        elif temp_sum == target:
            self.result.add(tuple(path[:]))
            return

        else:
            for i in range(len(candidates)):
                path.append(candidates[i])
                temp_sum += candidates[i]

                self.__backtrack(candidates, path[:], temp_sum, target)
                
                path.pop()
                temp_sum -= candidates[i]
                

    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.__backtrack(nums, [], 0, target)
        return len(self.result)
    '''

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]


    
        
# @lc code=end

