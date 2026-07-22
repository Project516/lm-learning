# Day 3 - Perceptron starter file
# Build the class one method at a time as you follow the site pages.
# Test after every method - don't write it all before running!

# --- The beach data (from "5. Teach it to learn") --------------------
# Each row is [sunny, warm, go_to_beach]
beach_data = [
    [1, 1, 1],  # sunny and warm   -> go
    [1, 0, 0],  # sunny, not warm  -> no
    [0, 1, 0],  # warm, not sunny  -> no
    [0, 0, 0],  # neither          -> no
]


class Perceptron:
    """A single artificial neuron that learns yes/no from examples.

    It remembers a list of weights (one per feature, plus a bias at
    the front) and nudges them during training until its predictions
    match the labels.
    """

    def __init__(self, num_features):
        """Sets up a brand-new, untrained perceptron.

        Args:
            num_features: How many input features each example has.
                The weights list needs one extra slot for the bias.
        """
        self.weights = []
        for i in range(num_features + 1):
            self.weights.append(0.0)
        self.learning_rate = 1

    def predict(self, features):
        """Makes a yes/no decision for one example.

        Args:
            features: A list of input numbers, like [1, 0].

        Returns:
            1 if the weighted sum (bias + each weight times its
            feature) is greater than 0, otherwise 0.
        """
        total = self.weights[0]
        for i in range(len(features)):
            total += self.weights[i + 1] * features[i]
        if total > 0:
            return 1
        else:
            return 0

    def score(self, features):
        """The raw weighted sum, before the threshold (section 9).

        Args:
            features: A list of input numbers, like [1, 0].

        Returns:
            The weighted sum as a float. Large positive means a
            confident yes, large negative a confident no, and near
            0 means the example sits close to the decision line.
        """
        # TODO (section 9): same as predict, but return the total
        # itself instead of turning it into a 1 or a 0.
        total = self.weights[0]
        for i in range(len(features)):
            total += self.weights[i + 1] * features[i]
        return total

    def train(self, data, epochs):
        """Teaches the perceptron by guessing and correcting.

        Args:
            data: A 2D list of rows like [feature1, feature2, label].
            epochs: How many full passes to make over the data.

        Returns:
            Nothing. Learning happens by updating self.weights.
        """
        for e in range(epochs):
            for row in data:
                features = row[:-1]
                label = row[-1]
                prediction = self.predict(features)
                error = label - prediction

                self.weights[0] += self.learning_rate * error
                for i in range(len(features)):
                    self.weights[i + 1] += self.learning_rate * error * features[i]


def accuracy(model, data):
    """Scores a model against labeled data (this one is provided).

    Args:
        model: Anything with a predict(features) method.
        data: A 2D list of rows like [feature1, feature2, label].

    Returns:
        The fraction of rows predicted correctly, 0.0 to 1.0.
    """
    correct = 0
    for row in data:
        features = row[:-1]
        if model.predict(features) == row[-1]:
            correct = correct + 1
    return correct / len(data)


# # --- The famous failure (from "7. The famous failure: XOR") ------------
# xor_data = [
#     [0, 0, 0],   # feature1=0, feature2=0, label 0
#     [1, 0, 1],
#     [0, 1, 1],
#     [1, 1, 0]
# ]

# # Build the same data with an added third feature: feature1 * feature2
# xor_data_3 = []

# for row in xor_data:
#     f1, f2, label = row[0], row[1], row[2]
#     xor_data_3.append([row[0], row[1], row[0] * row[1], row[2]])

# print(xor_data_3)
# # [[0, 0, 0, 0], [1, 0, 0, 1], [0, 1, 0, 1], [1, 1, 1, 0]]

# p3 = Perceptron(3)
# p3.train(xor_data_3, 100)
# print("weights ", p3.weights)
# print("XOR accuracy :", accuracy(p3, xor_data_3))

# study_data = [
#     [5, 5, 0], [2, 4, 0], [0, 2, 0], [0, 6, 0], [2, 3, 0], [2, 2, 0], [3, 0, 0], [1, 0, 0],
#     [7, 8, 1], [5, 4, 1], [6, 3, 1], [3, 3, 1], [4, 5, 1], [4, 8, 1], [6, 2, 1], [8, 6, 1]
# ]

# p = Perceptron(2)

