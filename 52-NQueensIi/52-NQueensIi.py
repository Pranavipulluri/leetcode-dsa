# Last updated: 6/2/2026, 12:04:27 PM
class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.' for j in range(n)] for i in range(n)]
        colset=set()
        lud=set()
        rud=set()
        def backtrack(row):
            if row==n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in colset or row-col in lud or row+col in rud:
                    continue
                board[row][col]="Q"
                colset.add(col)
                lud.add(row-col)
                rud.add(row+col)

                backtrack(row+1)

                board[row][col]="."
                colset.remove(col)
                lud.remove(row-col)
                rud.remove(row+col)
        backtrack(0)
        return len(res)
    