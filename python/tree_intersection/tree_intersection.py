
from dependices import  *
def tree_intersection(tree_a, tree_b):
    intersections = []
    table = Hashtable()
    tree_a_values = breadth_first(tree_a)
    tree_b_values = breadth_first(tree_b)
    for a_value in tree_a_values:
        table.add(str(a_value), None)
    for b_value in tree_b_values:
        if table.contains(str(b_value)):
            intersections.append(b_value)
    return None if not len(list(set(intersections))) else list(set(intersections))
