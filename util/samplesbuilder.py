class SamplesBuilder:
    @staticmethod
    def build_subject_samples(collection):
        return [[(y[0], y[2]) for y in x] for x in collection]

    @staticmethod
    def build_content_samples(collection):
        return [[(y[1], y[2]) for y in x] for x in collection]

    @staticmethod
    def build_union_samples(collection, subject_mpl=1):
        if subject_mpl == -1:
            return [[(y[0] * (len(y[1]) // len(y[0]) if len(y[0]) != 0 else 0) + y[1], y[2]) for y in x] for x in collection]
        return [[(y[0] * subject_mpl + y[1], y[2]) for y in x] for x in collection]
