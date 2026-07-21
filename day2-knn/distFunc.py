import math

training = [
    [1.4, 0.2, "setosa"],
    [1.3, 0.2, "setosa"],
    [1.5, 0.2, "setosa"],
    [1.7, 0.4, "setosa"],
    [1.4, 0.3, "setosa"],
    [4.5, 1.5, "versicolor"],
    [4.7, 1.4, "versicolor"],
    [4.0, 1.3, "versicolor"],
    [4.6, 1.5, "versicolor"],
    [3.9, 1.1, "versicolor"],
    [6.0, 2.5, "virginica"],
    [5.8, 1.8, "virginica"],
    [6.3, 1.8, "virginica"],
    [5.5, 2.1, "virginica"],
    [5.1, 1.9, "virginica"],
]


def distance(row_a, row_b):
    """Measures how far apart two flowers are, using their features.

    Args:
        row_a: A flower row like [petal_length, petal_width, species].
        row_b: Another row in the same format.

    Returns:
        The straight-line distance between the two flowers' features.
    """
    total = 0
    for i in range(2):  # two feature columns: index 0 and index 1
        diff = row_a[i] - row_b[i]  # HINT: the gap between the two flowers in feature i
        total += diff**2  # HINT: add diff-squared onto the running total
    return math.sqrt(
        total
    )  # the straight-line distance: sqrt of the total (outside the loop!)


print("two setosas:", distance(training[0], training[1]))
print("setosa vs virginica:", distance(training[0], training[10]))
