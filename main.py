from classifier.naivebayesclassifier import NaiveBayesClassifier
from crossvalidation.crossvalidation import CrossValidation
from stats.statscounter import StatsCounter
from tfidf.tfidfcounter import TfIdfCounter
from util.messagecollector import MessageCollector
from util.pathcollector import PathCollector
from util.samplesbuilder import SamplesBuilder
from numpy import arange
from pprint import pprint
import pylab as plt

paths = PathCollector.collect('Bayes', r'^\d+([a-z]+)\d+.txt$')
collection, classes = MessageCollector.collect(paths, log_paths=True)
samples = SamplesBuilder.build_union_samples(collection)
#dictionary = TfIdfCounter.compute_tf_idf(samples)
xs = []
ys = []
zs = []
results = CrossValidation.validate(NaiveBayesClassifier, samples, arange(0.5, 1.0, 0.1), True, True)
for x in sorted(results.keys()):
    xs.append(x)
    stat = StatsCounter.confusion_matrix(samples, results[x])
    print(stat)
    zs.append(stat["summary"]["ls"])
    ys.append(StatsCounter.accuracy(samples, results[x])["summary"])
plt.plot(xs, ys)
plt.figure()
plt.plot(xs, zs)
plt.show()