package stats;

import lib.extra.Fold;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by kvy on 01.11.2016.
 */
public class StatsCounter {
    public static List<Double> accuracy(List<Fold> folds, List<List<Integer>> results){
        List<Double> stat = new ArrayList<>();
        for (int i = 0; i < folds.size(); i++){
            int acc_sum = 0;
            for (int j = 0; j < folds.get(i).samples.size(); j++){
                if (folds.get(i).samples.get(j).label == results.get(i).get(j)){
                    acc_sum++;
                }
            }
            stat.add(acc_sum * 1.0 / folds.get(i).samples.size());
        }
        return stat;
    }
}
