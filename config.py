"""
Конфигурационные настройки игры
"""

# Настройки игры
GAME_NAME = "RPG WORLD"
VERSION = "1.0.0"
AUTHOR = "RPG Game Studio"

# Настройки отображения
SCREEN_WIDTH = 80
FRAME_SYMBOL = "═"
CORNER_SYMBOL = "╔╗╚╝"

# Настройки персонажа
STARTING_LEVEL = 1
BASE_HEALTH = 100
BASE_MANA = 50
BASE_EXP_TO_LEVEL = 100
EXP_MULTIPLIER = 1.5
ATTRIBUTE_POINTS_PER_LEVEL = 3
SKILL_POINTS_PER_LEVEL = 1

# Настройки классов
CLASS_CONFIG = {
    'warrior': {
        'display_name': '⚔️ WARRIOR',
        'health_bonus': 20,
        'mana_bonus': -20,
        'strength': 15,
        'agility': 8,
        'intelligence': 5,
        'description': 'High HP and Strength'
    },
    'mage': {
        'display_name': '🔮 MAGE',
        'health_bonus': -30,
        'mana_bonus': 50,
        'strength': 5,
        'agility': 7,
        'intelligence': 18,
        'description': 'High Mana and Intelligence'
    },
    'archer': {
        'display_name': '🏹 ARCHER',
        'health_bonus': -15,
        'mana_bonus': 0,
        'strength': 8,
        'agility': 16,
        'intelligence': 6,
        'description': 'High Agility and Precision'
    }
}

# Настройки навыков
SKILL_CONFIG = {
    'warrior': [
        {
            'name': 'Power Attack',
            'mana_cost': 10,
            'base_damage': 15,
            'stat_multiplier': {'strength': 1.2},
            'description': 'A powerful strike with your weapon'
        },
        {
            'name': 'Shield Bash',
            'mana_cost': 15,
            'base_damage': 10,
            'stat_multiplier': {'strength': 0.8},
            'description': 'Bash enemy with your shield'
        },
        {
            'name': 'Battle Cry',
            'mana_cost': 20,
            'base_damage': 0,
            'stat_multiplier': {'strength': 0.5},
            'description': 'Boost your strength temporarily'
        }
    ],
    'mage': [
        {
            'name': 'Fireball',
            'mana_cost': 25,
            'base_damage': 20,
            'stat_multiplier': {'intelligence': 1.5},
            'description': 'Launch a fiery projectile'
        },
        {
            'name': 'Ice Shard',
            'mana_cost': 15,
            'base_damage': 15,
            'stat_multiplier': {'intelligence': 1.2},
            'description': 'Sharp ice projectile'
        },
        {
            'name': 'Mana Shield',
            'mana_cost': 30,
            'base_damage': 0,
            'stat_multiplier': {'intelligence': 2.0},
            'description': 'Create a protective mana barrier'
        }
    ],
    'archer': [
        {
            'name': 'Precise Shot',
            'mana_cost': 12,
            'base_damage': 12,
            'stat_multiplier': {'agility': 1.3},
            'description': 'Aimed shot with increased accuracy'
        },
        {
            'name': 'Multi Arrow',
            'mana_cost': 30,
            'base_damage': 8,
            'stat_multiplier': {'agility': 1.0},
            'description': 'Shoot multiple arrows at once'
        },
        {
            'name': 'Evasion',
            'mana_cost': 0,
            'base_damage': 0,
            'stat_multiplier': {'agility': 0.5},
            'description': 'Passive: Increased dodge chance'
        }
    ]
}

# Настройки стартового снаряжения
STARTING_EQUIPMENT = {
    'warrior': [
        {
            'name': 'Iron Sword',
            'item_type': 'weapon',
            'stat_bonuses': {'strength': 3},
            'value': 50
        },
        {
            'name': 'Leather Armor',
            'item_type': 'armor',
            'stat_bonuses': {'max_health': 20},
            'value': 30
        }
    ],
    'mage': [
        {
            'name': 'Wooden Staff',
            'item_type': 'weapon',
            'stat_bonuses': {'intelligence': 3},
            'value': 50
        },
        {
            'name': 'Robe',
            'item_type': 'armor',
            'stat_bonuses': {'max_mana': 20},
            'value': 30
        }
    ],
    'archer': [
        {
            'name': 'Short Bow',
            'item_type': 'weapon',
            'stat_bonuses': {'agility': 3},
            'value': 50
        },
        {
            'name': 'Leather Vest',
            'item_type': 'armor',
            'stat_bonuses': {'agility': 2},
            'value': 30
        }
    ]
}

# Цвета для консоли (если поддерживается)
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'END': '\033[0m'
}