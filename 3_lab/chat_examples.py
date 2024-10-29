# Ось так нам допоміг ChatGPT зробити опис
class Students:
    """
    Клас Students для зберігання інформації про студентів.

    Attributes:
        surname (str): Прізвище студента.
        name (str): Ім'я студента.
        mark (int): Оцінка студента.
    """

    def __init__(self, surname: str, name: str, mark: int):
        """
        Ініціалізує новий екземпляр класу Students.

        Args:
            surname (str): Прізвище студента.
            name (str): Ім'я студента.
            mark (int): Оцінка студента, яка повинна бути цілим числом.
        """
        print("Викликаємо __init__")
        self.surname = surname
        self.name = name
        self.mark = mark