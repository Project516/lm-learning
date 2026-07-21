# Day 2 - K-Nearest Neighbors starter file
# You and your partner will fill in the TODOs as you work through
# the site pages. Run this file often - test each piece before
# building the next one!

import math

# --- The training data (from "3. The data") -------------------------
# Each row is [petal_length, petal_width, species]
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

# print(training[2][2])
# for i in range(len(training)):
#     print(training[i][2])


# --- Task 4: write the distance function -----------------------------
def distance(row_a, row_b):
    """Measures how far apart two flowers are, using their features.

    Args:
        row_a: A flower row like [petal_length, petal_width, species].
        row_b: Another row in the same format (a query with no species
            label at the end works too - only index 0 and 1 are used).

    Returns:
        The straight-line distance between the two flowers' features,
        as a float. Small means similar; 0.0 means identical features.
    """
    total = 0
    for i in range(2):
        diff = row_a[i] - row_b[i]
        total += diff**2
    return math.sqrt(total)


# --- Task 5: nearest neighbor (K = 1) ---------------------------------
def nearest_label(training, query):
    """Predicts a species by copying the single closest training flower.

    Args:
        training: The 2D list of flower rows [length, width, species].
        query: The mystery flower's features, like [1.5, 0.2] (no label).

    Returns:
        The species string of the training flower closest to the query.
    """
    best_label = training[0][2]  # assume first flower is closest for now
    best_dist = distance(training[0], query)  # its distance to the mystery flower

    for row in training:
        d = distance(row, query)  # HINT: this row's distance to the query
        if d < best_dist:  # HINT: closer than the best so far? (smaller wins)
            best_dist = d  # yes: remember its distance
            best_label = row[2]  # and remember this row's species
            # print("new closest:", row[2], "at distance", round(d, 3))

    return best_label


# mystery = [4.2, 1.3]                # a short, narrow petal, looks setosa-ish
# print("prediction:", nearest_label(training, mystery))


# --- Task 6: K nearest neighbors with voting --------------------------
def knn_predict(training, query, k):
    """Predicts a species by letting the K nearest flowers vote.

    Args:
        training: The 2D list of flower rows [length, width, species].
        query: The mystery flower's features (no label).
        k: How many nearest neighbors get a vote.

    Returns:
        The species string that wins the vote.
    """
    scored = []
    for row in training:
        d = distance(row, query)
        scored.append([d, row[2]])  # pair up the distance with this row's label

    scored.sort()

    # print(scored)                             # HINT: sort scored so the closest come first

    nearest_labels = []
    for i in range(k):
        nearest_labels.append(
            scored[i][1]
        )  # HINT: the label from the i-th closest pair

    best_label = nearest_labels[0]
    best_count = 0
    for label in nearest_labels:
        c = nearest_labels.count(
            label
        )  # HINT: count this label's votes among the neighbors
        if c > best_count:
            best_count = c
            best_label = label
    return best_label


# print("K=1:", knn_predict(training, [5.0, 1.7], 1))
# print("K=3:", knn_predict(training, [5.0, 1.7], 3))
# print("K=5:", knn_predict(training, [5.0, 1.7], 5))


# --- Task 7: measure accuracy ------------------------------------------
test = [
    [1.5, 0.2, "setosa"],
    [1.6, 0.3, "setosa"],
    [4.2, 1.3, "versicolor"],
    [4.4, 1.4, "versicolor"],
    [6.1, 2.3, "virginica"],
    [5.7, 2.0, "virginica"],
]


def accuracy(training, test, k):
    """Measures the fraction of test flowers predicted correctly.

    Args:
        training: The rows the model is allowed to learn from.
        test: Labeled rows the model has never seen.
        k: How many neighbors vote in each prediction.

    Returns:
        The fraction correct, between 0.0 and 1.0.
    """
    correct = 0
    for row in test:
        prediction = knn_predict(
            training, row, k
        )  # HINT: knn_predict's guess for this row's features
        if prediction == row[2]:  # HINT: did the guess match the true label, row[2]?
            correct = correct + 1
    return correct / len(test)  # HINT: the fraction that were right


# print("accuracy at K=3:", accuracy(training, test, 5))
print("nonsense flower:", knn_predict(training, [10.0, 5.0], 3))

# ======================================================================
# TESTS - check your own work, no peeking at the solution needed.
# Un-comment each block as you finish that function and re-run the file.
# Each line prints PASS or FAIL. Aim for PASS all the way down.
# ======================================================================


def check(label, got, expected):
    """Prints PASS/FAIL for one test (provided - you don't edit this)."""
    mark = "PASS" if got == expected else "FAIL"
    extra = "" if got == expected else "   (got " + repr(got) + ")"
    print(mark, label, extra)


