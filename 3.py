import tkinter as tk
import random

class GameOfFifteen:
    def __init__(self, master):
        self.master = master
        self.master.title("Игра в 15")

        self.tiles = []
        self.empty_tile = (3, 3)

        self.create_tiles()
        self.shuffle_tiles()

    def create_tiles(self):
        for i in range(4):
            for j in range(4):
                if i == 3 and j == 3:
                    self.tiles.append(None)
                else:
                    tile = tk.Button(self.master, text=str(i*4 + j + 1), width=5, height=2, command=lambda i=i, j=j: self.move_tile(i, j))
                    tile.grid(row=i, column=j)
                    self.tiles.append(tile)

    def shuffle_tiles(self):
        random.shuffle(self.tiles)
        for i in range(16):
            if self.tiles[i] is not None:
                self.tiles[i].grid(row=i // 4, column=i % 4)
            else:
                self.empty_tile = (i // 4, i % 4)

    def move_tile(self, i, j):
        if (i, j) == (self.empty_tile[0], self.empty_tile[1] - 1) or \
           (i, j) == (self.empty_tile[0], self.empty_tile[1] + 1) or \
           (i, j) == (self.empty_tile[0] - 1, self.empty_tile[1]) or \
           (i, j) == (self.empty_tile[0] + 1, self.empty_tile[1]):
            index = i * 4 + j
            empty_index = self.empty_tile[0] * 4 + self.empty_tile[1]
            self.tiles[index], self.tiles[empty_index] = self.tiles[empty_index], self.tiles[index]
            self.tiles[index].grid(row=self.empty_tile[0], column=self.empty_tile[1])
            self.tiles[empty_index].grid(row=i, column=j)
            self.empty_tile = (i, j)

    def is_solved(self):
        for i in range(15):
            if self.tiles[i] is not None and int(self.tiles[i]["text"]) != i + 1:
                return False
        return True

root = tk.Tk()
game = GameOfFifteen(root)
root.mainloop()
