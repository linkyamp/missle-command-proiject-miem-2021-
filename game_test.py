import unittest
from collision import promah
from collision import puli

import pygame
import random



class TestPuli(unittest.TestCase):
    def test_puli(self):
        self.assertEqual(puli[pygame.Rect(random.randint(10, 1000), 0, 40, 40), pygame.Rect(random.randint(10, 1000), 0, 40, 40), random.randint(100, 1000), random.randint(100, 1000)], 0)
