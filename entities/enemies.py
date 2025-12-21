"""
Классы врагов и монстров
"""

class Enemy:
    def __init__(self, name, level, health, damage, experience, gold):
        self.name = name
        self.level = level
        self.max_health = health
        self.health = health
        self.damage = damage
        self.experience = experience
        self.gold = gold
        self.alive = True
    
    def take_damage(self, damage):
        """Получить урон"""
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            return True  # Враг умер
        return False
    
    def attack(self, target):
        """Атаковать цель"""
        if self.alive and hasattr(target, 'take_damage'):
            target.take_damage(self.damage)
            return self.damage
        return 0
    
    def get_status(self):
        """Получить статус врага"""
        return {
            'name': self.name,
            'level': self.level,
            'health': f"{self.health}/{self.max_health}",
            'damage': self.damage,
            'experience': self.experience,
            'gold': self.gold,
            'alive': self.alive
        }
    
    def __str__(self):
        return f"{self.name} (Lvl {self.level})"


class Goblin(Enemy):
    def __init__(self, level=1):
        health = 30 + (level * 10)
        damage = 5 + (level * 2)
        experience = 20 + (level * 5)
        gold = 5 + level
        super().__init__("Goblin", level, health, damage, experience, gold)


class Orc(Enemy):
    def __init__(self, level=3):
        health = 50 + (level * 15)
        damage = 8 + (level * 3)
        experience = 40 + (level * 8)
        gold = 10 + (level * 2)
        super().__init__("Orc Warrior", level, health, damage, experience, gold)
        self.special_attack_cooldown = 0
    
    def attack(self, target):
        """Орк имеет шанс на специальную атаку"""
        import random
        damage = self.damage
        
        if self.special_attack_cooldown <= 0 and random.random() < 0.2:
            damage = int(damage * 1.5)
            self.special_attack_cooldown = 3
            print(f"{self.name} uses Brutal Strike!")
        
        if self.special_attack_cooldown > 0:
            self.special_attack_cooldown -= 1
        
        if hasattr(target, 'take_damage'):
            target.take_damage(damage)
        return damage


class Dragon(Enemy):
    def __init__(self, level=10):
        health = 200 + (level * 30)
        damage = 15 + (level * 5)
        experience = 200 + (level * 20)
        gold = 100 + (level * 10)
        super().__init__("Ancient Dragon", level, health, damage, experience, gold)
        self.breath_cooldown = 0
    
    def attack(self, target):
        """Дракон может использовать огненное дыхание"""
        import random
        damage = self.damage
        
        if self.breath_cooldown <= 0 and random.random() < 0.3:
            damage = int(damage * 2)
            self.breath_cooldown = 5
            print(f"{self.name} uses Fire Breath!")
        
        if self.breath_cooldown > 0:
            self.breath_cooldown -= 1
        
        if hasattr(target, 'take_damage'):
            target.take_damage(damage)
        return damage