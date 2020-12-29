#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def __init__(self):
        """
        docstring
        """
        self.result = set([])

    def __backtrace(self, candidates, path):
        """
        docstring
        """
        if candidates == []:
            self.result.add(tuple(path[:]))
            return

        for i in range(len(candidates)):
            # forward
            path.append(candidates[i])

            self.__backtrace(candidates[:i] + candidates[i+1:], path)

            # backward
            path.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        else:
            self.__backtrace(nums, [])
            return list(self.result)
        
# @lc code=end

