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
    """Тестовий клас, зараз реалізуємо опис студента
    
    ---

    surname : str
        Прізвище студента
    
    """
    def __init__(self, surname:str, name, mark:int, group=None):
        """
        Ініціалізуємо обєкт
        - в середині конструктора створюються атрибути
        """
        print("Викликаємо __init__")
        self.__surname = surname #  private Це приватні атрибути, вони не висвічуються назовні
        self.__name = name
        self.mark = mark # public публічний атрибук
        self.group = group
        self._age = None # (protected) захищений атрибут
        self._scholarship = 0
    
    @property
    def name(self):
        """Ця властивість є закритою, її можна читати але не можна змінювати
        """
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def say_hello(self):
        a = 1 + 2
        return f"Привіт {a}"
    
    def __repr__(self):
        return "Представлення обєкту Студент, його задають: MySuperClass(surname, name, mark)"
    
    def __len__(self):
        return len(self.surname)
    
    def fucntion_in_class(self):
        """Це вже метод згідно термінології, і він публічний
        """
        return "Ми викликали публічний метод"

    def _protected_method_in_class(self):
        """Це захищений метод
        """
        self.__this_is_private()
        return "Ми доступаємось до захищеного методу"
    
    def __this_is_private(self):
        print("Це приватний метод!")

    def calculate_scholarship_after_session(self, raiting: int):
        if raiting == 5:
            self._scholarship = "2200 грн"
            return "Присвоєно підвищену стипундію"
        if raiting == 4:
            self._scholarship = "1510 грн"
            return "Присвоєно звичайну стипундію"
        self._scholarship = 0
        return "Рейтинг занизький для стипендії"

def function_in_module():
    """Це просто функція (згідно загальної термінології)
    """
    pass



class Car:
    """Описує автомобіль BMW."""
    
    def __init__(self, model: str, year: int, price: float):
        self.model = model
        self.year = year
        self.price = price
    
    def __repr__(self):
        return f"{self.model} ({self.year}) - {self.price} грн"


class BMWShowroom:
    """Описує автосалон BMW."""
    
    def __init__(self):
        self.cars = []
    
    def add_car(self, car: Car):
        """Додає автомобіль до автосалону."""
        self.cars.append(car)
        return f"Автомобіль '{car.model}' доданий до автосалону."
    
    def remove_car(self, model: str):
        """Видаляє автомобіль з автосалону за моделлю."""
        for car in self.cars:
            if car.model.lower() == model.lower():
                self.cars.remove(car)
                return f"Автомобіль '{model}' видалений з автосалону."
        return f"Автомобіль '{model}' не знайдений."
    
    def find_cars_by_year(self, year: int):
        """Повертає список автомобілів за роком."""
        return [car for car in self.cars if car.year == year]
    
    def display_cars(self):
        """Виводить всі автомобілі в автосалоні."""
        if not self.cars:
            return "Автосалон порожній."
        return "\n".join(str(car) for car in self.cars)


def function_in_module():
    """Це просто функція (згідно загальної термінології)"""
    pass
