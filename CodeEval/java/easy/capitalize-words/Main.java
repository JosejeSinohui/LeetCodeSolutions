// Code Eval - CapitalizeWords
// https://www.codeeval.com/open_challenges/93/

import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String[] palabras = line.split(" ");
            String finished = "";
            for (int i = 0; i < palabras.length; i++) {
                String[] letras = palabras[i].split("");
                for (int j = 0; j < letras.length; j++) { 
                    if(j==0){
                        finished = finished + letras[j].toUpperCase();
                        
                    }
                    else{
                        finished = finished + letras[j];
                    }
                    
                }
                finished = finished + " ";
                
            }
            System.out.println(finished);
        }
    }
    
}
