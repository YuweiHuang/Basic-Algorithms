#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def __init__(self):
        """
        docstring
        """
        self.result = set([])

    def __backtrack(self, candidates, path, prev_num, temp_sum, target):
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
                if prev_num == candidates[i]:
                    continue

                # forward
                path.append(candidates[i])
                temp_sum += candidates[i]

                self.__backtrack(candidates[:i] + candidates[i+1:], path[:], prev_num, temp_sum, target)
                prev_num = candidates[i]

                # backward
                path.pop()
                temp_sum -= candidates[i]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.__backtrack(candidates, [], None, 0, target)
        return list(self.result)
# @lc code=end

