from collections import Counter, defaultdict
from math import log


class TfIdfCounter:
    @staticmethod
    def _compute_tf(document):
        tf = Counter(document)
        for feat in tf:
            tf[feat] /= float(len(tf))
        return tf

    @staticmethod
    def _pre_compute_idf(samples):
        docs = 0
        term_dict = defaultdict(lambda: 0)
        for fold in samples:
            for document, label in fold:
                docs += 1
                counter = Counter(document)
                for term in counter:
                    term_dict[term] += 1
        return term_dict, docs

    @staticmethod
    def compute_tf_idf(samples):
        term_dict, docs = TfIdfCounter._pre_compute_idf(samples)
        tf_idf_dict = []
        for fold in samples:
            fold_dict = []
            for doc in fold:
                doc_dict = defaultdict(lambda: 0)
                tf = TfIdfCounter._compute_tf(doc[0])
                for word in tf:
                    doc_dict[word] = tf[word] * (log(docs / term_dict[word]))
                fold_dict.append(doc_dict)
            tf_idf_dict.append(fold_dict)
        return tf_idf_dict