def close_enough(got, target):
    """True when a float answer is within a hair of the target."""
    return got is not None and abs(got - target) < 0.01


# After distance:  two setosas are close, setosa vs virginica is far.
# check("distance: two setosas ~0.1",
#       close_enough(distance(training[0], training[1]), 0.1), True)
# check("distance: setosa vs virginica ~5.1",
#       close_enough(distance(training[0], training[10]), 5.14), True)

# After nearest_label:  a clear setosa query should come back setosa.
# check("nearest_label: obvious setosa", nearest_label(training, [1.5, 0.2]), "setosa")

# After knn_predict:  the borderline flower [5.0, 1.7] can flip with k.
# Don't hard-code an answer here - just watch it run, then discuss with
# your partner WHY the vote can change as k grows.
# print("k=1:", knn_predict(training, [5.0, 1.7], 1))
# print("k=3:", knn_predict(training, [5.0, 1.7], 3))
# print("k=5:", knn_predict(training, [5.0, 1.7], 5))

# After accuracy:  the model should get most of the held-out test set.
# check("accuracy: strong on test set (>= 0.8)",
#       accuracy(training, test, 3) >= 0.8, True)


# --- Section 9: the real iris dataset --------------------------------
# Download iris.csv into this same folder (sidebar button on the site).
#
# READING FROM A FILE is brand new today - Day 1 never covered it - so
# this function is already written for you. Read it with your partner
# before you run it. The whole trick is four tools:
#   open(filename)  opens the file
#   .readlines()    gives a list of its lines (as strings)
#   .strip()        trims the invisible newline off the end of a line
#   .split(",")     chops a line into a list at every comma
# And one catch: everything from a file is TEXT, so float() must turn
# "5.1" into the number 5.1 before you can do math with it.


def load_iris(filename):
    """Reads the iris CSV into a 2D list of flowers.

    Args:
        filename: Path to iris.csv (keep it next to this file).

    Returns:
        A list of rows, each
        [sepal_length, sepal_width, petal_length, petal_width, species].
    """
    data = []

    f = open(filename)  # open the file...
    lines = f.readlines()  # ...grab every line...
    f.close()  # ...and close it politely

    for line in lines[1:]:  # lines[0] is the header, skip it
        parts = line.strip().split(",")

        sepal_length = float(parts[0])  # file text -> numbers
        sepal_width = float(parts[1])
        petal_length = float(parts[2])
        petal_width = float(parts[3])
        species = parts[4]

        data.append([sepal_length, sepal_width, petal_length, petal_width, species])

    print("loaded", len(data), "flowers")
    return data


# Un-comment once iris.csv sits in this folder (section 9):
iris = load_iris("iris.csv")  # -> loaded 150 flowers

# On the section 9 page you will then add, right here:
#   distance_n / knn_n / accuracy_n   (your three functions, upgraded to
#                                      take the feature count as an input)
#   split_data(data, fraction, seed)  -> train: 120  test: 30
# Expected: accuracy_n(iris_train, iris_test, 5, 4) is about 0.9667.


def distance_n(row_a, row_b, num_features):
    """Like distance, but for rows with any number of features.

    Args:
        row_a: A row whose first num_features items are numbers.
        row_b: Another row in the same format.
        num_features: How many leading columns are features.

    Returns:
        The straight-line distance across those features.
    """
    total = 0
    for i in range(num_features):  # HINT: not 2 any more, the feature count passed in
        diff = diff = row_a[i] - row_b[i]
        total += diff**2
    return math.sqrt(
        total
    )  # HINT: feature i of row_a minus feature i of row_b (section 4)
    # HINT: the square root of the total


def knn_n(training, query, k, num_features):
    """Like knn_predict, but for rows with any number of features.

    Args:
        training: Rows of num_features numbers followed by a label.
        query: The mystery row's features.
        k: How many nearest neighbors get a vote.
        num_features: How many leading columns are features.

    Returns:
        The label that wins the vote (labels live at row[num_features]).
    """
    scored = []
    for row in training:
        scored.append(
            [distance_n(row, query, num_features), row[num_features]]
        )  # HINT: the label. It sat at row[2] before; where is it now?
    scored.sort()
    nearest = []
    for i in range(k):
        nearest.append(
            scored[i][1]
        )  # HINT: the label of the i-th closest pair (section 6)
    best_label = nearest[0]
    best_count = 0
    for label in nearest:
        c = nearest.count(
            num_features
        )  # HINT: how many votes this label has, with .count()
        if c > best_count:
            best_count = c
            best_label = label
    return best_label


