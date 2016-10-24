class NaiveBayes:
    def __init__(self):
        from collections import defaultdict
        self.classes = defaultdict(lambda: 0)
        self.freq = defaultdict(lambda: 0)
        self.trained = False

    def train(self, samples):
        for features, label in samples:
            self.classes[label] += 1
            try:
                for feature in features:
                    self.freq[label, feature] += 1
            except TypeError:
                self.freq[label, features] += 1
        for label, feature in self.freq:
            self.freq[label, feature] /= self.classes[label]
        for c in self.classes:
            self.classes[c] /= len(samples)
        self.trained = True
        return self.classes, self.freq

    def classify(self, features):
        from math import log
        if not self.trained:
            raise RuntimeError('Classifier is not trained')
        return min(self.classes.keys(),
                   key=lambda x: -log(self.classes[x])
                   + sum(-log(self.freq.get((x, feature), 10**(-7))) for feature in features))
