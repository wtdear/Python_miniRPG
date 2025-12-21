"""
Пакет сущностей игры
"""
from .character import Character
from .skills import Skill
from .items import Item
from .enemies import Enemy, Goblin, Orc, Dragon

__all__ = ['Character', 'Skill', 'Item', 'Enemy', 'Goblin', 'Orc', 'Dragon']