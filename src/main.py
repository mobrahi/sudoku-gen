import random
import copy
from typing import List, Tuple, Optional

class SudokuGenerator:
    def __init__(self):
        self.size = 9
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = None
    
    def generate_full_board(self) -> List[List[int]]:
        """Generate a complete, valid Sudoku board"""
        # Start with an empty board
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        
        # Fill the diagonal 3x3 boxes first (they're independent)
        for box in range(0, 9, 3):
            self._fill_box(box, box)
        
        # Fill the remaining cells
        self._fill_remaining(0, 3)
        
        # Store the solution
        self.solution = copy.deepcopy(self.board)
        return self.board
    
    def _fill_box(self, row: int, col: int):
        """Fill a 3x3 box with random numbers 1-9"""
        nums = list(range(1, 10))
        random.shuffle(nums)
        
        index = 0
        for i in range(3):
            for j in range(3):
                self.board[row + i][col + j] = nums[index]
                index += 1
    
    def _is_valid(self, num: int, row: int, col: int) -> bool:
        """Check if number placement is valid"""
        # Check row
        for j in range(9):
            if self.board[row][j] == num and j != col:
                return False

# Check column
        for i in range(9):
            if self.board[i][col] == num and i != row:
                return False
        
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num and (i != row or j != col):
                    return False
        
        return True
    
    def _fill_remaining(self, row: int, col: int) -> bool:
        """Fill remaining cells using backtracking"""
        if row == 8 and col == 9:
            return True
        
        if col == 9:
            row += 1
            col = 0
        
        if self.board[row][col] != 0:
            return self._fill_remaining(row, col + 1)