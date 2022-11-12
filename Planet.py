from SpaceObject import SpaceObject


class Planet(SpaceObject):

    def __init__(self, name: str, size: int, mass: int, t: int, has_atmosphere: bool):
        super().__init__(name, size, mass, t)
        self.__has_atmosphere = has_atmosphere

    @property
    def has_atmosphere(self):
        return self.__has_atmosphere

    def __str__(self):
        return f"Name of star: {self.name}\nSize: {self.size}\nMass: {self.mass}\nTemperature: {self.t}\nAtmosphere: {self.has_atmosphere}"

    def suitable_for_life(self):
        if self.__has_atmosphere and self.has_normal_temperature_for_live():
            print("This planet can have live")
        else:
            print("This planet can`t have live")
