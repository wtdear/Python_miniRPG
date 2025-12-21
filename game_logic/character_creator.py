"""
Создание персонажей и начальная настройка
"""
from entities.character import Character
from entities.skills import Skill
from entities.items import Item
from config import CLASS_CONFIG, SKILL_CONFIG, STARTING_EQUIPMENT

def create_character_class(class_name, name):
    """Фабрика для создания персонажей разных классов"""
    if class_name not in CLASS_CONFIG:
        raise ValueError(f"Класс {class_name} не существует")
    
    # Создаем базового персонажа
    char = Character(name)
    char.class_name = class_name
    
    # Получаем конфигурацию класса
    class_config = CLASS_CONFIG[class_name]
    
    # Устанавливаем базовые атрибуты
    char.base_attributes['health'] = 100 + class_config.get('health_bonus', 0)
    char.base_attributes['max_health'] = 100 + class_config.get('health_bonus', 0)
    char.base_attributes['mana'] = 50 + class_config.get('mana_bonus', 0)
    char.base_attributes['max_mana'] = 50 + class_config.get('mana_bonus', 0)
    char.base_attributes['strength'] = class_config.get('strength', 10)
    char.base_attributes['agility'] = class_config.get('agility', 10)
    char.base_attributes['intelligence'] = class_config.get('intelligence', 10)
    
    # Обновляем текущие атрибуты
    char.current_attributes = char.base_attributes.copy()
    
    # Добавляем навыки
    skill_configs = SKILL_CONFIG.get(class_name, [])
    for skill_config in skill_configs:
        skill = Skill(
            name=skill_config['name'],
            mana_cost=skill_config['mana_cost'],
            base_damage=skill_config['base_damage'],
            stat_multiplier=skill_config['stat_multiplier'],
            description=skill_config['description']
        )
        char.skills.append(skill)
    
    # Даем стартовое снаряжение
    give_starting_equipment(char, class_name)
    
    return char

def give_starting_equipment(character, class_name):
    """Выдать стартовое снаряжение"""
    equipment_configs = STARTING_EQUIPMENT.get(class_name, [])
    
    for equip_config in equipment_configs:
        item = Item(
            name=equip_config['name'],
            item_type=equip_config['item_type'],
            stat_bonuses=equip_config.get('stat_bonuses', {}),
            value=equip_config.get('value', 0)
        )
        character.add_to_inventory(item)
        
        # Автоматически экипируем оружие и броню
        if item.item_type == 'weapon':
            character.equip_item(item, 'weapon')
            item.equipped = True
        elif item.item_type == 'armor':
            character.equip_item(item, 'armor')
            item.equipped = True
    
    # Также даем несколько зелий
    from entities.items import Potion
    health_potion = Potion("Health Potion", "heal", 50, 20, "Restores 50 HP")
    mana_potion = Potion("Mana Potion", "mana", 30, 25, "Restores 30 MP")
    
    character.add_to_inventory(health_potion)
    character.add_to_inventory(mana_potion)