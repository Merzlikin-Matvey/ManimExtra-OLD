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


def barycentric_to_cartesian(A, B, C, coordinates) -> np.ndarray:
    A, B, C, = dot_to_array(A, B, C)
    coordinates = np.array(coordinates) / np.array([sum(coordinates)] * 3)
    x = coordinates[0] * A[0] + coordinates[1] * B[0] + coordinates[2] * C[0]
    y = coordinates[0] * A[1] + coordinates[1] * B[1] + coordinates[2] * C[1]
    return np.array([x, y, 0])


def trilinear_to_cartesian(A, B, C, coordinates) -> np.ndarray:
    A, B, C, = dot_to_array(A, B, C)
    a, b, c = distance(B, C), distance(A, C), distance(B, A)
    coordinates = np.array(coordinates) * np.array([a, b, c])
    return barycentric_to_cartesian(A, B, C, coordinates)


def get_circumradius(A, B, C) -> float:
    A, B, C = dot_to_array(A, B, C)
    a, b, c = distance(B, C), distance(A, C), distance(B, A)
    p = (a + b + c) / 2
    return (a * b * c) / (4 * np.sqrt(p * (p - a) * (p - b) * (p - c)))