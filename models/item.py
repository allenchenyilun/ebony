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
        Item owner //ownership of the item
        Bool has_owner
        Set[Relationship] relations
        Set[Relationship] properties //any relationship for item whose parent is this.
        String reference
        *Set[Item] type //any end item of a property that describe the type of the item (optional)

    PRIVATE:
METHODS:
    CONSTRUCTOR:
        (String name) //DEFULT CONSTRUCTOR
        (Item parent, Owner parent) //DEFULT CONSTRUCTOR for inheriting from another class
        (Int id) //CONSTRUCTOR 
    PUBLIC:
        add_name(String name) //add name to a name list, initialized number of referenced
        reference_name(String name)
        add_owner(Item owner)
        change_owner(Item owner)
        add_relation(Relationship relation) //require that the suject is this item
        add_property(Relationship relation) //require that item is the owner of the subject
        
    PRIVATE:
"""
# LOG:
"""
07/07/2022; Allen Chen; Wrote the Class Description;
07/09/2022; Allen Chen; Wrote More Class Description;
07/11/2022; Allen Chen; Wrote More Class Description, created the class;
08/05/2022; Allen Chen; Updated __init__ with variable "name", create and wrote add_name, tested them all;
08/07/2022; Allen Chen; Updated add_name, wrote reference_name, add_owner, change_owner, add_relation, add_property, 
"""
# IMPORTS:

# CODE:

from asyncio.windows_events import NULL


class Item:
    def __init__(self, name): # Classic constructor
        #TODO: check name format
        self.name_list = {name: 1}
        self.name = name
        self.has_owner = False
        self.relations = []
        self.properties = []
        #TODO: id formation
    
    def add_name(self, name): #add name to a name list, initialized number of referenced
        if self.name_list.__contains__(name):
            raise Exception("class 'Item' add_name failed: name already exist.")
        else: self.name_list[name] = 1
        self.name = max(self.name_list, key=self.name_list.get)

    def reference_name(self, name): #reference a name in the namelist.
        if self.name_list.__contains__(name):
            self.name_list[name] = self.name_list[name] + 1
        else: raise Exception("class 'Item' reference_name failed: name does not exist.")
        self.name = max(self.name_list, key=self.name_list.get)

    def add_owner(self, owner):
        if self.has_owner:
            raise Exception("class 'Item' add_owner failed: owner already exist.")
        else: self.owner = owner
    
    def change_owner(self, owner):
        if self.has_owner:
            self.owner = owner
        else: raise Exception("class 'Item' change_owner failed: owner does not exist.")
    
    def add_relation(self, relation):
        # TODO: check duplicate by id
        # for self_relation in self.relations:
        if relation.item_before == self:
            self.relations.append(relation)
        else: raise Exception("class 'Item' add_relation failed: the relation is not related to this item.")
    
    def add_property(self, property):
        # TODO: check duplicate by id
        if property.item_before.has_owner:
            if property.item_before.owner == self:
                self.properties.append(property)
            else: raise Exception("class 'Item' add_property failed: the relation is not a property of this item.")
        else: raise Exception("class 'Item' add_property failed: the relation is not related to this item.")