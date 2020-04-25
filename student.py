import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from statusbar import *


class Student(GameObject, ABC):
    def __init__(self, x, y, width, height, name, image):
        GameObject.__init__(self, x, y, width, height)
        self._name = name
        self.image = image
        self.__statistics = {'Health': 100,
                             'Fatigue': 100,
                             # Сделать много подпунтков в пункте "Grades"
                             # 'Grades': {'Матеша': 0,
                             # 		'ФП': 0},
                             'Grades': 0,
                             'Money': 1000,
                             'Alcohol': 10,  # Алкоголь записывать в % (процент спирта в крови)
                             }
        self.font = pygame.font.Font('freesansbold.ttf', 25)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print("You can't do this operation!")
        return 0

    def draw(self, surface):
        surf = pygame.image.load(self.image)
        rect = surf.get_rect(bottomright=(self.bounds.x, self.bounds.y))
        surface.blit(surf, rect)
        text = self.font.render(str(self._name), True, (255, 0, 0),
                                (255, 255, 255))
        surface.blit(text, (self.bounds.x - 130, self.bounds.y))