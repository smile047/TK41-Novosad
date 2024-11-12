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





class MySuperClass:
    total_students = 0  # Атрибут класу для підрахунку кількості студентів
    total_marks = 0  # Атрибут класу для підрахунку суми балів
    college_raiting = "Високий"  # Загальний рейтинг коледжу
    var_lover_case = "Змінна класу"  # Тепер це атрибут класу
    
    def __init__(self, surname: str, name: str, mark: int, group=None):
        """
        Ініціалізуємо об'єкт, підраховуємо студентів та додаємо їхні бали.
        """
        self.__surname = surname
        self.__name = name
        self.mark = mark  # Оцінка студента
        self.group = group  # Група студента
        
        # Підвищуємо кількість студентів
        MySuperClass.total_students += 1
        
        # Додаємо оцінку до загальної суми балів
        MySuperClass.total_marks += self.mark

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @classmethod
    def get_avg_mark(cls):
        """Метод класу для розрахунку середнього балу."""
        if cls.total_students == 0:
            return 0
        return cls.total_marks / cls.total_students

    def __repr__(self):
        return f"Студент {self.surname} {self.name}, Оцінка: {self.mark}"

