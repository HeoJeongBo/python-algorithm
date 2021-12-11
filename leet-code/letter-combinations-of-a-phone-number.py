from typing import List


class Solution:
    phone_number_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        def recursive_dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in self.phone_number_letters[digits[i]]:
                    recursive_dfs(i + 1, path + j)

        def iterative_dfs():
            stack = [(0, [])]

            while stack:
                index, chars = stack.pop()
                if index == len(digits):
                    result.append("".join(chars))
                else:
                    for char in self.phone_number_letters[digits[index]]:
                        stack.append([index+1, chars + [char]])

        if not digits:
            return []

        result = []
        # recursive_dfs(0, "")
        iterative_dfs()

        return result
