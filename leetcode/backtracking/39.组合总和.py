#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
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
            path.sort()
            temp = path[:]
            self.result.add(tuple(temp))
            return

        else:
            for i in range(len(candidates)):
                # forward
                path.append(candidates[i])
                temp_sum += candidates[i]

                self.__backtrack(candidates, path[:], temp_sum, target)
                
                # backward
                path.pop()
                temp_sum -= candidates[i]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.__backtrack(candidates, [], 0, target)
        return list(self.result)

# @lc code=end

