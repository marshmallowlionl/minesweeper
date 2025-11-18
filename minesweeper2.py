import tkinter as tk
import random
from tkinter import messagebox

class MinesweeperGUI:
    def __init__(self, master, size=8, num_mines=10):
        self.master = master
        self.size = size
        self.num_mines = num_mines
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.mines = set()
        self.revealed = set()
        self.create_widgets()
        self.place_mines()

    def create_widgets(self):
        for x in range(self.size):
            for y in range(self.size):
                btn = tk.Button(self.master, width=3, height=1, command=lambda x=x, y=y: self.reveal(x, y))
                btn.grid(row=x, column=y)
                self.buttons[x][y] = btn

    def place_mines(self):
        while len(self.mines) < self.num_mines:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.mines.add((x, y))

    def count_adjacent_mines(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) in self.mines:
                count += 1
        return count

    def reveal(self, x, y):
        if (x, y) in self.revealed:
            return
        self.revealed.add((x, y))
        btn = self.buttons[x][y]
        if (x, y) in self.mines:
            btn.config(text='*', bg='red')
            self.explode()
            return
        count = self.count_adjacent_mines(x, y)
        btn.config(text=str(count) if count > 0 else '', state='disabled', relief='sunken')
        if count == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        if (nx, ny) != (x, y):
                            self.reveal(nx, ny)
        if self.check_win():
            messagebox.showinfo('Minesweeper', 'Congratulations! You cleared the board!')
            self.master.quit()

    def explode(self):
        for (x, y) in self.mines:
            self.buttons[x][y].config(text='*', bg='red')
        messagebox.showerror('Minesweeper', 'Boom! You hit a mine!')
        self.master.quit()

    def check_win(self):
        return all((x, y) in self.revealed or (x, y) in self.mines for x in range(self.size) for y in range(self.size))

def main():
    root = tk.Tk()
    root.title('Minesweeper')
    game = MinesweeperGUI(root, size=8, num_mines=10)
    root.mainloop()

if __name__ == '__main__':
    main()
