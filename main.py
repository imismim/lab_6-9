from AstronomicalAtlas import AstronomicalAtlas
from File import File

if __name__ == '__main__':
    lst = File.read_from_file_to_list("data.txt")
    aa = AstronomicalAtlas()
    aa.read_from_file("data.txt")

    print("\t\t\tSTARS GIANT")
    File.print_lst(aa.stars_giant())

    print("\t\t\tThe SMALLEST T OBJECT")
    print(aa.object_the_least_t())

    print("\t\t\tThe BIGGEST MASS OBJECT")
    print(aa.the_biggest_mass())
