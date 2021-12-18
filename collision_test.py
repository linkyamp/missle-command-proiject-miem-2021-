import unittest
from collision import promah
from collision import puli

import pygame
import random
Rect1 = Rect2 = pygame.Rect(random.randint(10, 1000), 0, 40, 40)
Rect3 = pygame.Rect(100001, 0, 40, 40)


class TestPuli(unittest.TestCase):
    def test_puli(self):
        self.assertEqual(puli(Rect1, Rect2, random.randint(100, 1000), random.randint(100, 1000)), 1)

    def test_promah(self):
        self.assertEqual(promah(Rect1, Rect3, random.randint(100, 1000), random.randint(100, 1000)), 0)


if __name__ == '__name__':
    unittest.main()
