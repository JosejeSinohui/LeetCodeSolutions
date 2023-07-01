// CodeEval Longest Word
// https://www.codeeval.com/open_challenges/111/

import java.io.*;

public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            // Process line of input Here
            String[] sep = line.split(" ");
            String longest = sep[0];
            for (int i = 0; i < sep.length; i++) {
                if(longest.length()<sep[i].length()){
                    longest = sep[i];
                }
            }
            System.out.println(longest);
        }
    }
}
