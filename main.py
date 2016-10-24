from pathcollector import PathCollector
paths = PathCollector.collect('Bayes', r'^\d+([a-z]+)\d+.txt$')
print(paths)