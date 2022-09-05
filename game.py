import minesweeper_assets_manager as assets
import random
import keyboard
import os
import json


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


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
        if self.selected == 0:
            return "play"
        elif self.selected == 1:
            return "settings"
        elif self.selected == 2:
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
        if self.selected == 0:
            return "assets"
        elif self.selected == 1:
            return "back"


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
        if self.selected == 0:
            return "back"
        else:
            assets.load_assets(self.options[self.selected])
            return "load"
