class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_set = set()
            for i in range(len(row)):
                if row[i] == ".":
                    continue
                else:
                    if row[i] in row_set:
                        return False
                    else:
                        row_set.add(row[i])
        for i in range (0 , 9):
            column_set = set()
            for row in board:
                if row[i] == ".":
                    continue
                else:
                    if row[i] in column_set:
                        return False
                    else:
                        column_set.add(row[i])
        box_sets = {}
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                box_key = (row // 3, col // 3)
                if box_key not in box_sets:
                    box_sets[box_key] = set()
                if val in box_sets[box_key]:
                    return False
                box_sets[box_key].add(val)
        return True

        