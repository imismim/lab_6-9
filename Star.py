from SpaceObject import SpaceObject


class Star(SpaceObject):
    GIANT_STAR = 696_340
    BRIGHTNESS = (-9, 9)

    def __init__(self, name: str, size: int, mass: int, t: int, brightness: int):
        super().__init__(name, size, mass, t)
        if not Star.BRIGHTNESS[0] <= brightness <= Star.BRIGHTNESS[1]:
            raise ValueError(
                f"Brightness is {brightness}, this number must be in range ({Star.BRIGHTNESS[0]},{Star.BRIGHTNESS[1]})")
        self.__brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    def __str__(self):
        return f"Name of star: {self.name}\nSize: {self.size}\nMass: {self.mass}\nTemperature: {self.t}\nBrightness: {self.brightness}"

    def giant_or_dwarf(self):
        if Star.GIANT_STAR <= self.size:
            print("This star is giant")
        else:
            print("This star is dwarf")
