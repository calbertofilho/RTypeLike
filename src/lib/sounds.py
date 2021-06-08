import os
import sys
import time
import pygame
from pygame.locals import *
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(__file__)                                # Diretório atual
MAIN_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)) # Diretório do jogo
sys.path.append(MAIN_DIR)                                             # Adição do diretório do jogo
SOUNDS_LOCAL = 'res/sounds'
VOLUME_BGM = 0.6
VOLUME_FX = 0.8

BGM = {
    'main': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'main-title.mid'),
    'one': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'stage-1.mid'),
    'two': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'stage-2.mid'),
    'three': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'stage-3.mid'),
    'four': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'stage-4.mid'),
    'five': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'stage-5.mid'),
    'six': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'stage-6.mid'),
    'seven': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'stage-7.mid'),
    'eight': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'stage-8.mid'),
    'clear': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'stage-clear_NOLOOP.mid'),
    'boss': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'boss.mid'),
    'end': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'ending.mid'),
    'death': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'bgm', 'game-over_NOLOOP.mid')
}

extension = 'wav' if 'win' in sys.platform else 'ogg'           # Decisão do tipo de áudio
FX = {
    'start': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'fx', f'start.{extension}'),
    'laser': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'fx', f'laser.{extension}'),
    'death': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'fx', f'death.{extension}'),
    'explosion': os.path.join(MAIN_DIR, SOUNDS_LOCAL, 'fx', f'explosion.{extension}')
}

def wait(delay):
    '''Função que atrasa a execução do código por um tempo determinado em segundos'''
    time_to_delay = time.time() + delay                              # Tempo inicial mais o delay
    while time.time() <= time_to_delay:                              # Enquanto não passar o delay
        pygame.display.update()                                      # Não faz nada

def play_bgm(track, loop):
    '''Função para executar a música de fundo do jogo'''
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(BGM[track])                          # Carrega a música pra executar
        pygame.mixer.music.set_volume(VOLUME_BGM)                    # Configura o volume
        if loop:
            pygame.mixer.music.play(loops = -1)                      # Executa a música em loop

def pause_bgm(state):
    '''Função para suspender e resumir a música de fundo do jogo'''
    if pygame.mixer.music.get_busy():                                # Testa se há algo tocando
        if state is True:                                            # Se recebeu o valor True
            pygame.mixer.music.pause()                               # Pausa a execução
    else:                                                            # Se não há playback
        if state is False:                                           # Se recebeu o valor False
            pygame.mixer.music.unpause()                             # Retorna a execução

def stop_bgm(delay):
    '''Função para para a música de fundo do jogo'''
    pygame.mixer.music.fadeout(delay)                                # Executa o fadeout da música
    wait(delay / 1000)                                               # Transforma em segundos e espera
    pygame.mixer.music.stop()                                        # Para a execução da música

def play_fx(effect):
    sound_fx = pygame.mixer.Sound(FX[effect])                        # Carrega o efeito sonoro
    sound_fx.set_volume(VOLUME_FX)                                   # Configura o volume
    pygame.mixer.Sound.play(sound_fx)                                # Executa o efeito sonoro
