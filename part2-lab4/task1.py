class Animal:
    pass


class Animal:
    """
    Базовый класс для всех животных.

    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
        _species (str): Вид животного (инкапсулированный атрибут).
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Конструктор класса Animal.

        Аргументы:
            name (str): Имя животного.
            age (int): Возраст животного.
            species (str): Вид животного.
        """
        self.__name = name
        self.__age = age
        self.__species = species  # Инкапсулированный атрибут, так как вид животного не должен изменяться извне.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя.
        """
        return f"{self.name} ({self._species}), возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчика.
        """
        return f"Animal(name={self.name}, age={self.age}, species={self._species})"

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает животное.
        """
        return "Неизвестный звук"

    def get_species(self) -> str:
        """
        Возвращает вид животного.
        """
        return self._species


    class Dog(Animal):
        """
        Дочерний класс для собак.

        Атрибуты:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            breed (str): Порода собаки.
        """

        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            Конструктор класса Dog.

            Аргументы:
                name (str): Имя собаки.
                age (int): Возраст собаки.
                breed (str): Порода собаки.
            """
            super().__init__(name, age, species="Canis lupus familiaris")
            self.breed = breed

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта для пользователя.
            """
            return f"{self.name} ({self.breed}), возраст: {self.age} лет"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта для разработчика.
            """
            return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

        def make_sound(self) -> str:
            """
            Возвращает звук, который издает собака.
            Перегруженный метод, так как собака издает специфический звук.
            """
            return "Гав-гав!"

        def fetch(self, item: str) -> str:
            """
            Возвращает строку, описывающую, как собака приносит предмет.

            Аргументы:
                item (str): Предмет, который приносит собака.
            """
            return f"{self.name} приносит {item}!"
