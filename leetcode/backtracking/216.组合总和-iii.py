#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def __init__(self):
        """
        docstring
        """
        self.result = set([])

    def __backtrace(self, candidates, path, temp_sum, n, k):
        """
        docstring
        """
        if temp_sum > n or len(path) > k:
            return

        elif temp_sum == n and len(path) == k:
            path.sort()
            temp = path[:]
            self.result.add(tuple(temp))
            return
        else:
            for i in range(len(candidates)):
                path.append(candidates[i])
                temp_sum += candidates[i]

                self.__backtrace(candidates[:i] + candidates[i+1:], path[:], temp_sum, n, k)

                path.pop()
                temp_sum -= candidates[i]

                

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.__backtrace([i for i in range(1, 10)], [], 0, n, k)
        return list(self.result)

# @lc code=end

