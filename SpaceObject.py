class SpaceObject:
    """
    13. Клас “Космічний об’єкт”.
Поля:
    · назва;
    · величина;
    · маса;
    · температура поверхні.

Методи:
    · визначення, у скільки разів маса об’єкта більша або менша від маси Землі.
    · перевірки, чи температура об’єкта є в межах діапазону існування живих організмів.
    """

    MASS_EARTH = 6 * 10 ** 24
    MAXIMUM_LIVING_T = 60
    MINIMUM_LIVING_T = -37

    def __init__(self, name: str, size: int, mass: int, t: int):
        if not isinstance(name, str):
            raise ValueError(f"attribute 'name' must be str type, but no '{type(name)}'")
        elif not isinstance(size, int):
            raise ValueError(f"attribute 'size' must be int type, but no {type(name)}")
        elif not isinstance(mass, int):
            raise ValueError(f"attribute 'mass' must be int type, but no '{type(name)}'")
        elif not isinstance(t, int):
            raise ValueError(f"attribute 't' must be str type, but no '{type(name)}'")
        self.__name = name
        self.__size = size
        self.__mass = mass
        self.__t = t

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def mass(self):
        return self.__mass

    @property
    def t(self):
        return self.__t

    def __str__(self):
        return f"Name: {self.name}\nSize: {self.size}\nMass: {self.mass}\nTemperature: {self.t}"

    def comparison_with_the_earth_mass(self):
        if self.mass < SpaceObject.MASS_EARTH:
            print(
                f"the mass of the object is {SpaceObject.MASS_EARTH / self.mass:.2f} times less than the mass of the earth")
        else:
            print(
                f"the mass of the object is {self.mass / SpaceObject.MASS_EARTH:.2f} times biggest than the mass of the earth")

    def living_temperature(self):
        if SpaceObject.MINIMUM_LIVING_T < self.t < SpaceObject.MAXIMUM_LIVING_T:
            print("Normal temperature for live")
        else:
            print("No normal temperature for live")

    def has_normal_temperature_for_live(self):
        if SpaceObject.MINIMUM_LIVING_T < self.t < SpaceObject.MAXIMUM_LIVING_T:
            return True
        else:
            return False
