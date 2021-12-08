from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)
        stack = []

        for index, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                top = stack.pop()
                solution[top] = index - top

            stack.append(index)

        return solution
