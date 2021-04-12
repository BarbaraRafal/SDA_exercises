from ibuilder import IHouseBuilder
from house import House


class MyHouseBuilder(IHouseBuilder):
    def buid_wall(self):
        self._house.wall = "murawane"

    def install_window(self):
        self._house.window = "kuloodporne"

    def install_door(self):
        self._house.door = "antywłamaniowe"

    def lay_floor(self):
        self._house.floor = "panele"

    def plant_garden(self):
        self._house.garden = "duży"

    def install_garage(self):
        self._house.garage = True

    def excavate_pool(self):
        self._house.swimming_pool = True
