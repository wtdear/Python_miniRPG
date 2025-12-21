"""
Функции отображения и UI утилиты
"""
import os
import time

def clear_screen():
    """Очистить экран"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Показать заголовок с рамкой"""
    print("     _______________________________________________________       ")
    print("    /\                                                      \      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
    print(f"    (                 {title:^40}                (       ")
    print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________/      ")

def show_box(content_lines):
    """Показать текст в рамке"""
    print("     _______________________________________________________       ")
    print("    /\                                                      \      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
    
    for line in content_lines:
        print(f"    (          {line:<40}                (       ")
    
    print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________/      ")

def show_character_stats(character):
    """Показать статистику персонажа"""
    clear_screen()
    print("     _______________________________________________________       ")
    print("    /\                                                      \      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
    print("    (                                                      (       ")
    print(f"    (              CHARACTER CREATED!                     (       ")
    print("     )                                                     )       ")
    print("    (                                                      (       ")
    print(f"     )         Name: {character.name:<20}              )       ")
    print(f"    (          Class: {character.class_name:<20}       (       ")
    print("     )                                                     )       ")
    print("    (                  STATISTICS:                         (       ")
    print("     )                                                     )       ")
    print(f"    (          Health: {character.get_stat('health'):<4}/{character.get_stat('max_health'):<4}          (       ")
    print(f"     )         Mana:   {character.get_stat('mana'):<4}/{character.get_stat('max_mana'):<4}            )       ")
    print(f"    (          Strength: {character.get_stat('strength'):<3}                    (       ")
    print(f"     )         Agility:   {character.get_stat('agility'):<3}                  )       ")
    print(f"    (          Intelligence: {character.get_stat('intelligence'):<3}              (       ")
    print("     )                                                     )       ")
    print("    (                  SKILLS:                             (       ")
    
    for i, skill in enumerate(character.skills, 1):
        if i <= 3:
            print(f"     )         {i}. {skill.name:<15}                    )       ")
    
    print("    (                                                      (       ")
    print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________/      ")

def show_combat_screen(player, enemy, message=""):
    """Показать экран боя"""
    clear_screen()
    print("     _______________________________________________________       ")
    print("    /\                                                      \      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
    print("    (                                                      (       ")
    print("    (                    ⚔️  COMBAT!                        (       ")
    print("     )                                                     )       ")
    print("    (                                                      (       ")
    
    # Информация об игроке
    print(f"     )         PLAYER: {player.name:<20}             )       ")
    print(f"    (          HP: {player.get_stat('health'):<4}/{player.get_stat('max_health'):<4} MP: {player.get_stat('mana'):<4}/{player.get_stat('max_mana'):<4}        (       ")
    print("     )                                                     )       ")
    
    # Разделитель
    print("    (                 VS                                   (       ")
    print("     )                                                     )       ")
    
    # Информация о враге
    print(f"    (          ENEMY: {enemy.name:<20}                (       ")
    print(f"     )         HP: {enemy.health:<4}/{enemy.max_health:<4} Level: {enemy.level:<3}           )       ")
    print("    (                                                      (       ")
    
    # Сообщение о действии
    if message:
        print(f"     )         {message:<40}         )       ")
        print("    (                                                      (       ")
    
    print("     )                ACTIONS:                             )       ")
    print("    (                1. ATTACK                             (       ")
    print("     )               2. USE SKILL                          )       ")
    print("    (                3. USE ITEM                           (       ")
    print("     )               4. FLEE                               )       ")
    print("    (                                                      (       ")
    print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________/      ")
    print('')

def print_colored(text, color):
    """Вывести цветной текст (если поддерживается)"""
    colors = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'PURPLE': '\033[95m',
        'CYAN': '\033[96m',
        'WHITE': '\033[97m',
        'BOLD': '\033[1m',
        'END': '\033[0m'
    }
    
    color_code = colors.get(color.upper(), colors['WHITE'])
    print(f"{color_code}{text}{colors['END']}")

def show_progress_bar(current, maximum, length=20):
    """Показать прогресс бар"""
    filled = int((current / maximum) * length)
    bar = '█' * filled + '░' * (length - filled)
    return f"[{bar}] {current}/{maximum}"

def animate_text(text, delay=0.03):
    """Анимированный вывод текста"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()