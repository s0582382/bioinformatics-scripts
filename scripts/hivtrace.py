import sys
import os
import shutil
import subprocess

# This script follows the approaches of the paper "HIV-TRACE-(TRAnsmission Cluster Engine): a Tool for Large Scale Molecular Epidemiology of HIV-1 and Other Rapidly Evolving Pathogens "
# https://academic.oup.com/mbe/article/35/7/1812/4833215

def append_fasta(source_path, destination_path):
    # Open the source and destination files in append mode
    with open(source_path, 'r') as source_file, open(destination_path, 'a') as destination_file:
        # Read the content of the source file
        source_content = source_file.read()
        
        # Append the source content to the destination file
        destination_file.write(source_content)
    
    print(f"Appended {source_path} to {destination_path}")

def run_hivtrace(fasta_path):
    # Define the Hivtrace command
    hivtrace_cmd = f"hivtrace -I {fasta_path} -a resolve -r HXB2_prrt -t .015 -m 500 -g .05"
    
    # Run the Hivtrace command using subprocess
    try:
        subprocess.run(hivtrace_cmd, shell=True, check=True)
        print("Hivtrace command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing Hivtrace command: {e}")

def run_hivnetworkcsv(csv_input, csv_output):
    # Define the Hivnetworkcsv command
    hivnetworkcsv_cmd = f"hivnetworkcsv -i {csv_input} -c {csv_output}"
    
    # Run the Hivnetworkcsv command using subprocess
    try:
        subprocess.run(hivnetworkcsv_cmd, shell=True, check=True)
        print("Hivnetworkcsv command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing Hivnetworkcsv command: {e}")

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_folder> <destination_file>")
        return
    
    # Retrieve the source folder path and destination file path from command-line arguments
    source_folder = sys.argv[1]
    destination_file = sys.argv[2]
    
    # Get the list of files in the source folder
    files = os.listdir(source_folder)
    
    # Iterate over the files in the source folder
    for file in files:
        # Get the file path
        source_file = os.path.join(source_folder, file)
        
        # Append the content of the FASTA file to the destination file
        append_fasta(source_file, destination_file)
        
    # Run the Hivtrace command to generate the CSV file
    run_hivtrace(destination_file)
        
    # Define the input and output paths for Hivnetworkcsv
    csv_input = destination_file + ".hxb2.prrt.csv"
    csv_output = "network.csv"
        
    # Run the Hivnetworkcsv command using the generated CSV file
    run_hivnetworkcsv(csv_input, csv_output)

if __name__ == "__main__":
    main()
