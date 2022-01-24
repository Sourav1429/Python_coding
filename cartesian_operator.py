from numpy.random import choice
from collections import Counter
from random import choice
import numpy as np
def cartesian_choice(*iterables):
    print(iterables)
    res=[]
    for i in iterables:
        print(i)
        res.append(choice(i))
    return res
print(cartesian_choice(['RED','ORANGE','PINK'],['John','Jack','Sam','Billings']))

