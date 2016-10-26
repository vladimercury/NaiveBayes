class CrossValidation:
    @staticmethod
    def validate(classifier_class, samples, log_folds=False):
        results = [[]] * len(samples)
        indexes = [x for x in range(len(samples))]
        for fold in range(len(samples)):
            if log_folds:
                print('Cross-validation: fold ' + str(fold))
            classifier = classifier_class()
            [classifier.train(samples[index]) for index in indexes[:fold] + indexes[fold+1:]]
            for x in samples[fold]:
                cls = classifier.classify(x[0])
                results[fold].append(cls)
        return results
