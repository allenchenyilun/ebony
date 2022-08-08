# for testing
from models.item import Item
from models.relationship import Relationship

apple = Item("apple")
apple.reference_name("apple")
apple.add_name("Ringo")

sweet = Item("sweet")
grown = Item("grown")
print(isinstance(apple, Item))
# print(not (isinstance(apple, Item) and isinstance(sweet, Item)))

apple_is_sweet = Relationship(apple, sweet, "is")
apple_is_sweet.add_condition("when", apple, grown, "is")
print(apple_is_sweet.to_string(True))
print(apple.name_list)
