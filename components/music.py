import pygame


def music():
    pygame.init()
    pygame.mixer.music.load('./music/overpass.mp3')
    pygame.mixer.music.play()
    input('parar musica')