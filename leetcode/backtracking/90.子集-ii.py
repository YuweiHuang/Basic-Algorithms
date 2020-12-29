#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def __init__(self):
        """
        docstring
        """
        self.result = set([tuple([])])

    def __backtrack(self, candidates, path):
        """
        docstring
        """
        for i in range(len(candidates)):
            path.append(candidates[i])
            temp = path[:]
            temp.sort()
            self.result.add(tuple(temp))

            self.__backtrack(candidates[i+1:], path)

            path.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.__backtrack(nums, [])
        return list(self.result)
# @lc code=end

