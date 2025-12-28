"""
Утилиты для работы с файлами
"""
import os
import shutil

def backup_file(filepath):
    """Создать резервную копию файла"""
    if os.path.exists(filepath):
        backup_path = filepath + ".bak"
        shutil.copy2(filepath, backup_path)
        return True
    return False

def get_file_size_mb(filepath):
    """Получить размер файла в МБ"""
    if os.path.exists(filepath):
        return os.path.getsize(filepath) / (1024 * 1024)
    return 0

def safe_write(filepath, content):
    """Безопасная запись в файл с созданием резервной копии"""
    try:
        # Создаем резервную копию если файл существует
        if os.path.exists(filepath):
            backup_file(filepath)
        
        # Записываем во временный файл
        temp_path = filepath + ".tmp"
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Перемещаем временный файл на место основного
        shutil.move(temp_path, filepath)
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False