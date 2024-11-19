class MySuperClass:
    """Тестовий клас, зараз реалізуємо опис студента
    
    ---

    surname : str
        Прізвище студента
    
    """
    var_lover_case = "Це проста класова змінна"
    COLLEGE_NAME = "Це подібне до константи в клосі, але ми можемо її перезаписати"
    _protected_var = 1
    __private_var = 2

    total_students = 0
    total_marks = 0

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

        self.var_lover_case = "Перазаписали класові змінну"
        MySuperClass.total_students += 1
        MySuperClass.total_marks += mark


    def __del__(self):
        print("Відрахували студента")
        MySuperClass.total_students -= 1

    @property
    def college_raiting(self):
        return MySuperClass.total_marks / MySuperClass.total_students

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
            self._scholarship = "1800 грн"
            return "Присвоєно підвищену стипундію"
        if raiting == 4:
            self._scholarship = "1400 грн"
            return "Присвоєно звичайну стипундію"
        self._scholarship = 0
        return "Рейтинг занизький для стипендії"
    
    def panishment(self):
        return "Ми прийшли додому і мама нас насварила за погані оцінки"
    
    @staticmethod
    def hobbi(h=None):
        """в таких методах нема вказівника на обєкт
        """
        if h:
            print(f"В мене зявилось хоббі {h}")
        else:
            print("На жаль в мене немає Хаббі")
    
    @classmethod
    def create_from_surname_name(cls, full_name:str):
        """ альтернативний конструктор, створюємо обєкт з повного імені
        розчеплюємо повне імя на частинки Прізкище та Імя
        """
        surname, name = full_name.split(" ")
        return cls(surname, name, 0)
    
    @classmethod
    def create_from_name_surname(cls, full_name:str):
        """ альтернативний конструктор, створюємо обєкт з повного імені
        розчеплюємо повне імя на частинки Прізкище та Імя
        """
        name, surname = full_name.split(" ")
        return cls(surname, name, 0)


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
    
class Person:
    """Клас, що описує особу: ім'я, вік, стать і хобі.
    
    Атрибути:
    - name : str : ім'я особи
    - age : int : вік особи
    - gender : str : стать особи (чоловік/жінка)
    """
    
    total_persons = 0  # Загальна кількість осіб
    
    def __init__(self, name: str, age: int, gender: str):
        """Ініціалізуємо атрибути класу: ім'я, вік, стать"""
        self.name = name
        self.age = age
        self.gender = gender
        Person.total_persons += 1  # Збільшуємо загальну кількість осіб

    def greet(self):
        """Метод для вітання"""
        return f"Привіт! Мене звати {self.name}, мені {self.age} років."

    def punishment(self):
        """Метод для опису покарання"""
        return f"{self.name} отримав(ла) покарання за погану поведінку."

    @staticmethod
    def hobby(h=None):
        """Статичний метод для хобі. Якщо передано хобі - виводимо його, якщо ні - повідомлення про відсутність хобі"""
        if h:
            print(f"{h} стало моїм новим хобі!")
        else:
            print("На жаль, у мене немає хобі.")

class MySuperClass:
    """Тестовий клас, зараз реалізуємо опис студента"""
    
    var_lover_case = "Це проста класова змінна"
    COLLEGE_NAME = "Це подібне до константи в класі, але ми можемо її перезаписати"
    _protected_var = 1
    __private_var = 2

    total_students = 0
    total_marks = 0

    def __init__(self, surname: str, name: str, mark: int, group=None):
        """
        Ініціалізуємо об'єкт
        - в середині конструктора створюються атрибути
        """
        print("Викликаємо __init__")
        self.__surname = surname  # private атрибут
        self.__name = name
        self.mark = mark  # public атрибут
        self.group = group
        self._age = None  # protected атрибут
        self._scholarship = 0

        self.var_lover_case = "Переозначили класову змінну"
        MySuperClass.total_students += 1
        MySuperClass.total_marks += mark

    def __del__(self):
        print("Відрахували студента")
        MySuperClass.total_students -= 1

    @property
    def college_raiting(self):
    if MySuperClass.total_students == 0:
        return 0  # Повертаємо 0, якщо немає студентів
    return MySuperClass.total_marks / MySuperClass.total_students


    @property
    def name(self):
        """Ця властивість є закритою, її можна читати, але не змінювати"""
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def say_hello(self):
        a = 1 + 2
        return f"Привіт {a}"
    
    def __repr__(self):
        return "Представлення об'єкту Студент, його задають: MySuperClass(surname, name, mark)"
    
    def __len__(self):
        return len(self.surname)
    
    def function_in_class(self):
        """Це вже метод згідно термінології, і він публічний"""
        return "Ми викликали публічний метод"

    def _protected_method_in_class(self):
        """Це захищений метод"""
        self.__this_is_private()
        return "Ми доступаємося до захищеного методу"
    
    def __this_is_private(self):
        print("Це приватний метод!")

    def calculate_scholarship_after_session(self, raiting: int):
        if raiting == 5:
            self._scholarship = "1800 грн"
            return "Присвоєно підвищену стипендію"
        if raiting == 4:
            self._scholarship = "1400 грн"
            return "Присвоєно звичайну стипендію"
        self._scholarship = 0
        return "Рейтинг занизький для стипендії"
    
    def panishment(self):
        return "Ми прийшли додому і мама нас насварила за погані оцінки"
    
    @staticmethod
    def hobbi(h=None):
        """в таких методах нема вказівника на об'єкт"""
        if h:
            print(f"В мене з'явилось хоббі {h}")
        else:
            print("На жаль, в мене немає хоббі")
    
    @classmethod
    def create_from_surname_name(cls, full_name: str):
        """Альтернативний конструктор, створюємо об'єкт з повного імені
        розчеплюємо повне ім'я на частинки Прізвище та Ім'я"""
        surname, name = full_name.split(" ")
        return cls(surname, name, 0)
    
    @classmethod
    def create_from_name_surname(cls, full_name: str):
        """Альтернативний конструктор, створюємо об'єкт з повного імені
        розчеплюємо повне ім'я на частинки Ім'я та Прізвище"""
        name, surname = full_name.split(" ")
        return cls(surname, name, 0)

def function_in_module():
    """Це просто функція"""
    pass

