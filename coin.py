import pygame

class Coin(pygame.Rect):
    def __init__(this, x, y, sprite):
        super().__init__(x, y, 25, 25)
        this.x = x
        this.y = y
        this.r = 12.5
        this.sprite = sprite