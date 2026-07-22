# Day 3 - Perceptron starter file
# Build the class one method at a time as you follow the site pages.
# Test after every method - don't write it all before running!

# --- The beach data (from "5. Teach it to learn") --------------------
# Each row is [sunny, warm, go_to_beach]
beach_data = [
    [1, 1, 1],   # sunny and warm   -> go
    [1, 0, 0],   # sunny, not warm  -> no
    [0, 1, 0],   # warm, not sunny  -> no
    [0, 0, 0]    # neither          -> no
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
        pass

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
                features = [row[0], row[1]]
                label = row[2]
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

# --- The famous failure (from "7. The famous failure: XOR") ------------
xor_data = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
]


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
p = Perceptron(2)
print("before:", p.weights)

p.train(beach_data, 10)
print("after: ", p.weights)

for row in beach_data:
    features = row[:-1]
    print(features, "-> predicted", p.predict(features), " correct", row[-1])


print(accuracy(p, beach_data))
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
