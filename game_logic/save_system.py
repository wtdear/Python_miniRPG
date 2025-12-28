"""
Система сохранения и загрузки игры
"""
import os
import json
import pickle
import zlib
import base64
from datetime import datetime

SAVE_DIR = "saves"
SAVE_EXTENSION = ".rpg_save"

class SaveSystem:
    def __init__(self):
        """Инициализация системы сохранения"""
        self.ensure_save_dir()
    
    def ensure_save_dir(self):
        """Создать директорию для сохранений, если её нет"""
        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
    
    def get_save_files(self):
        """Получить список файлов сохранений"""
        saves = []
        if os.path.exists(SAVE_DIR):
            for file in os.listdir(SAVE_DIR):
                if file.endswith(SAVE_EXTENSION):
                    filepath = os.path.join(SAVE_DIR, file)
                    stats = os.stat(filepath)
                    saves.append({
                        'filename': file,
                        'filepath': filepath,
                        'created': datetime.fromtimestamp(stats.st_ctime),
                        'modified': datetime.fromtimestamp(stats.st_mtime),
                        'size': stats.st_size
                    })
        return sorted(saves, key=lambda x: x['modified'], reverse=True)
    
    def save_game(self, character, slot_name="auto"):
        """Сохранить игру"""
        try:
            # Создаем данные для сохранения
            save_data = self.prepare_save_data(character)
            
            # Генерируем имя файла
            if slot_name == "auto":
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"save_{timestamp}{SAVE_EXTENSION}"
            else:
                filename = f"{slot_name}{SAVE_EXTENSION}"
            
            filepath = os.path.join(SAVE_DIR, filename)
            
            # Сохраняем в JSON (более читаемый формат)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, indent=2, ensure_ascii=False, default=str)
            
            # Также сохраняем бинарную версию для надежности
            binary_filepath = filepath.replace(SAVE_EXTENSION, ".bin")
            compressed_data = zlib.compress(pickle.dumps(save_data))
            with open(binary_filepath, 'wb') as f:
                f.write(compressed_data)
            
            return True, f"Game saved as {filename}"
            
        except Exception as e:
            return False, f"Save failed: {str(e)}"
    
    def prepare_save_data(self, character):
        """Подготовить данные персонажа для сохранения"""
        # Собираем все данные персонажа
        save_data = {
            'metadata': {
                'version': '1.0',
                'save_date': datetime.now().isoformat(),
                'game_name': 'RPG Game'
            },
            'character': {
                'name': character.name,
                'class_name': character.class_name,
                'level': character.level,
                'experience': character.experience,
                'experience_to_next_level': character.experience_to_next_level,
                'attribute_points': character.attribute_points,
                'skill_points': character.skill_points,
                'base_attributes': character.base_attributes,
                'current_attributes': character.current_attributes,
            },
            'skills': [],
            'inventory': [],
            'equipment': {}
        }
        
        # Сохраняем навыки
        for skill in character.skills:
            skill_data = {
                'name': skill.name,
                'mana_cost': skill.mana_cost,
                'base_damage': skill.base_damage,
                'stat_multiplier': skill.stat_multiplier,
                'skill_type': skill.skill_type,
                'level': skill.level,
                'description': getattr(skill, 'description', '')
            }
            save_data['skills'].append(skill_data)
        
        # Сохраняем инвентарь
        for item in character.inventory:
            item_data = {
                'name': item.name,
                'item_type': item.item_type,
                'stat_bonuses': item.stat_bonuses,
                'value': item.value,
                'description': getattr(item, 'description', ''),
                'equipped': getattr(item, 'equipped', False)
            }
            save_data['inventory'].append(item_data)
        
        # Сохраняем экипировку
        for slot, item in character.equipment.items():
            if item:
                item_data = {
                    'name': item.name,
                    'item_type': item.item_type,
                    'stat_bonuses': item.stat_bonuses,
                    'value': item.value,
                    'description': getattr(item, 'description', '')
                }
                save_data['equipment'][slot] = item_data
        
        return save_data
    
    def load_game(self, filename):
        """Загрузить игру из файла"""
        try:
            filepath = os.path.join(SAVE_DIR, filename)
            
            # Пробуем загрузить из JSON
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    save_data = json.load(f)
            else:
                # Пробуем загрузить из бинарного файла
                binary_filepath = filepath.replace(SAVE_EXTENSION, ".bin")
                if os.path.exists(binary_filepath):
                    with open(binary_filepath, 'rb') as f:
                        compressed_data = f.read()
                    save_data = pickle.loads(zlib.decompress(compressed_data))
                else:
                    return None, "Save file not found"
            
            # Восстанавливаем персонажа
            character = self.restore_character(save_data)
            return character, "Game loaded successfully"
            
        except Exception as e:
            return None, f"Load failed: {str(e)}"
    
    def restore_character(self, save_data):
        """Восстановить персонажа из данных сохранения"""
        from entities.character import Character
        from entities.skills import Skill
        from entities.items import Item
        
        char_data = save_data['character']
        
        # Создаем базового персонажа
        character = Character(char_data['name'])
        character.class_name = char_data['class_name']
        character.level = char_data['level']
        character.experience = char_data['experience']
        character.experience_to_next_level = char_data['experience_to_next_level']
        character.attribute_points = char_data['attribute_points']
        character.skill_points = char_data['skill_points']
        character.base_attributes = char_data['base_attributes']
        character.current_attributes = char_data['current_attributes']
        
        # Восстанавливаем навыки
        character.skills = []
        for skill_data in save_data['skills']:
            skill = Skill(
                name=skill_data['name'],
                mana_cost=skill_data['mana_cost'],
                base_damage=skill_data['base_damage'],
                stat_multiplier=skill_data['stat_multiplier'],
                skill_type=skill_data['skill_type'],
                description=skill_data.get('description', '')
            )
            skill.level = skill_data['level']
            character.skills.append(skill)
        
        # Восстанавливаем инвентарь
        character.inventory = []
        for item_data in save_data['inventory']:
            item = Item(
                name=item_data['name'],
                item_type=item_data['item_type'],
                stat_bonuses=item_data['stat_bonuses'],
                value=item_data['value'],
                description=item_data.get('description', '')
            )
            item.equipped = item_data.get('equipped', False)
            character.inventory.append(item)
        
        # Восстанавливаем экипировку
        for slot, item_data in save_data['equipment'].items():
            if item_data:
                item = Item(
                    name=item_data['name'],
                    item_type=item_data['item_type'],
                    stat_bonuses=item_data['stat_bonuses'],
                    value=item_data['value'],
                    description=item_data.get('description', '')
                )
                character.equip_item(item, slot)
                item.equipped = True
        
        return character
    
    def delete_save(self, filename):
        """Удалить сохранение"""
        try:
            filepath = os.path.join(SAVE_DIR, filename)
            
            # Удаляем оба файла (JSON и бинарный)
            if os.path.exists(filepath):
                os.remove(filepath)
            
            binary_filepath = filepath.replace(SAVE_EXTENSION, ".bin")
            if os.path.exists(binary_filepath):
                os.remove(binary_filepath)
            
            return True, "Save deleted successfully"
            
        except Exception as e:
            return False, f"Delete failed: {str(e)}"

# Глобальный экземпляр системы сохранения
save_system = SaveSystem()