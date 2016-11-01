package util;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by kvy on 01.11.2016.
 */
public class PathCollector {
    public static List<List<String>> collect(String sourceFile) throws IOException{
        BufferedReader reader = new BufferedReader(new FileReader(new File(sourceFile)));
        List<List<String>> paths = new ArrayList<>();
        String line;
        while ((line = reader.readLine()) != null){
            paths.add(Arrays.asList(line.split(" ")));
        }
        return paths;
    }
}
