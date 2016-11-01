package util;

import javafx.util.Pair;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by kvy on 01.11.2016.
 */
public class MessageReader {

    public static List<Integer> readSubject(String filename) throws IOException{
        BufferedReader reader = new BufferedReader(new FileReader(new File(filename)));
        try {
            return extract(reader.readLine());
        } finally {
            reader.close();
        }
    }

    public static List<Integer> readContent(String filename) throws IOException{
        BufferedReader reader = new BufferedReader(new FileReader(new File(filename)));
        try {
            String contentString = reader.readLine();
            while ((contentString = reader.readLine()).compareTo("") != 0){}
            return extract(contentString);
        } finally {
            reader.close();
        }
    }

    public static List<Integer> readUnion(String filename, int subject_multiplier) throws IOException{
        BufferedReader reader = new BufferedReader(new FileReader(new File(filename)));
        try {
            StringBuilder builder = new StringBuilder();
            String res = reader.readLine();
            builder.append(res);
            for (int i = 1; i < subject_multiplier; i++){
                builder.append(" ");
                builder.append(res);
            }
            while ((res = reader.readLine()).compareTo("") != 0){}
            builder.append(" ");
            builder.append(res);
            return extract(builder.toString());
        } finally {
            reader.close();
        }
    }

    public static List<Integer> read(String filename) throws IOException{
        return readContent(filename);
    }

    private static List<Integer> extract(String string){
        String[] words = string.split(" ");
        List<Integer> result = new ArrayList<>();
        for (String word : words){
            try {
                result.add(Integer.parseInt(word));
            } catch (NumberFormatException exc){

            }
        }
        return result;
    }
}
