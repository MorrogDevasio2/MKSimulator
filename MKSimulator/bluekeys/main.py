import random, os, pygame
from pynput import keyboard

press_sounds = ['GENERIC_R0.mp3','GENERIC_R1.mp3','GENERIC_R2.mp3','GENERIC_R3.mp3','GENERIC_R4.mp3']

key_db = []

pygame.init()

def on_key_down(key):
    if key in key_db:
        return
    key_db.append(key)
    sound_file = f'bluekeys/press/{press_sounds[random.randint(0, (press_sounds.__len__() - 1))]}'
    sound = pygame.mixer.Sound(sound_file)
    sound.play()

def on_key_up(key):
    if key in key_db:
        key_db.remove(key)
    sound_file = 'bluekeys/release/GENERIC.mp3'
    sound = pygame.mixer.Sound(sound_file)
    sound.play()

listener = keyboard.Listener(on_press=on_key_down, on_release=on_key_up)

listener.start()

listener.join()


