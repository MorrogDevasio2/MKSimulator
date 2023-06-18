'''
Coder: Morrog Devasio

Credis Sounds etc:
website: https://kbs.im/
github: https://github.com/tplai/kbsim
'''

try:
    from pynput import keyboard
    import pygame
    import os,time
except:
    import os,time
    print('Libraries not installed!')
    while True:
        answer = input('Would you lke to install them? (y/N): ').lower()
        if answer == 'y':
            os.system('pip3 install -r requirements.txt')
            from pynput import keyboard
            import pygame
            import os,time
            break
        elif answer == 'n':
            print('You chose not to install them')
            print('exiting...')
            quit()

print('Please hold tight!\n\n')
time.sleep(5)

print('''
  __  __ _  __ _____ _                 _       _ 
 |  \/  | |/ // ____(_)               | |     | |
 | \  / | ' /| (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
 | |\/| |  <  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
 | |  | | . \ ____) | | | | | | | |_| | | (_| | || (_) | |
 |_|  |_|_|\_\_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|
 [Made by Morrog#8989]\n        
''')

print('Welcome user\n\n')


def show_options():
    print('Here are all the options(more comming soon!)\n')
    print('[1]', 'Blackkeys')
    print('[2]', 'Bluekeys')
    print('[3]', 'Brownkeys\n')
    print('[x]', 'Show options again'+'       '+'[z]', 'Credits')


def roll_credits():
    print('''
    Coder: Morrog Devasio\n
    Credis Sounds etc:
    website: https://kbs.im/
    github: https://github.com/tplai/kbsim
    ''')


posible_answers = ['1','2','3','x','z']

answers = {
    '1': 'blackkeys',
    '2': 'bluekeys',
    '3': 'brownkeys',
    'x': 'options',
    'z': 'credits'
           }

show_options()


while True:
    choice = input('Whats would you like to chose: ').lower()
    if choice in posible_answers:
        if choice == '1':
            print(f'You chose option {choice}')
            os.system(f'python3 {answers[choice]}/main.py')
        elif choice == '2':
            print(f'You chose option {choice}')
            os.system(f'python3 {answers[choice]}/main.py')
        elif choice == '3':
            print(f'You chose option {choice}')
            os.system(f'python3 {answers[choice]}/main.py')
        elif choice == 'x':
            show_options()
        elif choice == 'z':
            roll_credits()
    else:
        print('Sorry i did not fully understand that')
        
        

