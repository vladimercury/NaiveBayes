from collections import defaultdict
from math import log, exp, log10


class NaiveBayesClassifier:
    def __init__(self):
        self.frequency_table = defaultdict(lambda: 0)
        self.messages_in_class = defaultdict(lambda: 0)
        self.messages_total = 0
        self.words_in_class = defaultdict(lambda: 0)
        self.words = defaultdict(lambda: 0)

    def train(self, samples):
        for msg in range(len(samples)):
            features = samples[msg][0]
            label = samples[msg][1]
            self.messages_in_class[label] += 1
            self.messages_total += 1
            for feature in features:
                self.frequency_table[label, feature] += 1
                self.words_in_class[label] += 1
                self.words[feature] += 1

    def classify(self, features, delim=0.5):
        keys = {x: log(self.messages_in_class[x] / self.messages_total)
                        + sum([log((self.frequency_table[x, feat] + 1)/(len(self.words) + self.words_in_class[x]))
                        for feat in features]) for x in self.messages_in_class.keys()}
        degree = keys[1] - keys[0]
        degree = -log(-degree) if degree < 0 else log(degree) if degree > 0 else 0
        pos = 0 if degree > 700 else 1 if degree < -700 else 1 / (1 + exp(degree))
        return 0 if pos > delim else 1

