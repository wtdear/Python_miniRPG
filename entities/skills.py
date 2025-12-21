"""
Классы навыков и умений
"""

class Skill:
    def __init__(self, name, mana_cost, base_damage, stat_multiplier, skill_type="active", description=""):
        self.name = name
        self.mana_cost = mana_cost
        self.base_damage = base_damage
        self.stat_multiplier = stat_multiplier  # Например, {'strength': 1.5}
        self.skill_type = skill_type  # active, passive, buff, etc.
        self.description = description
        self.level = 1
        self.max_level = 5
    
    def upgrade(self):
        """Улучшить навык"""
        if self.level < self.max_level:
            self.level += 1
            self.base_damage = int(self.base_damage * 1.3)
            self.mana_cost = int(self.mana_cost * 1.1)
            return True
        return False
    
    def calculate_damage(self, caster):
        """Рассчитать урон навыка"""
        damage = self.base_damage * self.level
        
        # Добавляем множители от характеристик
        for stat, multiplier in self.stat_multiplier.items():
            stat_value = caster.get_stat(stat)
            damage += stat_value * multiplier
        
        return int(damage)
    
    def use(self, caster, target=None):
        """Использовать навык"""
        damage = self.calculate_damage(caster)
        
        if target and hasattr(target, 'take_damage'):
            target.take_damage(damage)
        
        return {
            'skill': self.name,
            'damage': damage,
            'mana_cost': self.mana_cost,
            'critical': False  # Можно добавить систему критов
        }
    
    def get_info(self):
        """Получить информацию о навыке"""
        return {
            'name': self.name,
            'level': self.level,
            'mana_cost': self.mana_cost,
            'damage': self.base_damage,
            'type': self.skill_type,
            'description': self.description
        }
    
    def __str__(self):
        return f"{self.name} (Lvl {self.level}) - {self.mana_cost} MP"