# Import
from numpy import array_equal
from copy import deepcopy

# Goal
goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


# Find zero : Find the position of zero in data
def _find_zero(data):
    for i in range(len(data)):
        if data[i] == 0:
            return i


# Express : Print out the data as 4 x 4
def _express(data):
    for y in range(4):
        for x in range(4):
            print(str(data[x + y * 4]) + " ", end="")
        print()


# Get key : Return key of data
def get_key(data):
    return ".".join(map(str, data))


# Is goal : Check if this data matches goal
def is_goal(data):
    return array_equal(data, goal)


# Expands : Expands stuff with key
def expands(data, keys):
    z = _find_zero(data)

    mlist = []

    if z > 3:  # Can not move up if z in {0, 1, 2, 3} -> z > 3
        up = deepcopy(data)

        up[z] = up[z - 4]
        up[z - 4] = 0

        if get_key(up) not in keys:
            mlist.append(up)

    if z < 12:  # Can not move down if z in {12, 13, 14, 15} -> z < 12
        down = deepcopy(data)

        down[z] = down[z + 4]
        down[z + 4] = 0

        if get_key(down) not in keys:
            mlist.append(down)

    if z % 4 != 0:  # Can not move left if z in {0, 4, 8, 12} -> z % 4 != 0
        left = deepcopy(data)

        left[z] = left[z - 1]
        left[z - 1] = 0

        if get_key(left) not in keys:
            mlist.append(left)

    if z % 4 != 3:  # Can not move right if z in {3, 7, 11, 15} -> z % 4 != 3
        right = deepcopy(data)

        right[z] = right[z + 1]
        right[z + 1] = 0

        if get_key(right) not in keys:
            mlist.append(right)

    return mlist


# Present : Take a data list (path) and return the presentation of solution
def present(data_list):
    print("State 0 - Initial:")
    _express(data_list[0])

    if len(data_list[0]) == 1:
        return

    step = 0
    for i in range(1, len(data_list)):
        step += 1
        old_z = _find_zero(data_list[i - 1])
        new_z = _find_zero(data_list[i])
        dis = new_z - old_z

        if dis == 4:
            print("State " + str(step) + " by 0 going down, slide up:")  # dis = 4 -> Down
        elif dis == -4:
            print("State " + str(step) + " by 0 going up, slide down:")  # dis = -4 -> Up
        elif dis == 1:
            print("State " + str(step) + " by 0 going right, slide left:")  # dis = 1 -> Right
        else:
            print("State " + str(step) + " by 0 going left, slide right:")  # dis = -1 -> Left

        _express(data_list[i])


# Is solvable : Check if this puzzle is solvable
def is_solvable(data):
    id = 0
    z = -1

    for i in range(len(data) - 1):
        if data[i] == 0:
            z = i
            continue
        for j in range(i + 1, len(data)):
            if data[j] == 0:
                z = j
                continue
            if data[j] < data[i]:
                id += 1
    return (id % 2 == 0 and (z // 4) % 2 == 1) or (id % 2 == 1 and (z // 4) % 2 == 0)
