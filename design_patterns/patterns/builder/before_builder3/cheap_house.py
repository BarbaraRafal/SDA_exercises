from house import House


class CheapHouseBuilder:
    def get_house(self):
        return self._house

    def build_house(self):
        self._house = House()
        self.buid_wall()
        self.install_window()
        self.install_door()
        self.lay_floor()
        self.install_garage()
        self.plant_garden()
        self.excavate_pool()

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
