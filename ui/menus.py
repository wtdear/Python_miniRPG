"""
Меню игры
"""
import os
import sys
import time

from entities.character import Character
from entities.items import Item
from entities.skills import Skill
from config import CLASS_CONFIG, SKILL_CONFIG, STARTING_EQUIPMENT
from .display import clear_screen, show_header, show_character_stats
from game_logic.combat import start_combat
from game_logic.character_creator import create_character_class
from game_logic.save_system import save_system

def main_menu():
    """Главное меню игры"""
    while True:
        clear_screen()
        print("     _______________________________________________________       ")
        print("    /\                                                      \      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
        print("    (                                                      (       ")
        print("    (                ██████╗ ██████╗  ██████╗              (       ")
        print("     )               ██╔══██╗██╔══██╗██╔════╝              )       ")
        print("    (                ██████╔╝██████╔╝██║  ███╗             (       ")
        print("     )               ██╔══██╗██╔═══╝ ██║   ██║             )       ")
        print("    (                ██║  ██║██║     ╚██████╔╝             (       ")
        print("     )               ╚═╝  ╚═╝╚═╝      ╚═════╝              )       ")
        print("    (                                                      )       ")
        print("    (><><><><><><><><><><><><><><><><><><><><><><><><><><><(       ")
        print("    (                                                      (       ")
        print("    (                  Welcome to RPG WORLD!               (       ")
        print("    (                                                      (       ")
        print("     )     You can choose the classes you want to play!     )      ")
        print("    (                                                      (       ")
        print("     )        The main goal is to complete the game!        )      ")
        print("    (                                                      (       ")
        print("     )                1. 🎮 NEW GAME                        )      ")
        print("    (                  Start a new adventure               (       ")
        print("     )                                                     )       ")
        print("    (                 2. 📂 LOAD GAME                      (       ")
        print("     )                 Continue your adventure             )       ")
        print("    (                                                      (       ")
        print("     )                3. 🚪 EXIT                           )       ")
        print("    (                  Quit the game                       (       ")
        print("    (                                                      (       ")
        print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/______________________________________________________/      ")
        print('')
        
        choice = input("Select an option (1-3): ")
        
        if choice == "1":
            clear_screen()
            print("Starting new adventure...")
            time.sleep(1)
            
            character = choose_class_menu()
            
            if character:
                clear_screen()
                print("Loading your adventure...")
                time.sleep(1)
                print(f"\nWelcome, {character.name} the {character.class_name}!")
                print("Your adventure begins now!")
                time.sleep(2)
                character_menu(character)
                
        elif choice == "2":
            character = load_game_menu()
            if character:
                clear_screen()
                print(f"Welcome back, {character.name}!")
                print("Continuing your adventure...")
                time.sleep(2)
                character_menu(character)
            else:
                # Если загрузка отменена, остаемся в главном меню
                continue
                
        elif choice == "3":
            print("Goodbye!")
            time.sleep(1)
            sys.exit()
        else:
            print("Invalid choice! Please enter 1-3.")
            time.sleep(1)


def choose_class_menu():
    """Меню выбора класса персонажа"""
    while True:
        clear_screen()
        print("     _______________________________________________________       ")
        print("    /\                                                      \      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
        print("    (                                                      (       ")
        print("    (                 CHOOSE YOUR CLASS!                   (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        print("     )                1. ⚔️  WARRIOR                         )       ")
        print("    (                  High HP and Strength                (       ")
        print("     )                 Skills: Power Attack, Shield Bash    )       ")
        print("    (                                                      (       ")
        print("     )                2. 🔮 MAGE                            )       ")
        print("    (                  High Mana and Intelligence          (       ")
        print("     )                 Skills: Fireball, Ice Shard         )       ")
        print("    (                                                      (       ")
        print("     )                3. 🏹 ARCHER                          )       ")
        print("    (                  High Agility and Precision          (       ")
        print("     )                 Skills: Precise Shot, Multi Arrow    )       ")
        print("    (                                                      (       ")
        print("     )                4. 🔙 BACK TO MAIN MENU               )       ")
        print("    (                                                      (       ")
        print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/______________________________________________________/      ")
        print('')
        
        choice = input("Select your class (1-4): ")
        
        if choice == "1":
            return create_character_with_name("warrior")
        elif choice == "2":
            return create_character_with_name("mage")
        elif choice == "3":
            return create_character_with_name("archer")
        elif choice == "4":
            return None  # Вернуться в главное меню
        else:
            print("Invalid choice! Please select 1-4.")
            time.sleep(1)


def create_character_with_name(class_type):
    """Меню создания персонажа с именем"""
    clear_screen()
    print("     _______________________________________________________       ")
    print("    /\                                                      \      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
    print("    (                                                      (       ")
    print(f"    (              CREATING {class_type.upper():^20}            (       ")
    print("     )                                                     )       ")
    print("    (                                                      (       ")
    print("     )         Enter your character's name:                )       ")
    print("    (                                                      (       ")
    print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________/      ")
    print('')
    
    while True:
        name = input("Name: ").strip()
        if name:
            character = create_character_class(class_type, name)
            
            show_character_stats(character)
            
            confirm = input("\nConfirm this character? (Y/N): ").upper()
            if confirm == "Y":
                return character
            elif confirm == "N":
                return choose_class_menu()
            else:
                print("Please enter Y or N.")
                time.sleep(1)
        else:
            print("Name cannot be empty!")
            time.sleep(1)


def character_menu(character):
    """Главное меню персонажа"""
    while True:
        clear_screen()
        print("     _______________________________________________________       ")
        print("    /\                                                      \      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
        print("    (                                                      (       ")
        print(f"    (          {character.name} - Level {character.level} {character.class_name}      (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        print("     )                1. 🗺️  EXPLORE                        )       ")
        print("    (                  Go on an adventure                  (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        print("     )                2. 📊 CHARACTER INFO                  )       ")
        print("    (                  View stats and equipment            (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        print("     )                3. 🎒 INVENTORY                       )       ")
        print("    (                  Manage items and equipment          (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        print("     )                4. ⚙️  SKILLS                         )       ")
        print("    (                  View and upgrade skills             (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        print("     )                5. 💾 SAVE GAME                       )       ")
        print("    (                  Save your progress                  (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        print("     )                6. 📂 LOAD GAME                       )       ")
        print("    (                  Load saved progress                 (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        print("     )                7. 🏠 RETURN TO MAIN MENU             )       ")
        print("    (                                                      (       ")
        print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/______________________________________________________/      ")
        print('')
        
        choice = input("Select an option (1-7): ")
        
        if choice == "1":
            explore_menu(character)
        elif choice == "2":
            show_character_stats(character)
            input("\nPress Enter to continue...")
        elif choice == "3":
            inventory_menu(character)
        elif choice == "4":
            skills_menu(character)
        elif choice == "5":
            save_game_menu(character)
        elif choice == "6":
            loaded_character = load_game_menu()
            if loaded_character:
                character = loaded_character
                print(f"Loaded {character.name}!")
                time.sleep(2)
        elif choice == "7":
            return
        else:
            print("Invalid choice!")
            time.sleep(1)


