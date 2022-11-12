from SpaceObject import SpaceObject
from Star import Star
from Planet import Planet


class File:
    @staticmethod
    def read_from_file_to_list(name_file):
        lst_object = []
        with open(name_file, "r") as f:
            lst_info = f.readlines()
        for i in range(len(lst_info)):
            object = lst_info[i].split()
            object[2] = int(object[2])
            object[3] = eval(object[3])
            object[4] = int(object[4])
            match object[0]:
                case "O":
                    lst_object.append(SpaceObject(*object[1:]))
                case "S":
                    object[5] = int(object[5])
                    lst_object.append(Star(*object[1:]))
                case "P":
                    object[5] = True if object[5] == "True" else False
                    lst_object.append(Planet(*object[1:]))

        return lst_object

    @staticmethod
    def print_lst(lst_object: list):
        for obj in lst_object:
            if isinstance(obj, Star):
                print(obj)
                obj.comparison_with_the_earth_mass()
                obj.living_temperature()
                obj.giant_or_dwarf()
            elif isinstance(obj, Planet):
                print(obj)
                obj.comparison_with_the_earth_mass()
                obj.living_temperature()
                obj.suitable_for_life()
            elif isinstance(obj, SpaceObject):
                print(obj)
                obj.comparison_with_the_earth_mass()
                obj.living_temperature()
            print()
