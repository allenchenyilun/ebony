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
        Set[Condition] Conditions //in future, considering a better way to sort conditions
        Evaluation evaluation 

    PRIVATE:
METHODS:
    CONSTRUCTOR:
    PUBLIC:
        String toString(bool show_condition) //convert a relationship to string
    PRIVATE:
"""
# LOG:
"""
07/07/2022; Allen Chen; Created the Class, Wrote the Class Description;
07/09/2022; Allen Chen; Wrote More Class Description;
"""
# IMPORTS:

# CODE:
class Relationship:
    def __init__(self, item_before, item_after, logic): # Classic constructor
        #TODO: id formation
        self.item_before = item_before
        self.item_after = item_after
        self.logic = logic