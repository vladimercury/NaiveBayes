package lib.python.collections;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class DefaultDict<T>{
    private Map<T, Integer> data;
    private int defaultValue;

    public DefaultDict(int defaultValue){
        this.data = new HashMap<>();
        this.defaultValue = defaultValue;
    }

    public int get(T key){
        Integer result = data.get(key);
        if (result == null){
            return defaultValue;
        } else {
            return result;
        }
    }

    public void put(T key, int value){
        data.put(key, value);
    }

    public void append(T key, int value){
        Integer result = data.get(key);
        if (result == null){
            data.put(key, value);
        } else {
            data.put(key, value + result);
        }
    }

    public void increment(T key){
        Integer result = data.get(key);
        if (result == null){
            data.put(key, 0);
        } else {
            data.put(key, ++result);
        }
    }

    public Set<T> keys(){
        return this.data.keySet();
    }

    public int size(){
        return this.data.size();
    }
}
