class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        grid = {}

        for i in range(len(board[0])):
            for j in range(len(board)):
                entry = board[j][i]
                if entry == ".": continue
                if j not in rows:
                    rows[j] = set()
                if i not in cols:
                    cols[i] = set()
                if (i//3, j//3) not in grid:
                    grid[(i//3, j//3)] = set()

                if entry in rows[j] or entry in cols[i] or entry in grid[(i//3, j//3)]:
                    return False
                
                rows[j].add(entry)
                cols[i].add(entry)
                grid[(i//3, j//3)].add(entry)
    
        return True