def explore_menu(character):
    """Меню исследования"""
    while True:
        clear_screen()
        print("     _______________________________________________________       ")
        print("    /\                                                      \      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
        print("    (                                                      (       ")
        print("    (                    🗺️  EXPLORE                       (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        print("     )                1. 🌲 FOREST                         )       ")
        print("    (                  Fight weak enemies                  (       ")
        print("     )                 (Level 1-3)                         )       ")
        print("    (                                                      (       ")
        print("     )                2. 🏔️  MOUNTAINS                      )       ")
        print("    (                  Fight medium enemies                (       ")
        print("     )                 (Level 3-6)                         )       ")
        print("    (                                                      (       ")
        print("     )                3. 🐉 DRAGON'S LAIR                   )       ")
        print("    (                  Fight strong enemies                (       ")
        print("     )                 (Level 7+)                          )       ")
        print("    (                                                      (       ")
        print("     )                4. 🔙 BACK                           )       ")
        print("    (                                                      (       ")
        print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/______________________________________________________/      ")
        print('')
        
        choice = input("Select a location (1-4): ")
        
        if choice == "1":
            # Лес - слабые враги
            from entities.enemies import Goblin
            enemy = Goblin(character.level)
            start_combat(character, enemy)
        elif choice == "2":
            # Горы - средние враги
            from entities.enemies import Orc
            enemy = Orc(character.level + 1)
            start_combat(character, enemy)
        elif choice == "3":
            # Логово дракона - сильные враги
            from entities.enemies import Dragon
            enemy = Dragon(character.level + 2)
            start_combat(character, enemy)
        elif choice == "4":
            return
        else:
            print("Invalid choice!")
            time.sleep(1)


