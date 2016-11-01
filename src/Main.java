import classifier.NaiveBayesClassifier;
import crossvalidation.CrossValidation;
import lib.extra.Fold;
import stats.StatsCounter;
import util.MessageCollector;
import util.PathCollector;

import java.io.IOException;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        List<List<String>> paths = PathCollector.collect("Bayes/paths.txt");
        List<Fold> folds = MessageCollector.collect(paths);
        List<List<Integer>> results = CrossValidation.validate(new NaiveBayesClassifier(), folds);
        for (Double acc : StatsCounter.accuracy(folds, results)){
            System.out.println(acc);
        }
    }
}
