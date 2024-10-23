class MySuperClass:
    def __init__(self, surname, name, mark):
        # в середині конструктора створюються атрибути
        self.surname = surname
        self.name = name
        self.mark = mark

def function_in_module():
    pass


# my_class.py

class MySuperClass:
    """Тестовий клас, зараз реалізуємо опис студента.
    
    ---
    
    surname : str
        Прізвище студента.
    """
    
    def __init__(self, surname, name, mark):
        """
        Ініціалізуємо об'єкт.
        - в середині конструктора створюються атрибути.
        """
        print("Викликаємо __init__")
        self.surname = surname
        self.name = name
        self.mark = mark
    
    def __repr__(self):
        return f"Представлення об'єкту: MySuperClass(surname={self.surname}, name={self.name}, mark={self.mark})"
    
    def __len__(self):
        return len(self.surname)

# Головний файл
from my_class import MySuperClass

obj = MySuperClass("Петренко", "Іван", 85)

print(obj)
help(obj)

print(MySuperClass.__doc__)

# Використовуємо __len__ для об'єкта
print("Довжина прізвища: ", len(obj))  # Це викликає __len__() в класі

print("Беремо атрибут імені:", obj.name)
