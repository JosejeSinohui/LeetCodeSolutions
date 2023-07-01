// Code Eval- mth to last element
// https://www.codeeval.com/open_challenges/10/

import java.io.*;

public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String[] sep = line.split(" ");
            int len = sep.length-1;
            int number = Integer.parseInt(sep[sep.length-1]);
            if (number > len){
                continue;
            }
            System.out.println(sep[len-number]);
        }
    }
}