# Import
from ops import get_key, is_goal, expands
from pd import pd

# Big num (represents infinity) and h table to store h values
big_num = 2000
h_table = {}


# Heuristic function : Return h in table if h exists, else calculate and add an entry to table
def _h(data):
    key = get_key(data)
    if key in h_table:
        return h_table[key]

    h = pd(data)
    h_table[key] = h
    return h


# Search algorithm
def _search(path, g, bound, keys):
    data = path[-1]
    h = _h(data)
    f = g + h

    if f > bound:
        return f

    if is_goal(data):
        return True

    min_val = big_num
    successors = expands(data, keys)
    sorted(successors, key=lambda x: _h(x))

    for successor in successors:
        successor_key = get_key(successor)

        path.append(successor)
        keys.add(successor_key)

        t = _search(path, g + 1, bound, keys)

        if t == True:
            return True

        if t < min_val:
            min_val = t

        path.pop()
        keys.remove(successor_key)

    return min_val


# IDA Star
def ida_star(root):
    bound = _h(root)
    path = [root]
    keys = {get_key(root)}

    while True:
        t = _search(path, 0, bound, keys)
        if t == True:
            return path
        if t == big_num:
            return None
        bound = t
        print("Change bound: " + str(bound))
