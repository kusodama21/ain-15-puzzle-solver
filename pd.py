# Import
from json import load
from charge_pd import re_A, re_B, re_C, to_ps


# Read from json files
pd_A = None
with open("pdA.json", "r") as f:
    pd_A = load(f)
    print("Successfully loaded " + str(len(pd_A)) + " entries for pattern A")
pd_B = None
with open("pdB.json", "r") as f:
    pd_B = load(f)
    print("Successfully loaded " + str(len(pd_B)) + " entries for pattern B")
pd_C = None
with open("pdC.json", "r") as f:
    pd_C = load(f)
    print("Successfully loaded " + str(len(pd_C)) + " entries for pattern C")


# This is the heuristic function
def pd(data):
    ps_A = to_ps(data, re_A)
    ps_B = to_ps(data, re_B)
    ps_C = to_ps(data, re_C)
    return pd_A[ps_A] + pd_B[ps_B] + pd_C[ps_C]

