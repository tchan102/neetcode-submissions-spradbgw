class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if (r // 3, c // 3) not in boxes:
                    boxes[(r // 3, c // 3)] = set()

                if val in rows[r] or val in cols[c] or val in boxes[(r // 3, c // 3)]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)

        return True