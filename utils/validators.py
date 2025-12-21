"""
Валидаторы данных
"""

def validate_name(name):
    """Проверка имени персонажа"""
    if not name or len(name.strip()) == 0:
        return False, "Name cannot be empty"
    
    if len(name) > 20:
        return False, "Name too long (max 20 characters)"
    
    if not all(c.isalnum() or c.isspace() for c in name):
        return False, "Name can only contain letters, numbers and spaces"
    
    return True, ""

def validate_choice(choice, min_val, max_val):
    """Проверка выбора из меню"""
    try:
        value = int(choice)
        if min_val <= value <= max_val:
            return True, value
        else:
            return False, f"Please enter a number between {min_val} and {max_val}"
    except ValueError:
        return False, "Please enter a valid number"