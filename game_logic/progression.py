"""
Система прогрессии и уровней
"""

def calculate_exp_reward(enemy_level, player_level):
    """Рассчитать награду за опыт"""
    base_exp = 20
    level_diff = enemy_level - player_level
    
    if level_diff > 0:
        bonus = level_diff * 5
    else:
        bonus = 0
    
    return base_exp + bonus

def check_level_up(character):
    """Проверить повышение уровня"""
    while character.experience >= character.experience_to_next_level:
        character.level_up()