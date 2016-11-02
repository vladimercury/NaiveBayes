from classifier.naivebayesclassifier import NaiveBayesClassifier
from crossvalidation.crossvalidation import CrossValidation
from stats.statscounter import StatsCounter
from tfidf.tfidfcounter import TfIdfCounter
from util.messagecollector import MessageCollector
from util.pathcollector import PathCollector
from util.samplesbuilder import SamplesBuilder
from numpy import arange
import pprint

paths = PathCollector.collect('Bayes', r'^\d+([a-z]+)\d+.txt$')
collection, classes = MessageCollector.collect(paths, log_paths=True)
samples = SamplesBuilder.build_union_samples(collection)
#dictionary = TfIdfCounter.compute_tf_idf(samples)
results = CrossValidation.validate(NaiveBayesClassifier, samples, log_folds=True)
pprint.pprint(StatsCounter.accuracy(samples, results))