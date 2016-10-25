from pathcollector import PathCollector
from messagecollector import MessageCollector
from naivebayes import NaiveBayes
from samplesbuilder import SamplesBuilder

paths = PathCollector.collect('Bayes', r'^\d+([a-z]+)\d+.txt$')
collection, classes = MessageCollector.collect(paths, log_paths=True)
samples = SamplesBuilder.build_content_samples(collection)
classifier = NaiveBayes()
# TODO: cross-validation
n = 7
[classifier.train(x) for x in samples[:n] + samples[n+1:]]
print(sum([classifier.classify(x[0]) == x[1] for x in samples[n]])/ len(samples[n]))