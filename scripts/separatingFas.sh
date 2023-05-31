#!/bin/bash

fasta_file=$1

if [ $1 == "--help" ] || [ $1 == "-h" ]; then
	echo "Usage: $0 <fasta_file>"
	echo "Split a FASTA file into individual files based on sequence headers."
	echo
	echo "Arguemnts:"
	echo " <fasta_file> Path to FASTA file to be processed."
	exit 0
fi

if [[ ! -f "$fasta_file" ]]; then
	echo "Invalid FASTA file. Please provide a valid file."
	exit 1
fi

cat "$fasta_file" | awk '{
	if (substr($0, 1, 1) == ">") {
		filename = substr($0,2) ".fas"
	}
	print $0 > filename
}'
