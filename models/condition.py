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
        Item item_before
        Item item_after
        Logic logic
        String reference //For facts

    PRIVATE:
METHODS:
    CONSTRUCTOR:
    PUBLIC:
    PRIVATE:
"""
# LOG:
"""
07/09/2022; Allen Chen; Wrote the Class Description;
"""
# IMPORTS:

# CODE: