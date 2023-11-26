import tkinter as tk
from tkinter import messagebox
import random

class FifteenPuzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("Пятнашки")
        self.tiles = [[None] * 4 for _ in range(4)]
        self.empty_row, self.empty_col = 3, 3

        for i in range(4):
            for j in range(4):
                number = i * 4 + j + 1
                if number != 16:
                    button = tk.Button(root, text=str(number), width=5, height=2,
                                       command=lambda row=i, col=j: self.move_tile(row, col))
                    button.grid(row=i, column=j)
                    self.tiles[i][j] = button
                else:
                    # Ячейка с текстом "-", которая будет выполнять роль пустой ячейки
                    self.tiles[i][j] = tk.Button(root, text="-", width=5, height=2, state=tk.DISABLED)
                    self.tiles[i][j].grid(row=i, column=j)

        shuffle_button = tk.Button(root, text="Перемешать", command=self.shuffle)
        shuffle_button.grid(row=4, columnspan=4)

    def move_tile(self, row, col):
        if (abs(row - self.empty_row) == 1 and col == self.empty_col) or \
           (abs(col - self.empty_col) == 1 and row == self.empty_row) or \
           (row == self.empty_row and col == self.empty_col) or \
           (row == self.empty_row and col == self.empty_col + 1) or \
           (row == self.empty_row + 1 and col == self.empty_col):
            # Если рядом с нажатой ячейкой есть ячейка "-", меняем их местами
            if self.tiles[row][col]["text"] == "-" or self.tiles[self.empty_row][self.empty_col]["text"] == "-":
                self.tiles[self.empty_row][self.empty_col]["text"], self.tiles[row][col]["text"] = self.tiles[row][col]["text"], self.tiles[self.empty_row][self.empty_col]["text"]
                self.empty_row, self.empty_col = row, col
                # Меняем местами кнопку и пустую ячейку
                self.tiles[self.empty_row][self.empty_col].grid(row=self.empty_row, column=self.empty_col)
                self.tiles[row][col].grid(row=row, column=col)
                
                if self.is_solved():
                    messagebox.showinfo("Поздравляем!", "Вы разгадали пазл!")

    def shuffle(self):
        numbers = list(range(1, 16))
        random.shuffle(numbers)

        for i in range(4):
            for j in range(4):
                if numbers:
                    self.tiles[i][j]["text"] = str(numbers.pop(0))
                else:
                    self.tiles[i][j]["text"] = "-"
                    self.empty_row, self.empty_col = i, j
                    # Меняем местами кнопку и пустую ячейку
                    self.tiles[self.empty_row][self.empty_col].grid(row=self.empty_row, column=self.empty_col)

    def is_solved(self):
        numbers = [i for i in range(1, 16)]
        numbers.append("-")

        for i in range(4):
            for j in range(4):
                if self.tiles[i][j]["text"] != numbers[i * 4 + j]:
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = FifteenPuzzle(root)
    root.mainloop()
