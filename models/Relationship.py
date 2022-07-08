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
        Item item_before
        Item item_after
        Logic logic
        Logictree[Condition] Conditions
        Evaluation Evaluation 

    PRIVATE:
METHODS:
    PUBLIC:
    PRIVATE:
"""
# LOG:
"""
07/07/2022; Allen Chen; Created the Class, Wrote the Class Description
"""

class Relationship:
    def __init__(self, item_before, item_after, logic):
        self.item_before = item_before
        self.item_after = item_after
        self.logic = logic