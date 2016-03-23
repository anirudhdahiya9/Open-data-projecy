#! /usr/bin/env python

import os, sys
import pygame
from pygame.locals import *

#method to load the images into the sprites
def load_image(name, colorkey=None):
    path = os.path.join('data', 'images')
    path = os.path.join(path, name)

    try:
        image = pygame.image.load(path)
    except pygame.error, message:
        print 'Cannot load image:', path
        raise SystemExit, message

    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)

    return image

#method to load the background audio
def load_sound(name):
    
    path = os.path.join('data', 'audio')
    path = os.path.join('audio', name)
    try:
        sound = pygame.mixer.Sound(path)
    except pygame.error, message:
        print 'Cannot load sound:', path
        raise SystemExit, message

    sound = pygame.mixer.Sound(path)
    return sound

#method to stop the background audio
def stop_sound(sound):
    sound.stop()

#method to display text on the screen
def messageDisplay(screen, xpos, ypos, message, color, size):
    font = pygame.font.Font(None, size)
    screentext = font.render(message, True, color)
    textpos = screentext.get_rect()
    textpos.centerx = xpos
    textpos.centery = ypos
    screen.blit(screentext, textpos)
    


