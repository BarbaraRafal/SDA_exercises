from ibuilder import IHouseBuilder


class MyHouseBuilder(IHouseBuilder):
    def build_wall(self):
        self._house.wall = "murawane"
        return self

    def install_window(self):
        self._house.window = "kuloodporne"
        return self

    def install_door(self):
        self._house.door = "antywłamaniowe"
        return self

    def lay_floor(self):
        self._house.floor = "panele"
        return self

    def plant_garden(self):
        self._house.garden = "duży"
        return self

    def install_garage(self):
        self._house.garage = True
        return self

    def excavate_pool(self):
        self._house.swimming_pool = True
        return self
