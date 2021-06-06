'''
Game R-Type Like
Utilizando a biblioteca: PyGame

Criado por: Carlos Alberto Morais Moura Filho
Versão: 1.0
Atualizado em: 06/06/2021
'''

# pylint: disable=no-member
# pylint: disable=c-extension-no-member
# pylint: disable=no-name-in-module

import os
from lib.functions import ( close_game )
import pygame
from pygame.constants import ( QUIT, KEYDOWN, K_ESCAPE )

MAIN_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..")) # Diretorio do jogo
SCREEN_WIDTH = 1024                                                  # Comprimento da tela
SCREEN_HEIGHT = 768                                                  # Altura da tela
SCREEN_DIMENSION = (SCREEN_WIDTH, SCREEN_HEIGHT)                     # Dimensão da tela
BACKGROUND = (8, 17, 26)                                             # Cor do fundo
FPS = 30                                                             # Exibição dos frames p/segundo

def main():
    '''Função principal'''
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
    screen = pygame.display.set_mode(SCREEN_DIMENSION)
    pygame.Surface.fill(screen, BACKGROUND)
    icon = pygame.image.load(f'{MAIN_DIR}/res/images/icons/icon.png').convert_alpha()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Game R-Type Like')
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                close_game()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    close_game()
        pygame.display.update()

try:
    if __name__ == "__main__":
        main()
except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as exc:
    print(f"Oops! {exc.__class__} occurred.\n{exc.args}")
finally:
    close_game()
