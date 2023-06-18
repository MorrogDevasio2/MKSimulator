import random, os, pygame
from pynput import keyboard

press_sounds = ['GENERIC_R0.mp3','GENERIC_R1.mp3','GENERIC_R2.mp3','GENERIC_R3.mp3','GENERIC_R4.mp3']

key_db = []

pygame.init()

def on_key_down(key):
    if key == keyboard.Key.enter:
        if key in key_db:
            return
        key_db.append(key)
        enter_file = 'brownkeys/press/ENTER.mp3'
        enter_sound = pygame.mixer.Sound(enter_file)
        enter_sound.play()
    elif key == keyboard.Key.backspace:
        if key in key_db:
            return
        key_db.append(key)
        backspace_file = 'brownkeys/press/BACKSPACE.mp3'
        backspace_sound = pygame.mixer.Sound(backspace_file)
        backspace_sound.play()
    elif key == keyboard.Key.space:
        if key in key_db:
            return
        key_db.append(key)
        space_file = 'brownkeys/press/SPACE.mp3'
        space_sound = pygame.mixer.Sound(space_file)
        space_sound.play()
    else:
        if key in key_db:
            return
        key_db.append(key)
        sound_file = f'brownkeys/press/{press_sounds[random.randint(0, (press_sounds.__len__() - 1))]}'
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

def on_key_up(key):
    if key == keyboard.Key.enter:
        if key in key_db:
            key_db.remove(key)
        enter_file = 'brownkeys/release/ENTER.mp3'
        enter_sound = pygame.mixer.Sound(enter_file)
        enter_sound.play()
    elif key == keyboard.Key.backspace:
        if key in key_db:
            key_db.remove(key)
        backspace_file = 'brownkeys/release/BACKSPACE.mp3'
        backspace_sound = pygame.mixer.Sound(backspace_file)
        backspace_sound.play()
    elif key == keyboard.Key.space:
        if key in key_db:
            key_db.remove(key)
        space_file = 'brownkeys/release/SPACE.mp3'
        space_sound = pygame.mixer.Sound(space_file)
        space_sound.play()
    else:
        if key in key_db:
            key_db.remove(key)
        sound_file = 'brownkeys/release/GENERIC.mp3'
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

listener = keyboard.Listener(on_press=on_key_down, on_release=on_key_up)

listener.start()

listener.join()


