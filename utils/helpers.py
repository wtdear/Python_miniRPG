"""
Вспомогательные функции
"""
import random
import string

def validate_input(prompt, input_type=str, min_value=None, max_value=None):
    """Валидация ввода пользователя"""
    while True:
        try:
            user_input = input(prompt)
            
            if input_type == int:
                value = int(user_input)
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Value must be at most {max_value}")
                    continue
                return value
            elif input_type == float:
                value = float(user_input)
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Value must be at most {max_value}")
                    continue
                return value
            else:
                return user_input.strip()
                
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}")

def format_number(number):
    """Форматирование чисел"""
    if number >= 1000000:
        return f"{number/1000000:.1f}M"
    elif number >= 1000:
        return f"{number/1000:.1f}K"
    else:
        return str(number)

def get_random_name():
    """Генерация случайного имени"""
    syllables = ['ar', 'el', 'ion', 'dor', 'an', 'is', 'thor', 'val', 'mir', 'lin']
    name = ''.join(random.choices(syllables, k=random.randint(2, 3))).capitalize()
    return name

def roll_dice(sides=20, count=1):
    """Бросок костей"""
    total = 0
    for _ in range(count):
        total += random.randint(1, sides)
    return total

def chance(percentage):
    """Проверка шанса в процентах"""
    return random.random() < (percentage / 100)