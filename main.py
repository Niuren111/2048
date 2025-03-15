'''
2048 Game
'''
import tkinter as tk
from game import Game

class GameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 Game")
        self.game = Game()
        self.colors = {
            0: "#CDC1B4",
            2: "#EEE4DA",
            4: "#EDE0C8",
            8: "#F2B179",
            16: "#F59563",
            32: "#F67C5F",
            64: "#F65E3B",
            128: "#EDCF72",
            256: "#EDCC61",
            512: "#EDC850",
            1024: "#EDC53F",
            2048: "#EDC22E"
        }
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="#BBADA0")
        self.canvas.pack(padx=10, pady=10)
        
        # 绑定键盘事件到根窗口
        self.master.bind("<Key>", self.handle_keypress)
        self.master.focus_set()
        
        self.update_grid()

    def handle_keypress(self, event):
        moved = False
        if event.keysym == "Up":
            moved = self.game.move_up()
        elif event.keysym == "Down":
            moved = self.game.move_down()
        elif event.keysym == "Left":
            moved = self.game.move_left()
        elif event.keysym == "Right":
            moved = self.game.move_right()
            
        if moved:
            self.update_grid()
            
        if self.game.is_game_over():
            self.master.unbind("<Key>")
            self.canvas.create_rectangle(100, 150, 300, 250, fill="white", outline="gray")
            self.canvas.create_text(200, 200, text="Game Over", font=("Arial", 24, "bold"), fill="red")

    def update_grid(self):
        self.canvas.delete("all")
        for row in range(10):
            for col in range(10):
                value = self.game.grid[row][col]
                x1 = col * 40
                y1 = row * 40
                x2 = x1 + 40
                y2 = y1 + 40
                
                # 创建圆角矩形
                self.canvas.create_rectangle(x1+2, y1+2, x2-2, y2-2, 
                                          fill=self.colors.get(value, "#CDC1B4"),
                                          outline="")
                
                if value != 0:
                    font_size = 16 if value < 100 else 14 if value < 1000 else 12
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2,
                                         text=str(value),
                                         font=("Arial", font_size, "bold"),
                                         fill="#776E65" if value <= 4 else "white")
        self.canvas.update()

def main():
    root = tk.Tk()
    root.resizable(False, False)
    app = GameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()