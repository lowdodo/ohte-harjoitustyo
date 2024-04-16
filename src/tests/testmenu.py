import unittest
import pygame
from index import main_menu


class TestMenu:
    def setUp(self):
        pygame.init()
        self.menu = main_menu()

    def test_start(self, event):
        pass
