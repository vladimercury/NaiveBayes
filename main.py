from classifier.naivebayesclassifier import NaiveBayesClassifier
from crossvalidation.crossvalidation import CrossValidation
from stats.statscounter import StatsCounter
from util.messagecollector import MessageCollector
from util.pathcollector import PathCollector
from util.samplesbuilder import SamplesBuilder
import pprint

paths = PathCollector.collect('Bayes', r'^\d+([a-z]+)\d+.txt$')
collection, classes = MessageCollector.collect(paths, log_paths=True)
samples = SamplesBuilder.build_content_samples(collection)
results = CrossValidation.validate(NaiveBayesClassifier, samples, log_folds=True)
pprint.pprint(StatsCounter.accuracy(samples, results))