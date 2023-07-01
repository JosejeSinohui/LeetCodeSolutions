// CodeEval -Hidden Digits
// https://www.codeeval.com/open_challenges/122/

import java.io.*;

public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String[] split = line.split("(?!^)");
            String finished = "";
            for (int i = 0; i < split.length; i++) {
                if (split[i].matches("-?\\d+(\\.\\d+)?")) {
                    finished = finished + split[i];
                }
                switch (split[i]) {
                    case "a":
                        finished = finished + "0";
                        break;
                    case "b":
                        finished = finished + "1";
                        break;
                    case "c":
                        finished = finished + "2";
                        break;
                    case "d":
                        finished = finished + "3";
                        break;
                    case "e":
                        finished = finished + "4";
                        break;
                    case "f":
                        finished = finished + "5";
                        break;
                    case "g":
                        finished = finished + "6";
                        break;
                    case "h":
                        finished = finished + "7";
                        break;
                    case "i":
                        finished = finished + "8";
                        break;
                    case "j":
                        finished = finished + "9";
                        break;
    
                }
    
            }
            if (finished == "") {
                finished = "NONE";
            }
            System.out.println(finished);
                
         }
    }
}