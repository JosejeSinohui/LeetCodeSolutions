// Code eval Multiples of a number
// https://www.codeeval.com/open_challenges/18/

import java.io.*;

public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String[] sep = line.split(",");
            int x = Integer.parseInt(sep[0]);
            int n = Integer.parseInt(sep[1]);
            int cont = 1;
            while (true){
                if (n*cont>=x){
                    System.out.println(n*cont);
                    break;
                }
                cont++;
            }
        }
    }
}

