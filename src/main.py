'''
Game R-Type Like
Utilizando a biblioteca: PyGame

Criado por: Carlos Alberto Morais Moura Filho
Versão: 1.0
Atualizado em: 09/06/2021
'''
# pylint: disable=no-member
# pylint: disable=c-extension-no-member
# pylint: disable=no-name-in-module



# Importação das bibliotecas e dependências
import os
import sys
import pygame
from pygame.locals import *
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(__file__)                                # Diretório atual
MAIN_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)) # Diretório do jogo
sys.path.append(MAIN_DIR)                                             # Adição do diretório do jogo
from lib.functions import (
    init_libs, close_game,
    create_screen, splash, setup_environment,
    handle, controls
)
from lib.sounds import (
    play_bgm, pause_bgm, stop_bgm,
    play_fx
)
from classes.test import (
    funcao
)



# Constantes
SCREEN_WIDTH, SCREEN_HEIGHT = (1366, 768)                            # Comprimento e altura da tela
SCREEN_DIMENSION = (SCREEN_WIDTH, SCREEN_HEIGHT)                     # Dimensão da tela
BACKGROUND_COLOR = (8, 17, 26)                                       # Cor do fundo
ICON_FILE = os.path.normpath(os.path.join(MAIN_DIR, 'res\\images\\icons', 'icon.png'))   # Local do ícone
SPLASH_SCREEN = os.path.normpath(os.path.join(MAIN_DIR, 'res\\images\\messages', 'splash.png')) # Local da tela de abertura
FPS = 30                                                             # Valor do FRAMERATE
NEBULA = os.path.normpath(os.path.join(MAIN_DIR, 'res\\images\\assets', 'nebula.png'))
PLANETS = os.path.normpath(os.path.join(MAIN_DIR, 'res\\images\\assets', 'planets.png'))
BLACK_HOLE = os.path.normpath(os.path.join(MAIN_DIR, 'res\\images\\assets', 'black-hole.png'))
START_POS = 1366
ACCELERATION, ACCELERATION_STARS = (0.02, 0.05)



def main():
    '''Função principal'''
    init_libs('high')                                                      # Inicialização das bibliotecas
    icon = pygame.image.load(ICON_FILE)                              # Ícone da janela do jogo
    screen = create_screen(SCREEN_DIMENSION, icon, 'Game R-Type Like') # Criação da tela do jogo
    clock = pygame.time.Clock()                                      # Controle do tempo
    play_bgm('main', loop = True)
    funcao()
    while True:                                                      # Loop do jogo
        clock.tick(FPS)                                              # Controle do FRAMERATE do jogo
        running = splash(screen, pygame.image.load(SPLASH_SCREEN))   # Tela de abertura do jogo
        if running:
            play_fx('start')                                         # Executa o efeito sonoro de inicio
            stop_bgm(1500)                                           # Para a execução da música título
        setup_environment()                                          # Reinicia as variaveis do jogo
        image1 = pygame.transform.scale(pygame.image.load(PLANETS).convert_alpha(), (1024, 768))
        image2 = pygame.transform.scale(pygame.image.load(BLACK_HOLE).convert_alpha(), (395,360))
        image3 = pygame.transform.scale(pygame.image.load(NEBULA).convert_alpha(), (450, 450))
        image1_pos_x = START_POS + 0
        image2_pos_x = START_POS + 1500
        image3_pos_x = START_POS + 2200
        while running:                                               # Loop de execução do jogo
            play_bgm('lvl1', loop = True)
            pygame.Surface.fill(screen, BACKGROUND_COLOR)            # Preenche o fundo com uma cor
            image1_pos_x -= ACCELERATION
            image2_pos_x -= ACCELERATION
            image3_pos_x -= ACCELERATION
            screen.blit(image1, (image1_pos_x,-20))
            screen.blit(image2, (image2_pos_x,10))
            screen.blit(image3, (image3_pos_x,330))
            handle(escape = False, pause = True, enter = False)      # Trata os eventos do jogo
            controls()                                               # Trata os controles do jogo
            pygame.display.update()                                  # Atualização de tela



try:
    if __name__ == "__main__":
        main()
except SyntaxError as syntax_exception:
    print(f'Oops! Ocorreu um erro de sintaxe no código.\n\
        __class__ = {syntax_exception.__class__}\n\
        __doc__ = {syntax_exception.__doc__}\n\
        args = {syntax_exception.args}')
except (ValueError, ZeroDivisionError) as value_exception:
    print(f'Oops! Ocorreu um erro de valores.\n\
        __class__ = {value_exception.__class__}\n\
        __doc__ = {value_exception.__doc__}\n\
        args = {value_exception.args}')
except TypeError as type_exception:
    print(f'Oops! Ocorreu um erro de conversão de tipo de dados.\n\
        __class__ = {type_exception.__class__}\n\
        __doc__ = {type_exception.__doc__}\n\
        args = {type_exception.args}')
except Exception as general_exception:
    print(f'Oops! Ocorreu um erro não identificado.\n\
        __class__ = {general_exception.__class__}\n\
        __doc__ = {general_exception.__doc__}\n\
        args = {general_exception.args}')
finally:
    close_game()