# for e in range(30):
#     p.train(study_data, 1)          # one epoch at a time
#     print("epoch", e, "accuracy", accuracy(p, study_data))


def train_pocket(model, data, epochs):
    """Trains like normal, but remembers the best weights ever seen."""
    best_weights = model.weights[:]  # a copy of the current weights
    best_acc = accuracy(model, data)
    for e in range(epochs):
        model.train(data, 1)  # run one ordinary epoch (one call to model.train)
        current = accuracy(model, data)  # this epoch's accuracy
        if current > best_acc:  # a new personal best?
            best_acc = current
            best_weights = model.weights[
                :
            ]  # HINT: pocket a COPY - the [:] matters (see below)
    model.weights = best_weights  # finish with the best, not the last
    return best_acc


# plain = Perceptron(2)
# plain.train(study_data, 100)
# print("plain, final weights:", accuracy(plain, study_data))

# pocket = Perceptron(2)
# best = train_pocket(pocket, study_data, 100)
# print("pocket, best weights: ", accuracy(pocket, study_data))

# fruit_data = [
#     [1, 1, "berry"],  [2, 1, "berry"],  [1, 2, "berry"],  [2, 2, "berry"],
#     [8, 1, "banana"], [9, 1, "banana"], [8, 2, "banana"], [9, 2, "banana"],
#     [4, 7, "lemon"],  [5, 7, "lemon"],  [4, 8, "lemon"],  [5, 8, "lemon"]
# ]

# classes = ["berry", "banana", "lemon"]


def make_binary(data, target):
    """Relabels the data 1 for the target class, 0 for everything else."""
    result = []
    for row in data:
        features = row[:-1]
        is_target = 1 if row[-1] == target else 0
        result.append(features + [is_target])
    return result


# # train one perceptron per class and keep them in a dictionary
# team = {}
# for c in classes:
#     expert = Perceptron(2)
#     expert.train(make_binary(fruit_data, c), 50)
#     team[c] = expert
#     print(c, "expert weights:", expert.weights)


def classify(features):
    best_class = classes[0]
    best_score = team[classes[0]].score(features)
    for c in classes:
        s = team[c].score(features)  # this expert's score for these features
        if s > best_score:  # more confident than the best so far?
            best_score = s
            best_class = c
    return best_class


# test_fruit = [[2, 1, "berry"], [9, 2, "banana"], [4, 8, "lemon"]]
# for row in test_fruit:
#     features = [row[0], row[1]]
#     print(row[2], "-> predicted", classify(features),
#           " scores", {c: round(team[c].score(features), 1) for c in classes})


def load_iris(filename):
    data = []
    f = open(filename)
    lines = f.readlines()
    f.close()
    for line in lines[1:]:  # lines[0] is the header, skip it
        parts = line.strip().split(",")
        sepal_length = float(parts[0])
        sepal_width = float(parts[1])
        petal_length = float(parts[2])
        petal_width = float(parts[3])
        species = parts[4]
        data.append([sepal_length, sepal_width, petal_length, petal_width, species])
    print("loaded", len(data), "flowers")
    return data


iris = load_iris("iris.csv")

# setosa_data = make_binary(iris, "setosa")
# p_setosa = Perceptron(4)                  # four features now
# p_setosa.train(setosa_data, 10)
# print("setosa accuracy:", accuracy(p_setosa, setosa_data))

# versi_data = make_binary(iris, "versicolor")

# p_plain = Perceptron(4)
# p_plain.train(versi_data, 100)
# print("versicolor, plain:", accuracy(p_plain, versi_data))

# p_pocket = Perceptron(4)
# print("versicolor, pocket:", train_pocket(p_pocket, versi_data, 100))

classes = ["setosa", "versicolor", "virginica"]

team = {}
for c in classes:
    expert = Perceptron(4)
    train_pocket(expert, make_binary(iris, c), 100)
    team[c] = expert

correct = 0
for row in iris:
    if classify(row[:-1]) == row[-1]:
        correct = correct + 1
print("team:", correct, "out of", len(iris))

# p = Perceptron(2)
# p.weights = [-2.0, 1.0, 3.0]      # the weights it learned on page 6
# for features in [[1, 1], [1, 0], [0, 1], [0, 0]]:
#     print(features, "score", p.score(features), "-> predict", p.predict(features))

