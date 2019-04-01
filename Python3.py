
import os
count = 0

def checkfile(file, name):    
    subfiles = os.listdir(file)        
    if name in subfiles:        
        if "files.rcsb.org" not in subfiles: 
            os.chdir(file)
            print(os.getcwd())
            f = open(file+"/"+name, 'r')
            line = f.readline()
            PDBS = line.strip().split(",")
            global count
            count+=1
            print("Number of new pdb's created: ",count)
            for PDB in PDBS:            
                os.system("wget -r https://files.rcsb.org/download/"+PDB+
                          ".pdb")
                print(PDB)
            f.close()   
            print("\n Count : ",count)
         
        
    for s in subfiles:        
        if os.path.isdir(file+'/'+s):                        
            checkfile(file+'/'+s, name)    
    
    

 
path = input("Enter the path which contains Output_prosite_pattern")+"/Output_prosite_pattern"
name = "3D_structure.txt"
files = os.listdir(path)


for file in files:
    file = path+"/"+file
    if os.path.isdir(file):  
        checkfile(file, name) 
   
        
        
