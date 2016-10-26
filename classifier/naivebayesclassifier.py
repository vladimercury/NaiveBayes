class NaiveBayesClassifier:
    def __init__(self):
        from collections import defaultdict
        self.frequency_table = defaultdict(lambda: 0)
        self.messages_in_class = defaultdict(lambda: 0)
        self.messages_total = 0
        self.words_in_class = defaultdict(lambda: 0)
        self.words = defaultdict(lambda: 0)

    def train(self, samples):
        for features, label in samples:
            self.messages_in_class[label] += 1
            self.messages_total += 1
            for feature in features:
                self.frequency_table[label, feature] += 1
                self.words_in_class[label] += 1
                self.words[feature] += 1

    def classify(self, features):
        from math import log
        return max(self.messages_in_class.keys(),
                   key=lambda x: log(self.messages_in_class[x] / self.messages_total)
                        + sum([log((self.frequency_table[x, feat] + 1)/(len(self.words) + self.words_in_class[x]))
                        for feat in features]))