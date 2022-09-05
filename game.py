import sys
import minesweeper_assets_manager as assets
import random
import keyboard
import os
import json

menu = True


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Menu:
    def __init__(self):
        self.options = ["Play", "Settings", "Exit"]
        self.selected = 0

    def draw(self):
        cls()
        print("Minesweeper")
        for i in range(len(self.options)):
            if i == self.selected:
                print(f"> {self.options[i]}")
            else:
                print(f"  {self.options[i]}")

    def move(self, direction):
        if direction == "up":
            if self.selected > 0:
                self.selected -= 1
        elif direction == "down":
            if self.selected < len(self.options) - 1:
                self.selected += 1

    def select(self):
        global menu
        if self.selected == 0:
            menu = PreGameMenu()
            return "play"
        elif self.selected == 1:
            
            menu = Settings()
            return "settings"
        elif self.selected == 2:
            sys.exit()
            return "exit"


class Settings:
    def __init__(self):
        self.options = ["Assets", "Back"]
        self.selected = 0

    def draw(self):
        cls()
        print("Settings")
        for i in range(len(self.options)):
            if i == self.selected:
                print(f"> {self.options[i]}")
            else:
                print(f"  {self.options[i]}")

    def move(self, direction):
        if direction == "up":
            if self.selected > 0:
                self.selected -= 1
        elif direction == "down":
            if self.selected < len(self.options) - 1:
                self.selected += 1

    def select(self):
        global menu
        if self.selected == 0:
            menu = Assets()
            return "assets"
        elif self.selected == 1:
            menu = Menu()
            return "menu"


class Assets:
    def __init__(self):
        list_of_packs = os.listdir("assets")
        self.options = ["Back"]
        self.options += list_of_packs
        self.selected = 0

    def draw(self):
        cls()
        print("Assets")
        for i in range(len(self.options)):
            if i == self.selected:
                print(f"> {self.options[i]}")
            else:
                print(f"  {self.options[i]}")

    def move(self, direction):
        if direction == "up":
            if self.selected > 0:
                self.selected -= 1
        elif direction == "down":
            if self.selected < len(self.options) - 1:
                self.selected += 1

    def select(self):
        global menu
        if self.selected == 0:
            menu = Settings()
            menu.draw()
            return "settings"
        else:
            assets.load_assets("assets/" + self.options[self.selected])
            menu = Settings()
            menu.draw()
            return "settings"

class PreGameMenu:
    def __init__(self):
        self.options = ["Easy", "Medium", "Hard" "Back"]
        self.selected = 0

    def draw(self):
        cls()
        print("Select Difficulty")
        for i in range(len(self.options)):
            if i == self.selected:
                print(f"> {self.options[i]}")
            else:
                print(f"  {self.options[i]}")

    def move(self, direction):
        if direction == "up":
            if self.selected > 0:
                self.selected -= 1
        elif direction == "down":
            if self.selected < len(self.options) - 1:
                self.selected += 1

    def select(self):
        global menu
        if self.selected == 0:
            menu = Game(9, 9, 10)
            #menu.draw()
            return "game"
        elif self.selected == 1:
            menu = Game(16, 16, 40)
            #menu.draw()
            return "game"
        elif self.selected == 2:
            menu = Game(30, 16, 99)
            #menu.draw()
            return "game"

        elif self.selected == 3:
            menu = Menu()
            menu.draw()
            return "menu"


