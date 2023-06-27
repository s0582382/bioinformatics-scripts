import java.io.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

/*
This script compares two CSV files.
The differences between input file 1 and 2 are saved in the ouput file: file 3 = "result.csv "
*/

public class compareCSV {
    
    public static void main(String args[]) throws FileNotFoundException, IOException{
        if (args.length < 2){
            System.out.println("Please provide two CSV file paths as command-line arguments.");
            return;
        }
        String file1 = args[0]; // First input file passed as an argument 
        String file2 = args[1]; // Second input file passed as an argument
        String file3 = "result.csv";
        ArrayList<String> al1 = new ArrayList<>();
        ArrayList<String> al2 = new ArrayList<>();

        BufferedReader CSVFile1 = new BufferedReader(new FileReader(file1));
        String dataRow1 = CSVFile1.readLine(); // Asuming the first row contains headers 
        String headerRow1 = dataRow1; // Store the header row 
        dataRow1 = CSVFile.readline(); // Move to the next row 
        while (dataRow1 != null ){
            al1.add(dataRow1);
            dataRow1 = CSVFile1.readLine();
        }
        CSVFile.close();

        BufferedReader CSVFile2 = new BufferedReader(new FileReader(file2));
        String dataRow2  = CSVFile2.readLine();
        while (dataRow2 != null){
            al2.add(dataRow2);
            dataRow2 = CSVFile2.readLine();
        }
        CSVFile2.close();

        int size1 = al1.size();
        int size2 = al2.size();

        try {
            FileWriter writer = new FileWriter(file3);
            write.append(headerRow1); 
            write.append("\n");

            for (int i = 1; i < size1; i++){
                String[] row1 = al1.get(i).split(",");
                String sequenceID1 = row1[0]; 

                boolean foundMatch = false;
                for(int j = 1; j < size2; j++) {
                    String [] row2 = al2.get(j).split(",");
                    String sequenceID2 = row2[0]; 

                    if(sequenceID1.equals(sequenceID2)){
                        foundMatch = true;
                        if(!al1.get(i).equals(al2.get(j))){
                            writer.append("File1: " + al1.get(i));
                            writer.append('\n');
                            writer.append("File2: " + al2.get(j));
                            writer.append('\n');
                            writer.append('\n');
                        }
                        break;
                    }
                }

                if(!foundMatch){
                    writer.append("SequenceID not found in file2: " + al1.get(i));
                    writer.append('\n';)
                }

            }
            writer.flush();
            writer.close();
        }catch (IOException){
            e.printStackTrace();
            System.out.println("Something went wrong!");
        }
    }
}
