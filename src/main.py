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
