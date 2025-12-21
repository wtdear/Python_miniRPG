"""
Управление инвентарем
"""

def equip_item(character, item):
    """Экипировать предмет"""
    # Логика экипировки уже в классе Character
    pass

def unequip_item(character, slot):
    """Снять предмет"""
    # Логика снятия уже в классе Character
    pass

def use_item(character, item):
    """Использовать предмет"""
    if hasattr(item, 'use'):
        return item.use(character)
    return "Cannot use this item"