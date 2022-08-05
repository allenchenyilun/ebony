# CLASS: Ralationship
# DESCRIPTION: 
"""
This is a class that create a logical expression of two items, hence created a relationship with two items.
Relations would have sub-relations, then it would create a knowledge graph with these relationships.
"""
# MODEL:
"""
VARIABLES:
    PUBLIC:
        Int id
        Item item_before
        Item item_after
        Int logic //currently needs no logic to be an object
            Logic: "is"
        Set[Condition] Conditions //in future, considering a better way to sort conditions
        Evaluation evaluation 

    PRIVATE:
METHODS:
    CONSTRUCTOR:
    PUBLIC:
        String to_string(bool show_condition) //convert a relationship to string
        add_condition(self, item_before, item_after, logic) # add a condition to relationship
    PRIVATE:
"""
# LOG:
"""
07/07/2022; Allen Chen; Created the Class, Wrote the Class Description;
07/09/2022; Allen Chen; Wrote More Class Description;
08/05/2022; Allen Chen; wrote and tested add_condition and to_string;
"""
# IMPORTS:
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from item import *
from condition import *

# CODE:
class Relationship:
    def __init__(self, item_before, item_after, logic): # Classic constructor
        #TODO: id formation
        # check type (need to be solved)
        # if not (isinstance(item_before, Item) and isinstance(item_after, Item)): # make sure item_before and item_after is in the class "item"
        #     raise Exception("class 'Relationship' contructor failed: type error")
        self.item_before = item_before
        self.item_after = item_after
        self.logic = logic
        self.condition_exist = False # default: no condition
    
    def add_condition(self, type, item_before, item_after, logic): # add a condition to relationship
        self.condition = Condition(type, item_before, item_after, logic)
        self.condition_exist = True # now there is a condition
    
    def to_string(self, show_condition): # convert relationship to string
        if show_condition == True:
            if self.condition_exist == True:
                return  self.item_before.name + " " + self.logic + " " + self.item_after.name + " " + self.condition.to_string()
            else:
                raise Exception("request failed: condition does not exist")
        else:
            return self.item_before.name + " " + self.logic + " " + self.item_after.name
