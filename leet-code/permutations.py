from typing import List
import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def recursive_dfs(elements, next, prev=[]):
            if not next:
                results.append(prev)
                return

            for e in next:
                next_elements = copy.deepcopy(next)
                next_elements.remove(e)

                prev_elements = copy.deepcopy(prev)
                prev_elements.append(e)

                recursive_dfs(elements, next_elements, prev_elements)

        def iterative_dfs():
            stack = [([], nums)]

            while stack:
                prev, next = stack.pop()
                if not next:
                    results.append(prev)

                for e in next:
                    prev_elements = copy.deepcopy(prev)
                    prev_elements.append(e)

                    next_elements = copy.deepcopy(next)
                    next_elements.remove(e)

                    stack.append((prev_elements, next_elements))

        # recursive_dfs(nums, nums)
        iterative_dfs()
        return results
