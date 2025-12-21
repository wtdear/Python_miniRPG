"""
Классы предметов и снаряжения
"""

class Item:
    def __init__(self, name, item_type, stat_bonuses=None, value=0, description=""):
        self.name = name
        self.item_type = item_type  # weapon, armor, potion, etc.
        self.stat_bonuses = stat_bonuses or {}
        self.value = value
        self.description = description
        self.equipped = False
    
    def get_info(self):
        """Получить информацию о предмете"""
        info = {
            'name': self.name,
            'type': self.item_type,
            'value': self.value,
            'description': self.description
        }
        
        if self.stat_bonuses:
            info['bonuses'] = self.stat_bonuses
        
        return info
    
    def __str__(self):
        bonuses = ""
        if self.stat_bonuses:
            bonuses = " [" + ", ".join(f"{k}+{v}" for k, v in self.stat_bonuses.items()) + "]"
        return f"{self.name} ({self.item_type}){bonuses}"


class Weapon(Item):
    def __init__(self, name, damage, stat_bonuses=None, value=0, description="", weapon_type="sword"):
        super().__init__(name, 'weapon', stat_bonuses, value, description)
        self.damage = damage
        self.weapon_type = weapon_type  # sword, bow, staff, etc.


class Armor(Item):
    def __init__(self, name, defense, slot, stat_bonuses=None, value=0, description=""):
        super().__init__(name, 'armor', stat_bonuses, value, description)
        self.defense = defense
        self.slot = slot  # head, chest, legs, etc.


class Potion(Item):
    def __init__(self, name, effect_type, effect_amount, value=0, description=""):
        super().__init__(name, 'potion', None, value, description)
        self.effect_type = effect_type  # heal, mana, buff
        self.effect_amount = effect_amount
    
    def use(self, character):
        """Использовать зелье"""
        if self.effect_type == 'heal':
            character.heal(self.effect_amount)
            return f"Restored {self.effect_amount} HP"
        elif self.effect_type == 'mana':
            character.restore_mana(self.effect_amount)
            return f"Restored {self.effect_amount} MP"
        return "No effect"