import enum
import random

import math

import pygame

from pygame.locals import *
from game import Game
from misc import Color
from character import Character


class Level(Game):
    def __init__(self):
        super().__init__()


class TopDownLevel(Level):
    def __init__(self):
        super().__init__()

    def background_generator(self, color=Color.NAVYBLUE):
        while True:
            yield color

    def manage_event(self, event):
        super().manage_event(event)
        if self.mouse_pressed and event.type == MOUSEMOTION:
            self.player.destination = event.pos
        elif event.type == MOUSEBUTTONUP:
            self.mouse_pressed = False
        elif event.type == MOUSEBUTTONDOWN:
            self.player.destination = event.pos
            self.mouse_pressed = True

    def update_position(self, character):
        if (character.pos_x != character.destination[0]) or (
            character.pos_y != character.destination[1]
        ):
            distance = (
                character.destination[0] - character.pos_x,
                character.destination[1] - character.pos_y,
            )
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            if norm < character.speed:
                character.pos_x = character.destination[0]
                character.pos_y = character.destination[1]
            else:
                direction = (distance[0] / norm, distance[1] / norm)
                bullet_vector = (
                    direction[0] * character.speed,
                    direction[1] * character.speed,
                )
                character.pos_x += bullet_vector[0]
                character.pos_y += bullet_vector[1]


class SideLevel(Level):
    def __init__(self):
        super().__init__()
        self.gravity = 3.2

    def apply_gravity(self, character):
        if not self.detect_ground_colision(character):
            character.movey += self.gravity
        else:
            character.movey = 0

    def background_generator(self, color=Color.NAVYBLUE):
        assert all(
            color_element * 2 < 256 for color_element in color
        ), "color {} is a wrong input for background color generator".format(color)

        while True:
            yield color
            for i in range(100, 200):
                j = i / 100
                yield (color[0] * j, color[1] * j, color[2] * j)
            for i in range(200, 100, -1):
                j = i / 100
                yield (color[0] * j, color[1] * j, color[2] * j)

    def detect_ground_colision(self, character):
        for platform in self.platforms:
            if platform.top < character.pos_y + character.body_size + character.movey:
                print("Ground collision detected")
                return True
                pass

    def update_position(self, character):
        self.apply_gravity(character)
        character.pos_y += character.movey
        character.pos_x += character.movex


class LevelOne(SideLevel):
    def __init__(self):
        super().__init__()
        self.platforms = [pygame.Rect(0, self.WINDOWHEIGHT - 10, self.WINDOWWIDTH, 10)]
        self.backgrounds = [
            [
                pygame.Rect(
                    i * 10, self.WINDOWHEIGHT - random.randint(410, 450), 10, 200
                )
                for i in range(0, 65)
            ],
            [
                pygame.Rect(
                    i * 20, self.WINDOWHEIGHT - random.randint(360, 400), 20, 200
                )
                for i in range(0, 33)
            ],
            [
                pygame.Rect(
                    i * 40, self.WINDOWHEIGHT - random.randint(250, 350), 40, 350
                )
                for i in range(0, 17)
            ],
        ]
        self.background_color = self.background_generator()
        self.player = Character()
        self.characters = [self.player]

    def draw_background(self):
        self.DISPLAYSURF.fill(next(self.background_color))
        for element in self.backgrounds[0]:
            self.draw_element(element, Color.BLACK)
        for element in self.backgrounds[1]:
            self.draw_element(element, Color.DARK_GREY)
        for element in self.backgrounds[2]:
            self.draw_element(element, Color.LIGHT_GREY)
        for element in self.platforms:
            self.draw_element(element, Color.WHITE)
