import pygame
class Settins:
    def __init__(self):
        self.bg_color = (75,0,130)
        self.scree_width = 600
        self.screen_height = 700
        self.image = pygame.image.load("images (1).jpg")




        #soeed


        #bullet_settings

        self.bullet_width = 500
        self.bullet_height = 7
        self.bullet_color = (238, 75, 43)
        self.bullet_allow = 10
        #alien setting

        self.fleet_drop_speed = 10
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.iniatialize_dynamic_settings()

    def iniatialize_dynamic_settings(self):
        self.alien_speed = 2.1
        self.bullet_speed = 3
        self.ship_speed = 1.5
        self.fleet_direction = 1
        self.alien_point = 50

    def increse_speed(self):
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.speedup_scale)

