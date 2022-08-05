# CLASS: Item
# DESCRIPTION: 
"""
This is a class that create an item, the item is not identified by name, but rather the id. Therefore, an item can have multiple name,
and a name can be associated with multiple items.
"""
# MODEL:
"""
VARIABLES:
    PUBLIC:
        Int id
        String name //name with the highest number of referenece
        Map[String, Int] name_list //list of names associated with number of referenced
        Item Parent // the model that the item is inherited from
        Set[Item] owner //ownership of the item
        Set[Relationship] relations
        Set[Relationship] properties //any relationship for item whose parent is this.
        String reference
        *Set[Item] type //any end item of a property that describe the type of the item (optional)

    PRIVATE:
METHODS:
    CONSTRUCTOR:
        (String name) //DEFULT CONSTRUCTOR
        (Item parent, Owner parent) //DEFULT CONSTRUCTOR for inheriting from a 
        (Int id) //CONSTRUCTOR 
    PUBLIC:
        add_name(String name) //add name to a name list, initialized number of referenced
        reference_name(String name)
        add_owner(Item owener)
        add_relation(Relationship relation) //require that the suject is this item
        add_properties(Relationship relation) //require that item is the owner of the subject
        
    PRIVATE:
"""
# LOG:
"""
07/07/2022; Allen Chen; Wrote the Class Description;
07/09/2022; Allen Chen; Wrote More Class Description;
07/11/2022; Allen Chen; Wrote More Class Description, created the class;
08/05/2022; Allen Chen; Updated __init__ with variable "name", create and wrote add_name, tested them all;
"""
# IMPORTS:

# CODE:

class Item:
    def __init__(self, name): # Classic constructor
        #TODO: check name format
        self.name_list = {name: 1}
        self.name = name
        #TODO: id formation
    
    def add_name(self, name):
        if self.name_list.__contains__(name):
            self.name_list[name] = self.name_list[name] + 1
        else: self.name_list[name] = 1
        self.name = max(self.name_list, key=self.name_list.get)