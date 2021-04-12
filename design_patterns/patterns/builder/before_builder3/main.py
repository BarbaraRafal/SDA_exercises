from my_house import MyHouseBuilder
from cheap_house import CheapHouseBuilder

print("\nDrogi dom:")
builder = MyHouseBuilder()
builder.build_house()
house = builder.get_house()
house.display()

print("\nTani dom:")
builder = CheapHouseBuilder()
builder.build_house()
house = builder.get_house()
house.display()
