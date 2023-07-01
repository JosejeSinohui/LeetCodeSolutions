// Code Eval - Fibonacci Series
// https://www.codeeval.com/open_challenges/22/

import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            if (Integer.parseInt(line) == 0){
                System.out.println(0);
                continue;
            }
            int fibo = 1;
            int a = 0;
            for (int i = 0; i < Integer.parseInt(line)-1; i++) {
                fibo = fibo + a;
                a = fibo - a;
                    
            }
            System.out.println(fibo);
            
        }
    }
}
