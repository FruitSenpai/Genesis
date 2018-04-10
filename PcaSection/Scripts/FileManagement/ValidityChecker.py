import os

##Checks if its a valid PCA evec graph
def CheckPcaValid(fileName):
    ext = fileName.find(".pca.evec")
    if(ext == -1):
       print('Invalid PCA')
       return False
    else:
        print('Valid PCA')
        return True
       

##Checks if its a valid phen graph
def CheckPhenValid(fileName):
    ext = fileName.find(".phe")
    if(ext == -1):
       print('Invalid Phen')
       return False
    else:
        print('Valid Phen')
        return True

##Checks if its a valid fam graph
def CheckFamValid(fileName):
    ext = fileName.find(".fam")
    if(ext == -1):
       print('Invalid Fam')
       return False
    else:
        print('Valid Fam')
        return True

##Checks if its a valid admix evec graph
def CheckAdmixValid(fileName):
    ext = fileName.find(".Q.")
    if(ext == -1):
       print('Invalid Admix')
       return False
    else:
        print('Valid Admix')
        return True


##Checks amount of coloumns in line
##First Parameter is which line we want to read starting at 0
##Second Paramter is which file to open
def CheckLineAmount(WhichLineToRead, phenString):
    f = open(phenString)
    
    for i in range(0,WhichLineToRead+1):
        f.readline() 

    string = f.readline()
    listString = string.split()

    return len(listString)



'''
##################MAIN
evecString = os.getcwd()
evecString= evecString+'\..\Data\comm-SYMCL.pca.evec'

phenString = os.getcwd()
phenString= phenString+'\..\Data\comm.phe'

famString = os.getcwd()
famString= famString+'\..\Data\small.fam'

AdmixString = os.getcwd()
AdmixString= AdmixString+'\..\Data\small.Q.2'


#print(CheckLineAmount(1,phenString))
CheckPcaValid(AdmixString)
CheckPhenValid(AdmixString)
CheckFamValid(AdmixString)
CheckAdmixValid(AdmixString)
'''