def accuracy_n(training, test, k, num_features):
    """Like accuracy, but for rows with any number of features.

    Args:
        training: The rows the model is allowed to learn from.
        test: Labeled rows the model has never seen.
        k: How many neighbors vote in each prediction.
        num_features: How many leading columns are features.

    Returns:
        The fraction correct, between 0.0 and 1.0.
    """
    correct = 0
    for row in test:
        if (
            knn_n(training, row, k, num_features) == row[num_features]
        ):  # HINT: the flower's true label (same index idea as in knn_n)
            correct = correct + 1
    return correct / len(test)  # HINT: the fraction correct


import random


def split_data(data, fraction, seed):
    """Shuffles a dataset, then splits it into (training, test).

    Args:
        data: The full list of labeled rows.
        fraction: The share that goes to training, like 0.8 for 80 percent.
        seed: Any number; the same seed always gives the same shuffle.

    Returns:
        Two lists: the training rows, then the test rows.
    """
    shuffled = data[:]  # a copy, so we don't wreck the original
    random.seed(seed)  # same seed = same shuffle, every run
    random.shuffle(shuffled)
    cut = int(len(shuffled) * fraction)
    return shuffled[:cut], shuffled[cut:]


iris_train, iris_test = split_data(iris, 0.8, 42)
print("train:", len(iris_train), " test:", len(iris_test))  # train: 120  test: 30
print("iris accuracy, K=5:", accuracy_n(iris_train, iris_test, 5, 4))
# --- Section 10: when the data is biased ------------------------------
# No new functions needed - section 10 reuses knn_predict and accuracy
# on a deliberately skewed version of the fifteen-flower table.

# The fair dataset: 5 of each species.
fair_training = training

# The skewed dataset: setosa and virginica untouched, versicolor almost erased.
skewed_training = [
    [1.4, 0.2, "setosa"],
    [1.3, 0.2, "setosa"],
    [1.5, 0.2, "setosa"],
    [1.7, 0.4, "setosa"],
    [1.4, 0.3, "setosa"],
    [6.0, 2.5, "virginica"],
    [5.8, 1.8, "virginica"],
    [6.3, 1.8, "virginica"],
    [5.5, 2.1, "virginica"],
    [5.1, 1.9, "virginica"],
    [4.5, 1.5, "versicolor"]      # the only versicolor left
]


# ======================================================================
# OPTIONAL: fast-finisher function stubs (the A ladder + B set)
# ----------------------------------------------------------------------
# The optional pages ask you to WRITE these functions yourself, from the
# definitions on the page, with no fill-in-the-blank skeleton. The
# signatures are here so you know exactly what to build. Delete the
# `pass`, write the body, and only fill in the ones for pages you reach.
# (Some need data or helpers you set up on that page, e.g. `reg`,
# `ratings`, `iris`, `distance_n` - add those from the page first.)
# ======================================================================


# --- A.5, Part 3: precision and recall --------------------------------
def precision_recall(pairs, species):
    """Precision and recall for one species, from [true, predicted] pairs.

    Returns (precision, recall). Count true positives, false positives,
    and false negatives for `species`, then form the two ratios. Guard
    the denominators so a species that never appears gives 0.0.
    """
    pass


# --- B.1: KNN regression ----------------------------------------------
def knn_regress(training, query, k, num_features):
    """Predict a number: knn_n, but AVERAGE the k nearest neighbors'
    numbers (at row[num_features]) instead of voting on labels."""
    pass


def mean_error(training, test, k, num_features):
    """Mean absolute error: average size of the miss over the test set."""
    pass


# --- B.2: draw the decision map ---------------------------------------
def draw_map(training, k):
    """Sweep a grid of the petal space and print KNN's answer per cell.
    Petal width high->low (rows), petal length low->high (cols)."""
    pass


# --- B.3: anomaly detection -------------------------------------------
def strangeness(training, query, num_features):
    """Smallest distance_n from the query to any training flower
    (the 'best so far' scan, hunting a minimum)."""
    pass


# --- B.4: condensed nearest neighbors ---------------------------------
def condense(training, num_features):
    """Keep only the border flowers a 1-NN classifier needs (Hart 1968):
    sweep, add every flower the store misclassifies, until a pass adds
    nothing; return the store."""
    pass


# --- B.5: KNN recommender ---------------------------------------------
def taste_distance(a, b):
    """Distance between two people, ONLY on movies they have both rated
    (skip any position where either rating is 0)."""
    pass


def nearest_people(ratings, me_name, k):
    """The k people whose ratings are closest to me_name's."""
    pass


def recommend(ratings, me_name, k):
    """For each movie I have not seen (0), average my k nearest people's
    ratings; return the unseen movie with the highest predicted score."""
    pass


# --- B.6: KNN imputation ----------------------------------------------
def impute_mass(penguins, k):
    """Fill the one penguin whose body_mass is None by averaging the k
    nearest COMPLETE penguins, compared on the first three features."""
    pass


# print("two setosas:", distance(training[0], training[1]))
# print("setosa vs virginica:", distance(training[0], training[10]))
