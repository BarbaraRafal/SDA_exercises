from ibuilder import IHouseBuilder
from house import House


class CheapHouseBuilder(IHouseBuilder):
    def buid_wall(self):
        self._house.wall = "drewniane"

    def install_window(self):
        self._house.window = "stardard"

    def install_door(self):
        self._house.door = "standard"

    def lay_floor(self):
        self._house.floor = "parkiet"

    def plant_garden(self):
        self._house.garden = "mały"

    def install_garage(self):
        self._house.garage = True

    def excavate_pool(self):
        self._house.swimming_pool = False
