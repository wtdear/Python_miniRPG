"""
Класс персонажа игрока
"""

class Character:
    def __init__(self, name):
        self.name = name
        self.class_name = None
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100
        self.attribute_points = 0
        self.skill_points = 0
        
        # Базовые атрибуты
        self.base_attributes = {
            'health': 100,
            'max_health': 100,
            'mana': 50,
            'max_mana': 50,
            'strength': 10,
            'agility': 10,
            'intelligence': 10
        }
        
        # Текущие значения (могут меняться в бою)
        self.current_attributes = self.base_attributes.copy()
        
        self.skills = []
        self.inventory = []
        self.equipment = {
            'weapon': None,
            'armor': None,
            'helmet': None,
            'gloves': None,
            'boots': None,
            'accessory': None
        }
    
    def add_experience(self, amount):
        """Добавить опыт персонажу"""
        self.experience += amount
        while self.experience >= self.experience_to_next_level:
            self.level_up()
    
    def level_up(self):
        """Повышение уровня персонажа"""
        self.experience -= self.experience_to_next_level
        self.level += 1
        self.experience_to_next_level = int(self.experience_to_next_level * 1.5)
        self.attribute_points += 3
        self.skill_points += 1
        
        # Автоматическое увеличение характеристик при повышении уровня
        self.base_attributes['max_health'] += 10
        self.base_attributes['max_mana'] += 5
        self.base_attributes['health'] = self.base_attributes['max_health']
        self.base_attributes['mana'] = self.base_attributes['max_mana']
        
        print(f"{self.name} достиг {self.level} уровня!")
    
    def add_attribute_point(self, attribute):
        """Добавить очко характеристики"""
        if self.attribute_points > 0 and attribute in self.base_attributes:
            self.base_attributes[attribute] += 1
            self.attribute_points -= 1
            
            # Обновляем производные характеристики
            if attribute == 'strength':
                self.base_attributes['max_health'] += 5
            elif attribute == 'intelligence':
                self.base_attributes['max_mana'] += 5
            
            self.recalculate_stats()
    
    def recalculate_stats(self):
        """Пересчитать все характеристики с учетом снаряжения"""
        # Копируем базовые характеристики
        self.current_attributes = self.base_attributes.copy()
        
        # Добавляем бонусы от снаряжения
        for slot, item in self.equipment.items():
            if item and hasattr(item, 'stat_bonuses'):
                for stat, bonus in item.stat_bonuses.items():
                    if stat in self.current_attributes:
                        self.current_attributes[stat] += bonus
        
        # Гарантируем, что текущие HP/MP не превышают максимум
        self.current_attributes['health'] = min(
            self.current_attributes['health'], 
            self.current_attributes['max_health']
        )
        self.current_attributes['mana'] = min(
            self.current_attributes['mana'], 
            self.current_attributes['max_mana']
        )
    
    def get_stat(self, stat_name):
        """Получить текущее значение характеристики"""
        return self.current_attributes.get(stat_name, 0)
    
    def take_damage(self, damage):
        """Получить урон"""
        self.current_attributes['health'] -= damage
        if self.current_attributes['health'] <= 0:
            self.current_attributes['health'] = 0
            return True  # Персонаж умер
        return False
    
    def heal(self, amount):
        """Восстановить здоровье"""
        self.current_attributes['health'] = min(
            self.current_attributes['health'] + amount,
            self.current_attributes['max_health']
        )
    
    def restore_mana(self, amount):
        """Восстановить ману"""
        self.current_attributes['mana'] = min(
            self.current_attributes['mana'] + amount,
            self.current_attributes['max_mana']
        )
    
    def equip_item(self, item, slot):
        """Экипировать предмет"""
        if slot in self.equipment:
            # Снимаем текущий предмет, если он есть
            if self.equipment[slot]:
                self.unequip_item(slot)
            
            self.equipment[slot] = item
            self.recalculate_stats()
            return True
        return False
    
    def unequip_item(self, slot):
        """Снять предмет"""
        if slot in self.equipment and self.equipment[slot]:
            item = self.equipment[slot]
            self.equipment[slot] = None
            self.recalculate_stats()
            return item
        return None
    
    def add_to_inventory(self, item):
        """Добавить предмет в инвентарь"""
        self.inventory.append(item)
    
    def remove_from_inventory(self, item):
        """Удалить предмет из инвентаря"""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def get_skill(self, skill_name):
        """Найти навык по имени"""
        for skill in self.skills:
            if skill.name == skill_name:
                return skill
        return None
    
    def can_use_skill(self, skill):
        """Проверить, может ли персонаж использовать навык"""
        return (self.current_attributes['mana'] >= skill.mana_cost and 
                skill in self.skills)
    
    def use_skill(self, skill, target=None):
        """Использовать навык"""
        if not self.can_use_skill(skill):
            return None
        
        # Тратим ману
        self.current_attributes['mana'] -= skill.mana_cost
        
        # Используем навык
        return skill.use(self, target)
    
    def get_status(self):
        """Получить статус персонажа"""
        return {
            'name': self.name,
            'class': self.class_name,
            'level': self.level,
            'exp': f"{self.experience}/{self.experience_to_next_level}",
            'health': f"{self.current_attributes['health']}/{self.current_attributes['max_health']}",
            'mana': f"{self.current_attributes['mana']}/{self.current_attributes['max_mana']}",
            'stats': {
                'strength': self.current_attributes['strength'],
                'agility': self.current_attributes['agility'],
                'intelligence': self.current_attributes['intelligence']
            },
            'attribute_points': self.attribute_points,
            'skill_points': self.skill_points
        }
    
    def __str__(self):
        return f"{self.name} - Level {self.level} {self.class_name}"