#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:

    def __init__(self):
        """
        docstring
        """
        self.result = [[]]

    def __backtrack(self, candidates, path):
        """
        docstring
        """
        for i in range(len(candidates)):
            path.append(candidates[i])
            self.result.append(path[:])

            self.__backtrack(candidates[i+1:], path)
            
            path.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.__backtrack(nums, [])
        return self.result

# @lc code=end

