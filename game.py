'''
Game Logic
'''
import random

class Game:
    def __init__(self):
        self.grid = [[0] * 10 for _ in range(10)]
        self.add_random_tile()
        self.add_random_tile()
        
    def add_random_tile(self):
        empty_spots = []
        for row in range(10):
            for col in range(10):
                if self.grid[row][col] == 0:
                    empty_spots.append((row, col))
        if empty_spots:
            row, col = random.choice(empty_spots)
            self.grid[row][col] = random.choice([2, 2, 2, 2, 4])  # 80% 概率生成2，20% 概率生成4
            
    def move_up(self):
        moved = self.move_tiles("up")
        merged = self.merge_tiles("up")
        final_moved = self.move_tiles("up")
        if moved or merged or final_moved:
            self.add_random_tile()
        return moved or merged or final_moved
        
    def move_down(self):
        moved = self.move_tiles("down")
        merged = self.merge_tiles("down")
        final_moved = self.move_tiles("down")
        if moved or merged or final_moved:
            self.add_random_tile()
        return moved or merged or final_moved
        
    def move_left(self):
        moved = self.move_tiles("left")
        merged = self.merge_tiles("left")
        final_moved = self.move_tiles("left")
        if moved or merged or final_moved:
            self.add_random_tile()
        return moved or merged or final_moved
        
    def move_right(self):
        moved = self.move_tiles("right")
        merged = self.merge_tiles("right")
        final_moved = self.move_tiles("right")
        if moved or merged or final_moved:
            self.add_random_tile()
        return moved or merged or final_moved
        
    def move_tiles(self, direction):
        moved = False
        if direction == "up":
            for col in range(10):
                for row in range(1, 10):
                    if self.grid[row][col] != 0:
                        if self.move_tile(row, col, -1, 0):
                            moved = True
        elif direction == "down":
            for col in range(10):
                for row in range(8, -1, -1):
                    if self.grid[row][col] != 0:
                        if self.move_tile(row, col, 1, 0):
                            moved = True
        elif direction == "left":
            for row in range(10):
                for col in range(1, 10):
                    if self.grid[row][col] != 0:
                        if self.move_tile(row, col, 0, -1):
                            moved = True
        elif direction == "right":
            for row in range(10):
                for col in range(8, -1, -1):
                    if self.grid[row][col] != 0:
                        if self.move_tile(row, col, 0, 1):
                            moved = True
        return moved
        
    def move_tile(self, row, col, row_offset, col_offset):
        original_row = row
        original_col = col
        value = self.grid[row][col]
        self.grid[row][col] = 0
        
        while 0 <= row + row_offset < 10 and 0 <= col + col_offset < 10 and self.grid[row + row_offset][col + col_offset] == 0:
            row += row_offset
            col += col_offset
            
        self.grid[row][col] = value
        return row != original_row or col != original_col
        
    def merge_tiles(self, direction):
        merged = False
        if direction == "up":
            for col in range(10):
                for row in range(9):
                    if self.grid[row][col] != 0 and self.grid[row][col] == self.grid[row + 1][col]:
                        self.grid[row][col] *= 2
                        self.grid[row + 1][col] = 0
                        merged = True
        elif direction == "down":
            for col in range(10):
                for row in range(9, 0, -1):
                    if self.grid[row][col] != 0 and self.grid[row][col] == self.grid[row - 1][col]:
                        self.grid[row][col] *= 2
                        self.grid[row - 1][col] = 0
                        merged = True
        elif direction == "left":
            for row in range(10):
                for col in range(9):
                    if self.grid[row][col] != 0 and self.grid[row][col] == self.grid[row][col + 1]:
                        self.grid[row][col] *= 2
                        self.grid[row][col + 1] = 0
                        merged = True
        elif direction == "right":
            for row in range(10):
                for col in range(9, 0, -1):
                    if self.grid[row][col] != 0 and self.grid[row][col] == self.grid[row][col - 1]:
                        self.grid[row][col] *= 2
                        self.grid[row][col - 1] = 0
                        merged = True
        return merged
        
    def is_game_over(self):
        # 检查是否有2048
        for row in range(10):
            for col in range(10):
                if self.grid[row][col] >= 2048:
                    return True
                    
        # 检查是否还有空格
        for row in range(10):
            for col in range(10):
                if self.grid[row][col] == 0:
                    return False
                    
        # 检查是否还有可以合并的相邻数字
        for row in range(10):
            for col in range(10):
                current = self.grid[row][col]
                # 检查右边
                if col < 9 and current == self.grid[row][col + 1]:
                    return False
                # 检查下边
                if row < 9 and current == self.grid[row + 1][col]:
                    return False
                    
        return True  # 没有空格且没有可以合并的数字，游戏结束