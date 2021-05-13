# Import
from ops import is_solvable, present
from time import time
from idastar import ida_star


# Main function
def main(data):
    if not is_solvable(data):
        print("This is not solvable")
    else:
        start = time()
        path = ida_star(data)
        present(path)
        print("Time taken: " + str(time() - start) + " seconds.")


# Experiment 1: Devil's configuration
# Steps: 100, time: < 0.06 seconds
# d1 = [1, 5, 9, 13,
#       2, 6, 10, 14,
#       3, 7, 11, 15,
#       4, 8, 12, 0]


# Experiment 2:
# Steps: 90, time: < 0.03 seconds
# d2 = [9, 7, 5, 6,
#       8, 1, 14, 0,
#       11, 2, 10, 3,
#       4, 12, 15, 13]


# Experiment 3: Medium level
# Steps: 98, time: < 0.05 seconds
# d3 = [0, 11, 6, 13,
#       15, 3, 7, 9,
#       12, 5, 4, 2,
#       1, 8, 10, 14]


# Experiment 4:
# Steps: 62, time: < 0.02 seconds
# d4 = [0, 1, 3, 9,
#       13, 10, 11, 7,
#       8, 14, 2, 12,
#       6, 5, 4, 15]


# Experiment 5:
# Steps: 80, time: < 0.03 seconds
# d5 = [13, 12, 8, 7,
#       2, 1, 6, 14,
#       3, 9, 10, 11,
#       5, 0, 15, 4]


# Experiment 6:
# Steps: 65 steps, time: < 0.03 seconds
# d6 = [1, 2, 14, 3,
#       9, 6, 0, 13,
#       5, 11, 12, 10,
#       15, 4, 7, 8]


# Experiment 7:
# Steps: 74 steps, time: < 0.05 seconds
# d7 = [5, 7, 0, 10,
#       11, 3, 6, 4,
#       12, 1, 9, 13,
#       8, 2, 14, 15]


# Experiment 8:
# Steps: 84 steps, time: < 0.05 seconds
# d8 = [6, 11, 14, 9,
#       3, 2, 12, 8,
#       13, 4, 1, 7,
#       5, 10, 15, 0]


# Experiment 9:
# Steps: 74, time: < 0.05 seconds
# d9 = [2, 1, 12, 13,
#       8, 4, 15, 5,
#       6, 3, 7, 11,
#       9, 14, 10, 0]


# Experiment 10:
# Steps: 95, time: < 0.04 seconds
# d10 = [6, 2, 7, 11,
#        14, 10, 15, 5,
#        12, 8, 13, 9,
#        3, 4, 0, 1]

# Experiment 11:
# Unsolvable
# d11 = [1, 2, 3, 4,
#        5, 6, 7, 8,
#        9, 10, 11, 12,
#        13, 15, 14, 0]

# Replace the data with your state that you want to solve (represented in 1-D array)
data = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 0]

# Run main
main(data)
