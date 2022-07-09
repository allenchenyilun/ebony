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
        Map[String, Int] name_list
        Set[Relationship] sub_relations
        Set[Relationship] par_relations
        Set[Item] Type
        String reference

    PRIVATE:
METHODS:
    PUBLIC:
    PRIVATE:
"""
# LOG:
"""
07/07/2022; Allen Chen; Wrote the Class Description;
07/09/2022; Allen Chen; Wrote More Class Description;
"""