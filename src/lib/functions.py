# pylint: disable=no-member

import os
import sys
import pygame
from pygame.constants import (
    K_LSHIFT, QUIT, KEYDOWN,
    K_ESCAPE, K_PAUSE,
    K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE
)



def init_game():
    pygame.init()
    pygame.display.init()
    pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
    pygame.key.set_repeat()
def pause_game(state):
    pass
def close_game():
    pygame.display.quit()
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()



def create_screen(main_dir, screen_dimension):
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_mode(screen_dimension)
    icon = pygame.image.load(os.path.join(main_dir, 'res\images\icons', 'icon.png')).convert_alpha()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Game R-Type Like')
    return pygame.display.get_surface()



def handle():
    for event in pygame.event.get():                                 # Identifica os eventos
        if event.type == QUIT:                                       # Evento: Fechar a janela
            close_game()                                             # Chamada da função de fechar
        if event.type == KEYDOWN:                                    # Evento: Pressionar tecla
            if event.key == K_ESCAPE:                                # Testa se a tecla é "ESC"
                close_game()                                         # Chamada da função de fechar
            if event.key == K_PAUSE:                                 # Testa se a tecla é "PAUSE"
                pause_game(True)                                     # Chamada da função de pausar
def controls():
    commands = pygame.key.get_pressed()                              # Captura as teclas pressionadas
    if commands[K_LEFT]:                                             # Testa se a tecla é "←"
        print('Seta para esquerda')
    if commands[K_RIGHT]:                                            # Testa se a tecla é "→"
        print('Seta para direita')
    if commands[K_UP]:                                               # Testa se a tecla é "↑"
        print('Seta para cima')
    if commands[K_DOWN]:                                             # Testa se a tecla é "↓"
        print('Seta para baixo')
    if commands[K_SPACE]:                                            # Testa se a tecla é "Espaço"
        print('Espaço')
    if commands[K_LSHIFT]:                                           # Testa se a tecla é "Shift Esquerdo"
        print('Shift esquerdo')
