from ibuilder import IHouseBuilder


class Director:
    def __init__(self, builder: IHouseBuilder):
        self._builder = builder

    def build_house(self):
        # płynny interfejs (fluent interface)
        self._builder\
            .new_house()\
            .build_wall()\
            .install_window()\
            .install_door()\
            .lay_floor()\
            .install_garage()\
            .plant_garden()\
            .excavate_pool()

    def get_house(self):
        return self._builder.get_house()
