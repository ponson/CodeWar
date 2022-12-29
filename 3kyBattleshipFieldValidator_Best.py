import numpy as np
from scipy.ndimage import label, find_objects
battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def test(field):
    field = np.array(field)
    label_array, num = label(field, np.ones((3, 3)))
    # print(f"number of labels is: {num}")
    # print(f"array of labels is: {label_array}")

    # return sorted(ship.size for ship in [field[pos] for pos in find_objects(label_array)]) 
    
    for ship in (field[pos] for pos in find_objects(label(field, np.ones((3, 3)))[0])):
        print(ship.shape)

def validate_battlefield(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field, np.ones((3, 3)))[0]))
    )
    # == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


print(test(battleField))
#print(validate_battlefield(battleField))
