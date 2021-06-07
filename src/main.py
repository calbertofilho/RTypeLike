'''
Game R-Type Like
Utilizando a biblioteca: PyGame

Criado por: Carlos Alberto Morais Moura Filho
Versão: 1.0
Atualizado em: 07/06/2021
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
from src.lib.functions import (
    init_game, pause_game, close_game,
    create_screen,
    handle, controls
)



# Constantes
SCREEN_WIDTH, SCREEN_HEIGHT = (1366, 768)                            # Comprimento e altura da tela
SCREEN_DIMENSION = (SCREEN_WIDTH, SCREEN_HEIGHT)                     # Dimensão da tela
BACKGROUND_COLOR = (8, 17, 26)                                       # Cor do fundo
FPS = 30                                                             # Valor do FRAMERATE



def main():
    '''Função principal'''
    init_game()
    screen = create_screen(MAIN_DIR, SCREEN_DIMENSION)
    clock = pygame.time.Clock()                                      # Controle do tempo

    while True:
        clock.tick(FPS)                                              # Controle do FRAMERATE do jogo
        pygame.Surface.fill(screen, BACKGROUND_COLOR)                # Preenche o fundo com uma cor
        handle()                                                     # Trata os eventos do jogo
        controls()                                                   # Trata os controles do jogo
        pygame.display.update()                                      # Atualização de tela



try:
    if __name__ == "__main__":
        main()
except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as exception:
    print(f"Oops! {exception.__class__} occurred.\n{exception.args}")
finally:
    close_game()
