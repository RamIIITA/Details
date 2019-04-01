# PDBDownload
#Download PDB files according to the Prosite database format
This is Python3 Script mainly designed to automate the PDB Downloads sccording to the Prosite database format

Language: Python3

libraries: OS module

Input: Input the path which contains Output_prosite_pattern ("Don't include the Output_prosite_pattern in the path")

Output: Path of the each folder where operations are carried out, Number of new PDB folder created in each folder, Total PDB ID's

Format of Prosite Database format:
(Prosite database mainly designed for classification of proteins)

Output_prosite_pattern folder -> multiple folders with ID's (Each classified protein is given an ID) as name -> Each folder may contain one or more sub folders(i.e sub classes) -> folder name protein functional site pattern -> consists of three files namely 3D_Strucuture.txt, positive_seq_id.txt, record_info.txt (Our output of the program is generated in the folder named as "files.rcsb.org" Which contains multiple PDB files) (For more infomation regrading the prosite pattern please refer the offical website of the prosite)
