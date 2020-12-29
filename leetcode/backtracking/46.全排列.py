#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:

    def __init__(self):
        """
        docstring
        """
        self.result = []

    # list, list
    def __backtrack(self, path, candidates):
        """
        docstring
        """
        if candidates == []:
            # we should copy the data here !!!!
            self.result.append(path[:])
            return

        for i in range(len(candidates)):
            path.append(candidates[i])
            # tracing on other data
            res_candidates = candidates[:i] + candidates[i+1:]
            self.__backtrack(path, res_candidates)

            path.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        else:
            self.__backtrack([], nums)
            return self.result

# @lc code=end

