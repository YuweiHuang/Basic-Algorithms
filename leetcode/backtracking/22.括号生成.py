#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def __init__(self):
        """
        docstring
        """
        self.result = set([])

    def __match(self, parenthesis):
        """
        docstring
        """
        lab_stack = []

        for i in parenthesis:
            if i == '(':
                lab_stack.append('(')
            else:
                if lab_stack == []:
                    return False
                else:
                    lab_stack.pop()

        if lab_stack == []:
            return True
        else:
            False
                


    def __backtrack(self, candidates, path, n, left_count, right_count):
        """
        docstring
        """
        if len(path) == 2 * n:
            if left_count == right_count:
                if self.__match(path):
                    self.result.add(path)
                    return
                
            else:
                return
        else:
            for i in range(len(candidates)):
                path += candidates[i]
                if candidates[i] == "(":
                    left_count += 1
                else:
                    right_count += 1

                self.__backtrack(candidates, path[:], n, left_count, right_count)

                path = path[:-1]
                if candidates[i] == "(":
                    left_count -= 1
                else:
                    right_count -= 1

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            self.__backtrack(["(", ")"], "", n, 0, 0)
            return list(self.result)

# @lc code=end