# p2 = Perceptron(2)
# p2.train(xor_data, 1000)          # train it hard: 100 epochs
# print("weights:", p2.weights)
# print("accuracy:", accuracy(p2, xor_data))

# p = Perceptron(2)
# p.train(beach_data, 10)
# print(p.weights)
# print(accuracy(p, beach_data))

# ======================================================================
# TESTS - check your own work, no peeking at the solution needed.
# Un-comment each block as you finish that method and re-run the file.
# Each line prints PASS or FAIL. Aim for PASS all the way down.
# ======================================================================


def check(label, got, expected):
    """Prints PASS/FAIL for one test (provided - you don't edit this)."""
    mark = "PASS" if got == expected else "FAIL"
    extra = "" if got == expected else "   (got " + repr(got) + ")"
    print(mark, label, extra)


# After __init__:  a fresh 2-feature perceptron has three zero weights.
# p = Perceptron(2)
# print(p.weights)
# print(p.predict([1,1]))

# check("init: three zero weights", p.weights, [0.0, 0.0, 0.0])

# After predict:  set the beach weights by hand and check all four cases
# against the arithmetic you did on pages 2-3.
# p = Perceptron(2)
# print("before:", p.weights)

# p.train(beach_data, 10)
# print("after: ", p.weights)

# for row in beach_data:
#     features = row[:-1]
#     print(features, "-> predicted", p.predict(features), " correct", row[-1])


# print(accuracy(p, beach_data))
# p.weights = [-2.0, 1.0, 2.0]
# check("predict sunny + warm", p.predict([1, 1]), 1)
# check("predict sunny only",   p.predict([1, 0]), 0)
# check("predict warm only",    p.predict([0, 1]), 0)
# check("predict neither",      p.predict([0, 0]), 0)

# After score:  same weighted sum as predict, but the raw number.
# p = Perceptron(2)
# p.weights = [-2.0, 1.0, 2.0]
# check("score sunny + warm", p.score([1, 1]),  1.0)
# check("score neither",      p.score([0, 0]), -2.0)

# After train:  a trained perceptron should get the beach rule perfectly.
# (We check the behaviour, not specific weights - there is more than one
# winning set of weights, but only one right answer on every row.)
# p = Perceptron(2)
# p.train(beach_data, 10)
# check("train: perfect on beach_data", accuracy(p, beach_data), 1.0)

# XOR (page 7): the famous failure. This one is SUPPOSED to get stuck.
# p2 = Perceptron(2)
# p2.train(xor_data, 100)
# print("XOR accuracy:", accuracy(p2, xor_data), "(expected around 0.5 - one straight line cannot split XOR)")


# ======================================================================
# B-SET TESTS (the optional "Beyond the perceptron" pages)
# ----------------------------------------------------------------------
# These pages are the hardest, most optional of the week: nothing
# tomorrow or in the capstone depends on them. Each page gives you a
# skeleton with a blank or two. When you finish one, un-comment its test
# below and run. Run each test RIGHT AFTER its exercise, before the next
# page reuses a name like `weights` or `p`. (`check` is defined above.)
# ======================================================================

# --- B.1: the two-layer network gets all four XOR cases right ---------
# check("B.1 XOR network",
#       [network([0,0]), network([1,0]), network([0,1]), network([1,1])],
#       [0, 1, 1, 0])

# --- B.2: the sigmoid neuron's beach probabilities (needs `weights`,
#          `sigmoid` from the B.2 page) ---------------------------------
# check("B.2 sunny+warm is a confident yes",
#       sigmoid(weights[0] + weights[1] + weights[2]) > 0.9, True)
# check("B.2 neither is a confident no",
#       sigmoid(weights[0]) < 0.1, True)

# --- B.3: the regressor recovers the hidden rule 2*x1 + 1*x2 + 3 -------
# check("B.3 learned weights ~ [3, 2, 1]",
#       [round(w) for w in weights], [3, 2, 1])

# --- B.4: the adversarial nudge flips the beach prediction (needs `p`) -
# check("B.4 nudging warm by 0.5 flips [1,1] to 'no'",
#       p.predict([1, 0.5]), 0)

# --- B.5: the trained boundary separates every point (needs `p`,
#          `line_data` from the B.5 page) --------------------------------
# check("B.5 boundary reaches full accuracy",
#       sum(1 for r in line_data if p.predict(r[:2]) == r[2]) / len(line_data), 1.0)
