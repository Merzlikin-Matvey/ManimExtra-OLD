import numpy as np


def dot_to_array(*dots) -> list:
    coordinates = []
    for dot in dots:
        if isinstance(dot, np.ndarray):
            coordinates.append(dot)
        else:
            try:
                coordinates.append(dot.get_center())
            except:
                pass
    return coordinates


def distance(A, B) -> float:
    A, B = dot_to_array(A, B)
    return np.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2)