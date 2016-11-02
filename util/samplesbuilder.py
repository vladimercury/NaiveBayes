class SamplesBuilder:
    @staticmethod
    def build_subject_samples(collection):
        return [[(y[0], y[2]) for y in x] for x in collection]

    @staticmethod
    def build_content_samples(collection):
        return [[(y[1], y[2]) for y in x] for x in collection]

    @staticmethod
    def build_union_samples(collection, subject_mpl=1):
        return [[(y[0] * subject_mpl + y[1], y[2]) for y in x] for x in collection]
