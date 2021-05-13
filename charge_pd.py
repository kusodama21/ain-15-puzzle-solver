# This file should only be run once as it fills the 3 empty json files: pdA, pdB and pdC for look up.
# After running the first time, you should comment out the function "run" in order to avoid it running again.

# Import
from json import dump
from queue import Queue
from copy import deepcopy

# Goal states for each pattern A, B, C (irrelevant tiles are represented by -1)
goal_A = [1, 2, 3, 4,
          -1, -1, 7, -1,
          -1, -1, -1, -1,
          -1, -1, -1, 0]
goal_B = [-1, -1, -1, -1,
          5, 6, -1, -1,
          9, 10, -1, -1,
          13, -1, -1, 0]
goal_C = [-1, -1, -1, -1,
          -1, -1, -1, 8,
          -1, -1, 11, 12,
          -1, 14, 15, 0]

# A set of relevant entries for each pattern A, B, C
re_A = {1, 2, 3, 4, 7}
re_B = {5, 6, 9, 10, 13}
re_C = {8, 11, 12, 14, 15}


# _to_cs (to cache string): Return the cache string of data
# The cache string considers 0 as the same importance as relevant entries
def _to_cs(data, re):
    cl = []  # Component list, which later will be converted to cache string

    fst_re = True  # The first component is expected to be relevant, this will turn false after the first iteration
    irr_pended = False  # Check if there are irrelevant tiles before the current process relevant tile
    irr_num = 0  # The number of irrelevant tiles pended

    for tile in data:
        if tile in re or tile == 0:
            if irr_pended:
                if fst_re:
                    fst_re = False

                cl.append("i" + str(irr_num))
                irr_pended = False
                irr_num = 0
            if fst_re:
                cl.append(str(tile))
                fst_re = False
            else:
                cl.append("." + str(tile))
        else:
            irr_num += 1
            if not irr_pended:
                irr_pended = True

    # Last check since the ending tile may not be relevant, as it will not pend the irrelevant tiles at the end
    if irr_pended:
        cl.append("i" + str(irr_num))

    return "".join(cl)


# to_ps (to pattern string): Return the pattern string of data
# The pattern string does not consider 0 as the same importance as relevant entries
# The private indicator "_" is removed since this will be used again to look up on json files.
def to_ps(data, re):
    cl = []  # Component list, which later will be converted to pattern string

    fst_re = True  # The first component is expected to be relevant, this will turn false after the first iteration
    irr_pended = False  # Check if there are irrelevant tiles before the current process relevant tile
    irr_num = 0  # The number of irrelevant tiles pended

    for tile in data:
        if tile in re:
            if irr_pended:
                if fst_re:
                    fst_re = False

                cl.append("i" + str(irr_num))
                irr_pended = False
                irr_num = 0
            if fst_re:
                cl.append(str(tile))
                fst_re = False
            else:
                cl.append("." + str(tile))
        else:
            irr_num += 1
            if not irr_pended:
                irr_pended = True

    # Last check since the ending tile may not be relevant, as it will not pend the irrelevant tiles at the end
    if irr_pended:
        cl.append("i" + str(irr_num))

    return "".join(cl)


# _charge : This function inserts entries to a given pattern string dictionary
def _charge(data_queue, g, pattern_dict, cache_set, re):
    print("On turn!")
    if data_queue.empty():
        return

    pass_queue = Queue()
    g_increased = False

    while not data_queue.empty():
        data = data_queue.get()

        z = -1  # Index of 0
        for i in range(len(data)):
            if data[i] == 0:
                z = i
                break

        # Condition to go up : z not in {0, 1, 2, 3} -> z > 3
        if z > 3:
            up = deepcopy(data)

            up[z] = up[z - 4]
            up[z - 4] = 0

            up_cs = _to_cs(up, re)

            # Check cache set: If exists then do nothing, if not than add to set and queue, check dict
            if up_cs not in cache_set:
                cache_set.add(up_cs)
                pass_queue.put(up)

                # Check dictionary: If exist then do nothing, if no than add to queue
                up_ps = to_ps(up, re)
                if up_ps not in pattern_dict:
                    if not g_increased:
                        g += 1
                        g_increased = True
                    pattern_dict[up_ps] = g

        # Condition to go down : z not in {12, 13, 14, 15} -> z < 12
        if z < 12:
            down = deepcopy(data)

            down[z] = down[z + 4]
            down[z + 4] = 0

            down_cs = _to_cs(down, re)

            # Check cache set: If exists then do nothing, if not than add to set and queue, check dict
            if down_cs not in cache_set:
                cache_set.add(down_cs)
                pass_queue.put(down)

                # Check dictionary: If exist then do nothing, if no than add to queue
                down_ps = to_ps(down, re)
                if down_ps not in pattern_dict:
                    if not g_increased:
                        g += 1
                        g_increased = True
                    pattern_dict[down_ps] = g

        # Condition to go left : z not in {0, 4, 8, 12} -> z % 4 != 0
        if z % 4 != 0:
            left = deepcopy(data)

            left[z] = left[z - 1]
            left[z - 1] = 0

            left_cs = _to_cs(left, re)

            # Check cache set: If exists then do nothing, if not than add to set and queue, check dict
            if left_cs not in cache_set:
                cache_set.add(left_cs)
                pass_queue.put(left)

                # Check dictionary: If exist then do nothing, if no than add to queue
                left_ps = to_ps(left, re)
                if left_ps not in pattern_dict:
                    if not g_increased:
                        g += 1
                        g_increased = True
                    pattern_dict[left_ps] = g

        # Condition to go right : z not in {3, 7, 11, 15} -> z % 4 != 3
        if z % 4 != 3:
            right = deepcopy(data)

            right[z] = right[z + 1]
            right[z + 1] = 0

            right_cs = _to_cs(right, re)

            # Check cache set: If exists then do nothing, if not than add to set and queue, check dict
            if right_cs not in cache_set:
                cache_set.add(right_cs)
                pass_queue.put(right)

                # Check dictionary: If exist then do nothing, if no than add to queue
                right_ps = to_ps(right, re)
                if right_ps not in pattern_dict:
                    if not g_increased:
                        g += 1
                        g_increased = True
                    pattern_dict[right_ps] = g

    # Recursion
    _charge(pass_queue, g, pattern_dict, cache_set, re)


# _write : This function will write the pattern string dictionary into a file given as string
def _write(goal, re, file_str):
    data_queue = Queue()
    data_queue.put(goal)

    pattern_dict = {to_ps(goal, re): 0}
    cache_set = {_to_cs(goal, re)}

    _charge(data_queue, 0, pattern_dict, cache_set, re)

    del cache_set
    with open(file_str, "w") as f:
        dump(pattern_dict, f)
        print("Successfully inserted " + str(len(pattern_dict)) + " entries into file " + file_str)


# run : Run the charging process
def run():
    _write(goal_A, re_A, "pdA.json")
    _write(goal_B, re_B, "pdB.json")
    _write(goal_C, re_C, "pdC.json")


# Comment this out after the first run (since there are other files that use functions from this file)
# The procedure will take about 30 - 35 minutes (on my PC with Ryzen 3 and 4 GB RAM it takes 32 minutes)
# In this folder, the json files have been filled already, so no need to run this
# run()
