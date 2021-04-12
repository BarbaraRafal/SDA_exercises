from ibuilder import IHouseBuilder


class CheapHouseBuilder(IHouseBuilder):
    def build_wall(self):
        self._house.wall = "drewniane"
        return self

    def install_window(self):
        self._house.window = "stardard"
        return self

    def install_door(self):
        self._house.door = "standard"
        return self

    def lay_floor(self):
        self._house.floor = "parkiet"
        return self

    def plant_garden(self):
        self._house.garden = "mały"
        return self

    def install_garage(self):
        self._house.garage = True
        return self

    def excavate_pool(self):
        self._house.swimming_pool = False
        return self
