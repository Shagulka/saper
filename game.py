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
    elif keyboard.read_key() == "esc":
        break
