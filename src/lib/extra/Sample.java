package lib.extra;

import java.util.List;

public class Sample {
    public List<Integer> features;
    public int label;

    public Sample(List<Integer> features, int label){
        this.features = features;
        this.label = label;
    }
}
