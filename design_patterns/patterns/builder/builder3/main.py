from director import Director
from my_house import MyHouseBuilder
from cheap_house import CheapHouseBuilder

print("\nDrogi dom:")

builder = MyHouseBuilder()
director = Director(builder)
director.build_house()
house = director.get_house()
house.display()


print("\nTani dom:")
builder = CheapHouseBuilder()
director = Director(builder)
director.build_house()
house = director.get_house()
house.display()
