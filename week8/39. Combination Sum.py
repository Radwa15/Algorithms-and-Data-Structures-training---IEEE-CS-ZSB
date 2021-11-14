class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, current, N = [], [], len(candidates)
        def dfs(current,start ,target):
            if target == 0:
                result.append(current.copy())
                return;
            if target < 0: return
            for i in range(start, N):
                current.append(candidates[i])
                dfs(current,i, target - candidates[i])
                current.pop()
        dfs(current, 0, target)
        return result
