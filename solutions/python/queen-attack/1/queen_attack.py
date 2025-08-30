class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        
        self.row, self.column = row, column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        same_row = self.row == another_queen.row
        same_column = self.column == another_queen.column
        same_diagonal = abs(self.row - another_queen.row) == abs(self.column - another_queen.column)
        
        return same_row or same_column or same_diagonal       