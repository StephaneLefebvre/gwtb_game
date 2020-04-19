#!/usr/bin/env python3

from levels import LevelOne

if __name__ == "__main__":
    game = LevelOne()

    while True:  # main game loop
        game.update_status()
        game.update_display()
