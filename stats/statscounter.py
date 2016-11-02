class StatsCounter:
    @staticmethod
    def accuracy(samples, results):
        if len(samples) != len(results):
            raise RuntimeError('Samples size not equal to results size')
        if len(samples) == 0:
            return {}, 0
        stat = [0] * len(samples)
        for fold in range(len(samples)):
            acc_sum = 0
            for i in range(len(samples[fold])):
                acc_sum += samples[fold][i][1] == results[fold][i]
            stat[fold] = acc_sum / len(samples[fold])
        return {'stats': stat, 'summary': sum(stat) / len(stat)}

    @staticmethod
    def f1(samples, results):
        if len(samples) != len(results):
            raise RuntimeError('Samples size not equal to results size')
        if len(samples) == 0:
            return {}, 0
        f1_stat = [0] * len(samples)
        recall_stat = [0] * len(samples)
        precision_stat = [0] * len(samples)
        for fold in range(len(samples)):
            tp, fp, fn, tn = 0, 0, 0, 0
            for i in range(len(samples[fold])):
                sample_0 = samples[fold][i][1] == 0
                result_0 = results[fold][i] == 0
                tp += sample_0 and result_0
                fp += sample_0 and not result_0
                fn += not sample_0 and result_0
            recall_stat[fold] = tp / (tp + fp) if tp + fp != 0 else 0
            precision_stat[fold] = tp / (tp + fn) if tp + fn != 0 else 0
            recall = recall_stat[fold]
            precision = precision_stat[fold]
            f1_stat[fold] = 2 * recall * precision / (recall + precision) if recall + precision != 0 else 0
        return {'f1': f1_stat,
                'recall': recall_stat,
                'precision': precision_stat,
                'summary': {
                    'f1': sum(f1_stat)/len(f1_stat),
                    'recall': sum(recall_stat)/len(recall_stat),
                    'precision': sum(precision_stat)/len(precision_stat)
                }}

    @staticmethod
    def confusion_matrix(samples, results):
        if len(samples) != len(results):
            raise RuntimeError('Samples size not equal to results size')
        if len(samples) == 0:
            return {}, 0
        fold_confusions = []
        fss, fsl, fls, fll = 0, 0, 0, 0
        for fold in range(len(samples)):
            ss, sl, ls, ll = 0, 0, 0, 0
            for i in range(len(samples[fold])):
                sample_0 = samples[fold][i][1] == 0
                result_0 = results[fold][i] == 0
                ss += sample_0 and result_0
                sl += sample_0 and not result_0
                ls += not sample_0 and result_0
                ll += not sample_0 and not result_0
            fss += ss
            fsl += sl
            fls += ls
            fll += ll
            fold_confusions.append({
                'ss': ss,
                'sl': sl,
                'ls': ls,
                'll': ll,
            })
        summary = {
            'ss': fss / len(samples),
            'sl': fsl / len(samples),
            'ls': fls / len(samples),
            'll': fll / len(samples),
        }
        return {
            'folds': fold_confusions,
            'summary': summary,
        }
