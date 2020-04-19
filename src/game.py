import pygame, sys
from pygame.locals import *

from misc import Color
from character import Character


class Game:
    def __init__(self):
        pygame.init()
        self.FPS = 30  # frames per second, the general speed of the program
        self.FPSCLOCK = pygame.time.Clock()
        self.WINDOWWIDTH = 640  # size of window's width in pixels
        self.WINDOWHEIGHT = 480  # size of windows' height in pixels
        self.screen_generator = self.switch_fullscreen()
        self.DISPLAYSURF = next(self.screen_generator)
        pygame.display.set_caption("Gone with the blastwave")

        self.mouse_pressed = False

        self.background = []
        self.player = None
        self.characters = []

    def manage_events(self):
        for event in pygame.event.get():
            self.manage_event(event)

    def switch_fullscreen(self):
        while True:
            yield pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
            yield pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def manage_event(self, event):
        if event.type == QUIT or event.type == KEYDOWN and event.key == 27:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.unicode == "f":
            self.DISPLAYSURF = next(self.screen_generator)

    def update_position(self, character):
        pass

    def update_status(self):
        self.manage_events()
        for character in self.characters:
            self.update_position(character)

    def draw_element(self, element, color=Color.DARK_GREY):
        pygame.draw.rect(self.DISPLAYSURF, color, element)

    def draw_background(self):
        self.DISPLAYSURF.fill(Color.BLACK)
        for element in self.background:
            self.draw_element(element)

    def update_display(self):
        self.draw_background()
        self.player.update_display(self.DISPLAYSURF)
        pygame.display.update()
        self.FPSCLOCK.tick(self.FPS)
