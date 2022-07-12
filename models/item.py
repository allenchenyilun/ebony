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
"""
# IMPORTS:

# CODE:

class Item:
    def __init__(name): # Classic constructor
        #TODO: check name format
        name_list = {name: 1}
        #TODO: id formation