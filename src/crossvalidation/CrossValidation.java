package crossvalidation;

import classifier.Classifier;
import lib.extra.Fold;
import lib.extra.Sample;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by kvy on 01.11.2016.
 */
public class CrossValidation {
    public static List<List<Integer>> validate(Classifier classifier, List<Fold> folds){
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < folds.size(); i++){
            System.out.println("FOLD " + i);
            result.add(new ArrayList<Integer>());
            classifier.refresh();
            for (int j = 0; j < folds.size(); j++){
                if (j != i){
                    classifier.train(folds.get(j).samples);
                }
            }
            for (Sample sample : folds.get(i).samples){
                result.get(i).add(classifier.classify(sample.features));
            }
        }
        return result;
    }
}
