from Star import Star
from File import File


class AstronomicalAtlas:
    """
    · наповнення інформації з файлу про зірки і планети;
    · пошук зірок-гігантів;
    · визначення планети з найбільшою масою;
    · пошук космічного об’єкта з атласу з найменшою температурою поверхні;
    """
    def __init__(self, lst_object=[]):
        self.__lst_object = lst_object

    def read_from_file(self, name_file):
        self.__lst_object = File.read_from_file_to_list(name_file)

    def stars_giant(self):
        lst_star_giant = [obj for obj in self.__lst_object if
                          isinstance(obj, Star) and Star.GIANT_STAR <= obj.size]
        return lst_star_giant

    def the_biggest_mass(self):
        return max(self.__lst_object, key=lambda obj: obj.mass)

    def object_the_least_t(self):
        return min(self.__lst_object, key=lambda obj: obj.t)
