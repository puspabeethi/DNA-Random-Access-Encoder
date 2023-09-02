Download the repository in your system as the zipped folder DNA-Random-Access-Encoder-main.zip and unzip it. 
The folder DNA-Random-Access-Encoder-main contains this README file, two Python files : DNA-Random-Access-Encoder.py and main.py, and two folders : puspabeethis_files and Output_files.

The file DNA-Random-Access-Encoder.py contains the program for encoding multiple files of a folder into synthetic DNA molecules, such that random access of each individual file in the folder can be carried out during PCR process.
This file is imported in the main.py file as a python module and the desired DNA-encoded data is obtained in the Output_files folder by running this main.py file.

The program facilitates encoding binary data of a maximum total size of 28,501,824 bits (this includes all the desired files that are intended to be stored) into short-length synthetic DNA molecules of length upto 239 nt.
The designed oligos have length equal or close to the desired oligo length specified by user, and make use of P primer pairs, where P is the total number of files that are to be encoded. A unique primer pair is used with each file.
An oligo is of the form FORWARD PRIMER + ADDRESS BLOCK + PAYLOAD + (reverse complement of) REVERSE PRIMER.
User data must not exceed 200 files, and can be encoded into a maximum of 93756 oligos in total, with maximum oligo length 239 nt.

The main.py file takes the following two arguments, that are fed into the encoder function of DNA-Random-Access-Encoder module.
1) argument 1: the desired length of each oligo.
(This length should be atleast 60).
2) argument 2: the path of the folder containing the .txt files that the user intends to encode into DNA molecules.
(User needs to create a subfolder in DNA-Random-Access-Encoder-main folder and store the desired binary text files in this subfolder. Each file that is to be encoded should be a binary text file, with the binary data stored as a single string in the first line. The data size of a text file is b bits, where b is the Column no. of the last bit in Line 1 of the text file).
User needs to enter these two arguments of DNA-Random-Access-Encoder.encoder function in line 6 of main.py file.

The folder puspabeethis_files contains the necessary files required for the operation of the Python module.

The folder Output_files contains a blank fasta file named DNA_encoded_file1_data. 
After execution of the program, the output files are stored in this folder. 
These output files comprise four excel documents: AddressBook, CodeBook, ForwardPrimers, ReversePrimers, and the finally obtained P fasta files that contain the DNA-encoded data of the P input files. These fasta files are named DNA_encoded_file1_data.fasta through DNA_encoded_fileP_data.fasta
The fasta files now contain all the oligo sequences that collectively store the user data.

The four excel documents in the Output_files folder are necessary for decoding the .fasta files, that were encoded using DNA-Random-Access-Encoder module.
1) AddressBook contains the ordered address sequences of the oligos. The first M1 sequences in this document are used as address blocks of the oligos in file1, in respective orders. The next M2 sequences are used as address blocks of the oligos in file2, maintaining the order of sequences, and so on...Here M1, M2,.... are used to refer to the number of oligos containing the data in file1, file2,...., respectively. (Note that the P fasta file are named DNA_encoded_file1_data.fasta through DNA_encoded_fileP_data.fasta).
2) A message 'm' is encoded into the codeword in the '(m+2)'th row of CodeBook.xlsx, where m ranges from 0 to 65535.
(The sequences from row number 65538 of CodeBook.xlsx are used as fillers to achieve the fixed payload length in the last oligo of each of the P files, when the remaining messages for the last oligo fall short of achieving the determined payload length after concatenation).
3) ForwardPrimers.xlsx comprises P forward primer sequences, where the sequence in the 'p'th row of the excel sheet corresponds to the forward primer of the '(p-1)'th primer pair in our designed Primer_Pair_List of 200 primer pairs. Similarly, ReversePrimers.xlsx comprises P reverse primer sequences, and the sequence in the 'p'th row of this excel sheet corresponds to the reverse primer of the '(p-1)'th primer pair of Primer_Pair_List, out of which P are required for encoding given user data.







