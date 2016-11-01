package classifier;

import lib.extra.Sample;

import java.util.List;

public interface Classifier {
    void refresh();
    void train(List<Sample> samples);
    int classify(List<Integer> features);
}