class Game:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.true_board = []
        self.player_board = []
        self.flagged = []
        self.selected = [0, 0]
        self.game_over = False
        self.game_won = False
        self.mine_locations = []
        self.mine_count = 0
        self.flag_count = 0
        self.time = 0
        self.generate_board()
        self.generate_mines()
        self.generate_numbers()
        self.draw()
    
    def generate_board(self):
        for i in range(self.height):
            self.true_board.append([])
            self.player_board.append([])
            for j in range(self.width):
                self.true_board[i].append(0)
                self.player_board[i].append(0)
    
    def generate_mines(self):
        for i in range(self.mines):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self.true_board[y][x] != 9:
                    self.true_board[y][x] = 9
                    self.mine_locations.append([x, y])
                    break
    
    def generate_numbers(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.true_board[i][j] != 9:
                    self.true_board[i][j] = self.get_surrounding_mines(j, i)

    def get_surrounding_mines(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + j >= 0 and x + j < self.width and y + i >= 0 and y + i < self.height:
                    if self.true_board[y + i][x + j] == 9:
                        count += 1
        return count

    def draw(self):
        cls()
        print(f"Time: {self.time}")
        print(f"Flags: {self.flag_count}/{self.mines}")
        for i in range(self.height):
            for j in range(self.width):
                if self.player_board[i][j] == 0:
                    if [j, i] == self.selected:
                        print(assets.get_asset("selected"), end="")
                    else:
                        print(assets.get_asset("hidden"), end="")
                elif self.player_board[i][j] == 1:
                    if [j, i] == self.selected:
                        print(assets.get_asset("selected"), end="")
                    elif self.true_board[i][j] == 9:
                        print(assets.get_asset("mine"), end="")
                    elif self.true_board[i][j] == 0:
                        print(assets.get_asset("empty"), end="")
                    else:
                        print(assets.get_asset(str(self.true_board[i][j])), end=" ")
                elif self.player_board[i][j] == 2:
                    print(assets.get_asset("flag"), end="")
            print()
        if self.game_over:
            print("Game Over")
        elif self.game_won:
            print("You Win!")
    
    def move(self, direction):
        if direction == "up":
            if self.selected[1] > 0:
                self.selected[1] -= 1
        elif direction == "down":
            if self.selected[1] < self.height - 1:
                self.selected[1] += 1
        elif direction == "left":
            if self.selected[0] > 0:
                self.selected[0] -= 1
        elif direction == "right":
            if self.selected[0] < self.width - 1:
                self.selected[0] += 1

    def flag(self):
        x = self.selected[0]
        y = self.selected[1]
        if self.player_board[y][x] == 0:
            self.player_board[y][x] = 2
            self.flag_count += 1
            self.flagged.append([x, y])
        elif self.player_board[y][x] == 2:
            self.player_board[y][x] = 0
            self.flag_count -= 1
            self.flagged.remove([x, y])
    
    def select(self):
        x = self.selected[0]
        y = self.selected[1]
        if self.player_board[y][x] == 0:
            if self.true_board[y][x] == 9:
                self.player_board[y][x] = 1
                self.game_over = True
            elif self.true_board[y][x] == 0:
                self.player_board[y][x] = 1
                self.reveal_empty(x, y)
            else:
                self.player_board[y][x] = 1
        if self.check_win():
            self.game_won = True

    
    
    def reveal_empty(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + j >= 0 and x + j < self.width and y + i >= 0 and y + i < self.height:
                    if self.player_board[y + i][x + j] == 0:
                        self.player_board[y + i][x + j] = 1
                        if self.true_board[y + i][x + j] == 0:
                            self.reveal_empty(x + j, y + i)

    def check_win(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.player_board[i][j] == 0 and self.true_board[i][j] != 9:
                    return
        self.game_won = True
    
    def update(self):
        if self.game_over or self.game_won:
            return "menu"
        self.time += 1
        return "game"
    
    


    


menu = Menu()
menu.draw()
while True:
    if keyboard.read_key() == "w":
        menu.move("up")
        menu.draw()
    elif keyboard.read_key() == "s":
        menu.move("down")
        menu.draw()
    elif keyboard.read_key() == "a":
        menu.move("left")
        menu.draw()

    elif keyboard.read_key() == "d":
        menu.move("right")
        menu.draw()
    elif keyboard.read_key() == "enter":
        menu.select()
        menu.draw()
    elif keyboard.read_key() == "f":
        menu.flag()
        menu.draw()
    elif keyboard.read_key() == "esc":
        break
