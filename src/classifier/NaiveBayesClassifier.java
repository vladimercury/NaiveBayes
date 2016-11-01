package classifier;

import javafx.util.Pair;
import lib.extra.Sample;
import lib.python.collections.DefaultDict;

import java.util.List;

public class NaiveBayesClassifier implements Classifier {
    private DefaultDict<Pair<Integer, Integer>> frequencyTable;
    private DefaultDict<Integer> messagesInClass;
    private int messagesTotal;
    private DefaultDict<Integer> wordsInClass;
    private DefaultDict<Integer> words;

    public NaiveBayesClassifier(){
        refresh();
    }

    @Override
    public void refresh(){
        this.frequencyTable = new DefaultDict<>(0);
        this.messagesInClass = new DefaultDict<>(0);
        this.messagesTotal = 0;
        this.wordsInClass = new DefaultDict<>(0);
        this.words = new DefaultDict<>(0);
    }

    @Override
    public void train(List<Sample> samples){
        for (Sample sample : samples){
            this.messagesInClass.increment(sample.label);
            this.messagesTotal++;
            for (Integer feature : sample.features){
                this.frequencyTable.increment(new Pair<>(sample.label, feature));
                this.wordsInClass.increment(sample.label);
                this.words.increment(feature);
            }
        }
    }

    private double formula(Integer label, List<Integer> features){
        double sum = 0;
        for (Integer feature : features){
            sum += Math.log((this.frequencyTable.get(new Pair<>(label, feature)) + 1)) /
                    (this.words.size() + this.wordsInClass.get(label));
        }
        return Math.log(this.messagesInClass.get(label) / this.messagesTotal) + sum;
    }

    @Override
    public int classify(List<Integer> features){
        int maxKey = 0;
        double maxVal = Double.MIN_VALUE;
        for (Integer label : this.messagesInClass.keys()){
            double value = formula(label, features);
            if (maxKey == -1 || value > maxVal) {
                maxKey = label;
                maxVal = value;
            }
        }
        return maxKey;
    }
}
