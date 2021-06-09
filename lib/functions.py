# pylint: disable=no-member

import os
import sys
import pygame
from pygame.locals import *
from pygame.constants import (
    QUIT, KEYDOWN,
    K_ESCAPE, K_PAUSE, K_SPACE, K_LSHIFT,
    K_RETURN, K_LEFT, K_RIGHT, K_UP, K_DOWN
)



BEGIN = False



def init_libs(quality):
    '''Função que inicializa as bibliotecas do jogo'''
    if quality == 'high':                                            # Decisão da qualidade de som
        buf = 2048                                                   # Alta qualidade
    elif quality == 'mid':
        buf = 1024                                                   # Qualidade média
    else:
        buf = 512                                                    # Qualidade baixa
    pygame.init()
    pygame.display.init()
    pygame.mixer.pre_init(
        frequency = 44100,
        size = 16,
        channels = 1,
        buffer = buf
    )
    pygame.key.set_repeat()
def begin_game():
    '''Função que sinaliza o início do jogo e a saída da tela de abertura'''
    global BEGIN
    BEGIN = not(BEGIN)
def pause_game(state):
    '''Função que suspende a execução do jogo temporariamente'''
    pass
def close_game():
    '''Função que encerra todas as bibliotecas e fecha o jogo'''
    pygame.display.quit()
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()



def create_screen(screen_dimension, icon, title):
    '''Função que cria a tela onde jogo é exibido'''
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_mode(screen_dimension)
    pygame.display.set_icon(icon.convert_alpha())
    pygame.display.set_caption(title)
    return pygame.display.get_surface()
def splash(screen, image):
    '''Função que exibe a tela de abertura do jogo'''
    screen.blit(image, (0, 0))
    pygame.display.update()
    while not(BEGIN):
        handle(escape = True, pause = False, enter = True)
        return BEGIN
def setup_environment():
    '''Função que reinicia todas as variáveis do jogo'''
    global BEGIN
    BEGIN = False
    pass



def handle(escape, pause, enter):
    '''Função que gerencia os eventos do jogo'''
    for event in pygame.event.get():                                 # Identifica os eventos
        if event.type == QUIT:                                       # Evento: Fechar a janela
            close_game()                                             # Chamada da função de fechar
        if event.type == KEYDOWN:                                    # Evento: Pressionar tecla
            if escape:
                if event.key == K_ESCAPE:                            # Testa se a tecla é "ESC"
                    close_game()                                     # Chamada da função de fechar
            if pause:
                if event.key == K_PAUSE:                             # Testa se a tecla é "PAUSE"
                    pause_game(pause)                                # Chamada da função de pausar
            if enter:
                if event.key == K_RETURN or event.key == K_KP_ENTER: # Testa se a tecla é "ENTER"
                    begin_game()                                     # Chamada da função de início
def controls():
    '''Função que gerencia as teclas pressionadas do jogo'''
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
