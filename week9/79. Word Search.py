class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        n = len(word)
        visited = set()
        def dfs(r,c,idx):
            if idx > n :
                return False
            visited.add((r,c))
            if idx == n-1:
                return True
            for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                rr,cc = r + dr, c + dc
                if rr in range(row)  and cc in range(col) \
                    and (rr,cc) not in visited and board[rr][cc] == word[idx+1]:
                    if dfs(rr,cc,idx+1): return True
            visited.remove((r,c))
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r,c,0): 
                        return True
