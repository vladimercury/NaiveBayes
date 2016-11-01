package util;

import lib.extra.Fold;
import lib.extra.Sample;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by kvy on 01.11.2016.
 */
public class MessageCollector {
    public static List<Fold> collect(List<List<String>> paths) throws IOException{
        List<Fold> folds = new ArrayList<>();
        for (List<String> folder : paths){
            Fold fold = new Fold(new ArrayList<Sample>());
            for (String file : folder){
                int cls = 0;
                if (file.contains("legit")){
                    cls = 1;
                }
                fold.samples.add(new Sample(MessageReader.read(file), cls));
            }
            folds.add(fold);
        }
        return folds;
    }
}
