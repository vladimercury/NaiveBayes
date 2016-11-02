class CrossValidation:
    @staticmethod
    def validate(classifier_class, samples, spam_delim=[0.5], log_folds=False, log_delims=False):
        indexes = [x for x in range(len(samples))]
        results = {y: [[] for x in range(len(samples))] for y in spam_delim}
        for fold in range(len(samples)):
            if log_folds:
                print('Cross-validation: fold ' + str(fold))
            classifier = classifier_class()
            [classifier.train(samples[index]) for index in indexes[:fold] + indexes[fold+1:]]
            for y in spam_delim:
                if log_delims:
                    print(y)
                for x in samples[fold]:
                    cls = classifier.classify(x[0], delim=y)
                    results[y][fold].append(cls)
        return results
