# CLASS: Condition
# DESCRIPTION: 
"""
A Condition is where a relation sit under. The condition are a special type of relationship that is not a fact, but a premise.
"""
# MODEL:
"""
VARIABLES:
    PUBLIC:
        Int relation_id
        Int type //Type of condition such as "When", "Assuming that", "Because", etc. (or extend?)
            coded type: when => 0, assuming that => 1, because => 2.
        Item item_before
        Item item_after
        Logic logic
        String reference //For facts

    PRIVATE:
METHODS:
    CONSTRUCTOR:
        (self, type, item_before, item_after, logic) # Classic constructor
    PUBLIC:
        to_string() # convert condition to string
    PRIVATE:
"""
# LOG:
"""
07/09/2022; Allen Chen; Wrote the Class Description;
08/05/2022; Allen Chen; Wrote and tested __init__ and to_string;
"""
# IMPORTS:

from item import *

# CODE:

class Condition:
    def __init__(self, type, item_before, item_after, logic): # Classic constructor
        #TODO: id formation
        # coded type: when => 0, assuming that => 1, because => 2.
        if isinstance(item_before, Item) and isinstance(item_after, Item): # make sure item_before and item_after is in the class "item"
            raise Exception("class 'Relationship' contructor failed: type error")
        if type == "when":
            self.type = 0
        elif type == "assuming that":
            self.type = 1
        else:
            self.type = 2
        self.item_before = item_before
        self.item_after = item_after
        self.logic = logic
    
    def to_string(self): # convert condition to string
        if self.type == 0:
            out_type = "when"
        elif self.type == 1:
            out_type = "assuming that"
        else:
            out_type = "because"
        return out_type + " " + self.item_before.name + " " + self.logic + " " + self.item_after.name