import pygame

import math
from misc import Color, Role


class Character:
    def __init__(
        self,
        color=Color.RED,
        position=(20, 20),
        size=(10, 15),
        role=Role.Soldier,
        name="Steeve",
    ):
        # RPG elements
        self.name = name
        self.role = role

        # Visual elements
        self.color = color
        self.head_size = 10
        self.body_size = 15

        # Location elements
        self.pos_x = position[0]
        self.pos_y = position[1]

        # Top Down elements
        self.speed = 3
        self.destination = (self.pos_x, self.pos_y)

        # Side scroller elements
        self.movey = 0
        self.movex = 0

    def keyboard_update(self, event):
        assert event.type == KEYDOWN, "Wrong event type"

    def update_status(self, event):
        if event.type == KEYDOWN:
            self.keyboard_update(event)

    def update_display(self, DISPLAYSURF):
        pygame.draw.rect(
            DISPLAYSURF,
            self.color,
            pygame.Rect(self.pos_x, self.pos_y, self.head_size, self.head_size),
        )
        pygame.draw.rect(
            DISPLAYSURF,
            Color.GREY,
            pygame.Rect(
                self.pos_x, self.pos_y + self.head_size, self.head_size, self.body_size
            ),
        )
