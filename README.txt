Download the repository in your system as the zipped folder DNA-Random-Access-Encoder-main.zip and unzip it. 
The folder DNA-Random-Access-Encoder-main contains this README file, two Python files : DNA-Random-Access-Encoder.py and main.py, and two folders : puspabeethis_files and Output_files.

The file DNA-Random-Access-Encoder.py contains the program for encoding multiple files of a folder into synthetic DNA molecules, such that random access of each individual file in the folder can be carried out during PCR process.
This file is imported in the main.py file as a python module and the desired DNA-encoded data is obtained in the Output_files folder by running this main.py file.

The program facilitates encoding binary data of a maximum total size of 28,501,824 bits (this includes all the desired files that are intended to be stored) into short-length synthetic DNA molecules of length upto 239 nt.
The designed oligos have length equal or close to the desired oligo length specified by user, and make use of P primer pairs, where P is the total number of files that are to be encoded. A unique primer pair is used with each file.
An oligo is of the form FORWARD PRIMER + ADDRESS BLOCK + PAYLOAD + (reverse complement of) REVERSE PRIMER.
User data must not exceed 200 files, and can be encoded into a maximum of 93756 oligos in total, with maximum length 239 nt.

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




