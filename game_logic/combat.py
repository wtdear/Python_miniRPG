"""
Боевая система
"""
import time
import random
from ui.display import show_combat_screen, print_colored

def start_combat(player, enemy):
    """Начать бой"""
    print(f"\nA wild {enemy.name} appears!")
    time.sleep(1)
    
    while player.get_stat('health') > 0 and enemy.alive:
        # Ход игрока
        player_turn(player, enemy)
        
        if not enemy.alive:
            victory(player, enemy)
            break
        
        # Ход врага
        enemy_turn(player, enemy)
        
        if player.get_stat('health') <= 0:
            defeat(player)
            break
    
    # Восстановление после боя
    if player.get_stat('health') > 0:
        print("\nResting after battle...")
        player.heal(player.get_stat('max_health') // 10)  # Восстанавливаем 10% HP
        player.restore_mana(player.get_stat('max_mana') // 5)  # Восстанавливаем 20% MP
        time.sleep(2)

def player_turn(player, enemy):
    """Ход игрока"""
    action_taken = False
    
    while not action_taken:
        show_combat_screen(player, enemy)
        
        try:
            choice = input("Choose action (1-4): ")
            
            if choice == "1":
                # Обычная атака
                damage = calculate_player_damage(player)
                enemy.take_damage(damage)
                print_colored(f"\n{player.name} attacks {enemy.name} for {damage} damage!", "GREEN")
                action_taken = True
                
            elif choice == "2":
                # Использовать навык
                skill = choose_skill(player)
                if skill:
                    if player.can_use_skill(skill):
                        result = player.use_skill(skill, enemy)
                        if result:
                            print_colored(f"\n{player.name} uses {skill.name} for {result['damage']} damage!", "BLUE")
                        else:
                            print_colored(f"\nSkill failed!", "RED")
                        action_taken = True
                    else:
                        print_colored(f"\nNot enough mana! Need {skill.mana_cost} MP.", "RED")
                        time.sleep(2)
                else:
                    print("No skill selected!")
                    time.sleep(1)
                    
            elif choice == "3":
                # Использовать предмет
                print("\nItem usage not implemented yet!")
                time.sleep(1)
                # Можно добавить использование зелий
                
            elif choice == "4":
                # Попытка убежать
                if attempt_flee():
                    print_colored(f"\n{player.name} successfully fled from battle!", "YELLOW")
                    enemy.alive = False  # Завершаем бой
                    return
                else:
                    print_colored(f"\nFailed to flee!", "RED")
                    action_taken = True  # Пропускаем ход при неудачной попытке побега
                    
            else:
                print("Invalid choice!")
                time.sleep(1)
                
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)
    
    time.sleep(1)

def enemy_turn(player, enemy):
    """Ход врага"""
    if enemy.alive:
        damage = enemy.attack(player)
        if damage > 0:
            print_colored(f"\n{enemy.name} attacks {player.name} for {damage} damage!", "RED")
        time.sleep(1)

def combat_turn(player, enemy):
    """Один ход в бою (альтернативная упрощенная версия)"""
    # Эта функция может использоваться для простых пошаговых боев
    damage = calculate_player_damage(player)
    enemy.take_damage(damage)
    print(f"{player.name} attacks for {damage} damage!")
    
    if enemy.alive:
        damage = enemy.attack(player)
        if damage > 0:
            print(f"{enemy.name} attacks back for {damage} damage!")
    
    return enemy.alive

def calculate_player_damage(player):
    """Рассчитать урон от обычной атаки игрока"""
    base_damage = player.get_stat('strength') // 2
    weapon_bonus = 0
    
    if player.equipment['weapon']:
        # Можно добавить логику урона от оружия
        weapon_bonus = player.equipment['weapon'].stat_bonuses.get('strength', 0)
    
    total_damage = base_damage + weapon_bonus + random.randint(1, 5)
    return max(1, total_damage)

def choose_skill(player):
    """Выбрать навык для использования"""
    if not player.skills:
        return None
    
    print("\nAvailable skills:")
    for i, skill in enumerate(player.skills, 1):
        print(f"{i}. {skill.name} ({skill.mana_cost} MP)")
    
    try:
        choice = int(input("Select skill (0 to cancel): "))
        if choice == 0:
            return None
        elif 1 <= choice <= len(player.skills):
            return player.skills[choice - 1]
        else:
            print("Invalid skill number!")
            return None
    except ValueError:
        print("Please enter a number!")
        return None

def attempt_flee():
    """Попытка убежать из боя"""
    return random.random() < 0.5  # 50% шанс успеха

def victory(player, enemy):
    """Победа в бою"""
    exp_gain = enemy.experience
    gold_gain = enemy.gold
    
    player.add_experience(exp_gain)
    # Здесь можно добавить получение золота в инвентарь
    
    print_colored(f"\n╔══════════════════════════════════════╗", "GREEN")
    print_colored(f"║          VICTORY!                    ║", "GREEN")
    print_colored(f"║                                      ║", "GREEN")
    print_colored(f"║  You defeated {enemy.name:^20}  ║", "GREEN")
    print_colored(f"║                                      ║", "GREEN")
    print_colored(f"║  Experience gained: {exp_gain:<6}       ║", "GREEN")
    print_colored(f"║  Gold gained: {gold_gain:<6}             ║", "GREEN")
    print_colored(f"║                                      ║", "GREEN")
    print_colored(f"╚══════════════════════════════════════╝", "GREEN")
    
    # Шанс на дроп предмета
    if random.random() < 0.3:  # 30% шанс
        from entities.items import Item
        loot_items = [
            Item("Health Potion", "potion", {"heal": 50}, 20, "Restores 50 HP"),
            Item("Mana Potion", "potion", {"mana": 30}, 25, "Restores 30 MP"),
            Item("Leather Gloves", "armor", {"agility": 1}, 15, "Simple leather gloves")
        ]
        loot = random.choice(loot_items)
        player.add_to_inventory(loot)
        print_colored(f"\nFound: {loot.name}!", "YELLOW")
    
    # Автосохранение после победы
    try:
        from game_logic.save_system import save_system
        success, message = save_system.save_game(player, "autosave")
        if success:
            print_colored("\nGame autosaved!", "CYAN")
    except Exception as e:
        print(f"Autosave failed: {e}")
    
    time.sleep(3)

def defeat(player):
    """Поражение в бою"""
    print_colored(f"\n╔══════════════════════════════════════╗", "RED")
    print_colored(f"║           DEFEAT!                    ║", "RED")
    print_colored(f"║                                      ║", "RED")
    print_colored(f"║   {player.name:^30}   ║", "RED")
    print_colored(f"║        has been defeated!            ║", "RED")
    print_colored(f"║                                      ║", "RED")
    print_colored(f"║  You lose some gold and experience   ║", "RED")
    print_colored(f"║                                      ║", "RED")
    print_colored(f"╚══════════════════════════════════════╝", "RED")
    
    # Штрафы за смерть
    player.experience = max(0, player.experience - 50)
    player.current_attributes['health'] = player.current_attributes['max_health'] // 2
    player.current_attributes['mana'] = player.current_attributes['max_mana'] // 2
    
    # Автосохранение после смерти
    try:
        from game_logic.save_system import save_system
        success, message = save_system.save_game(player, "death_save")
        if success:
            print_colored("\nGame saved before respawn!", "CYAN")
    except Exception as e:
        print(f"Autosave failed: {e}")
    
    time.sleep(3)