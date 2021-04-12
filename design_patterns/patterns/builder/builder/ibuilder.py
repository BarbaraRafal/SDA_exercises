import abc

from house import House


class IHouseBuilder(abc.ABC):

    def get_house(self):
        return self._house

    def build_house(self):
        self.new_house()
        self.buid_wall()
        self.install_window()
        self.install_door()
        self.lay_floor()
        self.install_garage()
        self.plant_garden()
        self.excavate_pool()

    def new_house(self):
        self._house = House()

    @abc.abstractmethod
    def buid_wall(self):
        pass

    @abc.abstractmethod
    def install_door(self):
        pass

    @abc.abstractmethod
    def install_door(self):
        pass

    @abc.abstractmethod
    def install_window(self):
        pass

    @abc.abstractmethod
    def lay_floor(self):
        pass

    @abc.abstractmethod
    def plant_garden(self):
        pass

    @abc.abstractmethod
    def install_garage(self):
        pass

    @abc.abstractmethod
    def excavate_pool(self):
        pass