def inventory_menu(character):
    """Меню инвентаря"""
    while True:
        clear_screen()
        print("     _______________________________________________________       ")
        print("    /\                                                      \      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
        print("    (                                                      (       ")
        print("    (                    🎒 INVENTORY                      (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        
        # Показать экипировку
        print("     )                EQUIPPED ITEMS:                     )       ")
        for slot, item in character.equipment.items():
            if item:
                print(f"    (          {slot:10}: {item.name:<20}       (       ")
            else:
                print(f"    (          {slot:10}: {'Empty':<20}          (       ")
        
        print("     )                                                     )       ")
        print("    (                INVENTORY ITEMS:                      (       ")
        
        # Показать инвентарь
        if character.inventory:
            for i, item in enumerate(character.inventory, 1):
                if i <= 8:  # Ограничиваем отображение
                    equipped = "(Equipped)" if item.equipped else ""
                    print(f"     )         {i}. {item.name:<20}{equipped:<12} )       ")
        else:
            print("     )                Empty                             )       ")
        
        print("    (                                                      (       ")
        print("     )               1. EQUIP ITEM                         )       ")
        print("    (                2. UNEQUIP ITEM                       (       ")
        print("     )               3. USE ITEM                           )       ")
        print("    (                4. BACK                               (       ")
        print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/______________________________________________________/      ")
        print('')
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            equip_item_menu(character)
        elif choice == "2":
            unequip_item_menu(character)
        elif choice == "3":
            use_item_menu(character)
        elif choice == "4":
            return
        else:
            print("Invalid choice!")
            time.sleep(1)


def equip_item_menu(character):
    """Меню экипировки предмета"""
    if not character.inventory:
        print("Inventory is empty!")
        time.sleep(1)
        return
    
    print("\nSelect item to equip:")
    for i, item in enumerate(character.inventory, 1):
        print(f"{i}. {item}")
    
    try:
        choice = int(input("Enter item number: "))
        if 1 <= choice <= len(character.inventory):
            item = character.inventory[choice - 1]
            
            # Определяем слот для экипировки
            if item.item_type == 'weapon':
                slot = 'weapon'
            elif item.item_type == 'armor':
                slot = 'armor'
            else:
                print("This item cannot be equipped!")
                time.sleep(1)
                return
            
            if character.equip_item(item, slot):
                print(f"Equipped {item.name}!")
                item.equipped = True
            else:
                print("Failed to equip item!")
        else:
            print("Invalid item number!")
    except ValueError:
        print("Please enter a number!")
    
    time.sleep(1)


def unequip_item_menu(character):
    """Меню снятия предмета"""
    print("\nSelect slot to unequip:")
    slots = ['weapon', 'armor', 'helmet', 'gloves', 'boots', 'accessory']
    
    equipped_slots = []
    for i, slot in enumerate(slots, 1):
        if character.equipment[slot]:
            print(f"{i}. {slot}: {character.equipment[slot].name}")
            equipped_slots.append(slot)
    
    if not equipped_slots:
        print("No items equipped!")
        time.sleep(1)
        return
    
    try:
        choice = int(input("Enter slot number: "))
        if 1 <= choice <= len(equipped_slots):
            slot = equipped_slots[choice - 1]
            item = character.unequip_item(slot)
            if item:
                item.equipped = False
                print(f"Unequipped {item.name}!")
        else:
            print("Invalid slot number!")
    except ValueError:
        print("Please enter a number!")
    
    time.sleep(1)


def use_item_menu(character):
    """Меню использования предмета"""
    # В этой версии только зелья можно использовать
    potions = [item for item in character.inventory if item.item_type == 'potion']
    
    if not potions:
        print("No usable items in inventory!")
        time.sleep(1)
        return
    
    print("\nSelect potion to use:")
    for i, potion in enumerate(potions, 1):
        print(f"{i}. {potion}")
    
    try:
        choice = int(input("Enter potion number: "))
        if 1 <= choice <= len(potions):
            potion = potions[choice - 1]
            result = potion.use(character)
            print(result)
            character.remove_from_inventory(potion)
        else:
            print("Invalid potion number!")
    except ValueError:
        print("Please enter a number!")
    
    time.sleep(2)


def skills_menu(character):
    """Меню навыков"""
    while True:
        clear_screen()
        print("     _______________________________________________________       ")
        print("    /\                                                      \      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
        print("    (                                                      (       ")
        print("    (                    ⚙️  SKILLS                        (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        
        # Показать навыки
        print(f"     )         Skill Points: {character.skill_points:<3}                 )       ")
        print("    (                                                      (       ")
        
        for i, skill in enumerate(character.skills, 1):
            info = skill.get_info()
            print(f"     )         {i}. {info['name']:<20} Lvl {info['level']:<2}       )       ")
            print(f"    (            MP: {info['mana_cost']:<3} Damage: {info['damage']:<4}            (       ")
            print(f"     )           {info['description']:<30}   )       ")
            print("    (                                                      (       ")
        
        print("     )               1. UPGRADE SKILL                       )       ")
        print("    (                2. BACK                                (       ")
        print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/______________________________________________________/      ")
        print('')
        
        choice = input("Select an option (1-2): ")
        
        if choice == "1":
            upgrade_skill_menu(character)
        elif choice == "2":
            return
        else:
            print("Invalid choice!")
            time.sleep(1)


def upgrade_skill_menu(character):
    """Меню улучшения навыков"""
    if character.skill_points <= 0:
        print("No skill points available!")
        time.sleep(1)
        return
    
    print("\nSelect skill to upgrade:")
    for i, skill in enumerate(character.skills, 1):
        info = skill.get_info()
        print(f"{i}. {info['name']} (Level {info['level']}/{skill.max_level})")
    
    try:
        choice = int(input("Enter skill number: "))
        if 1 <= choice <= len(character.skills):
            skill = character.skills[choice - 1]
            if skill.level < skill.max_level:
                if character.skill_points > 0:
                    skill.upgrade()
                    character.skill_points -= 1
                    print(f"Upgraded {skill.name} to level {skill.level}!")
                else:
                    print("Not enough skill points!")
            else:
                print("Skill is already at maximum level!")
        else:
            print("Invalid skill number!")
    except ValueError:
        print("Please enter a number!")
    
    time.sleep(2)


def save_game_menu(character):
    """Меню сохранения игры"""
    while True:
        clear_screen()
        print("     _______________________________________________________       ")
        print("    /\                                                      \      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
        print("    (                                                      (       ")
        print("    (                    💾 SAVE GAME                      (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        
        # Показать существующие сохранения
        saves = save_system.get_save_files()
        if saves:
            print("     )            EXISTING SAVES:                      )       ")
            for i, save in enumerate(saves[:5], 1):  # Показываем только 5 последних
                save_name = save['filename'].replace('.rpg_save', '')
                date_str = save['modified'].strftime("%Y-%m-%d %H:%M")
                print(f"    (          {i}. {save_name:<20} {date_str}  (       ")
        else:
            print("     )            No saved games found                )       ")
        
        print("     )                                                     )       ")
        print("    (                1. QUICK SAVE                         (       ")
        print("     )                 (Auto-named)                        )       ")
        print("    (                2. NAMED SAVE                         (       ")
        print("     )                 (Choose name)                       )       ")
        print("    (                3. BACK                               (       ")
        print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/______________________________________________________/      ")
        print('')
        
        choice = input("Select an option (1-3): ")
        
        if choice == "1":
            success, message = save_system.save_game(character, "auto")
            print(f"\n{message}")
            time.sleep(2)
            return
        elif choice == "2":
            named_save_menu(character)
            return
        elif choice == "3":
            return
        else:
            print("Invalid choice!")
            time.sleep(1)


def named_save_menu(character):
    """Меню именованного сохранения"""
    clear_screen()
    print("     _______________________________________________________       ")
    print("    /\                                                      \      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
    print("    (                                                      (       ")
    print("    (                NAMED SAVE                            (       ")
    print("     )                                                     )       ")
    print("    (                                                      (       ")
    print("     )         Enter save name:                            )       ")
    print("    (          (letters, numbers, underscores only)       (       ")
    print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________/      ")
    print('')
    
    while True:
        save_name = input("Save name: ").strip()
        
        if not save_name:
            print("Save name cannot be empty!")
            continue
        
        # Проверяем допустимость имени файла
        import re
        if not re.match(r'^[a-zA-Z0-9_-]+$', save_name):
            print("Invalid save name! Use only letters, numbers, underscores and hyphens.")
            continue
        
        success, message = save_system.save_game(character, save_name)
        print(f"\n{message}")
        time.sleep(2)
        return


def load_game_menu():
    """Меню загрузки игры"""
    while True:
        clear_screen()
        print("     _______________________________________________________       ")
        print("    /\                                                      \      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/      ")
        print("    (                                                      (       ")
        print("    (                   📂 LOAD GAME                       (       ")
        print("     )                                                     )       ")
        print("    (                                                      (       ")
        
        saves = save_system.get_save_files()
        
        if not saves:
            print("     )            No saved games found                )       ")
            print("    (                                                      (       ")
            print("     )                Press Enter to return               )       ")
            print("    (                                                      (       ")
            print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
            print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
            print("    \/______________________________________________________/      ")
            print('')
            input("Press Enter to continue...")
            return None
        
        print("     )            SELECT SAVE FILE:                       )       ")
        
        # Показываем сохранения
        for i, save in enumerate(saves, 1):
            save_name = save['filename'].replace('.rpg_save', '')
            date_str = save['modified'].strftime("%m/%d %H:%M")
            char_info = ""
            
            # Пытаемся получить информацию о персонаже
            try:
                character, _ = save_system.load_game(save['filename'])
                if character:
                    char_info = f"{character.name} Lvl {character.level}"
            except:
                pass
            
            if char_info:
                print(f"    (          {i}. {save_name:<15} {char_info:<20} {date_str}  (       ")
            else:
                print(f"    (          {i}. {save_name:<15} {'':<20} {date_str}  (       ")
        
        print("     )                                                     )       ")
        print("    (                0. BACK                                (       ")
        print("    (                D. DELETE SAVE                         (       ")
        print("    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\      ")
        print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
        print("    \/______________________________________________________/      ")
        print('')
        
        choice = input("Select save (1-9, 0 to back, D to delete): ").upper()
        
        if choice == "0":
            return None
        elif choice == "D":
            delete_save_menu(saves)
            continue
        else:
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= len(saves):
                    selected_save = saves[choice_num - 1]
                    character, message = save_system.load_game(selected_save['filename'])
                    
                    if character:
                        print(f"\n{message}")
                        return character
                    else:
                        print(f"\nFailed to load: {message}")
                        time.sleep(2)
                else:
                    print("Invalid selection!")
                    time.sleep(1)
            except ValueError:
                print("Invalid input!")
                time.sleep(1)


def delete_save_menu(saves):
    """Меню удаления сохранения"""
    print("\nSelect save to delete:")
    for i, save in enumerate(saves, 1):
        save_name = save['filename'].replace('.rpg_save', '')
        date_str = save['modified'].strftime("%Y-%m-%d")
        print(f"{i}. {save_name} ({date_str})")
    
    try:
        choice = int(input("Enter number (0 to cancel): "))
        if choice == 0:
            return
        
        if 1 <= choice <= len(saves):
            selected_save = saves[choice - 1]
            confirm = input(f"Delete '{selected_save['filename']}'? (Y/N): ").upper()
            
            if confirm == "Y":
                success, message = save_system.delete_save(selected_save['filename'])
                print(message)
                time.sleep(2)
            else:
                print("Deletion cancelled.")
                time.sleep(1)
        else:
            print("Invalid selection!")
            time.sleep(1)
    except ValueError:
        print("Invalid input!")
        time.sleep(1)