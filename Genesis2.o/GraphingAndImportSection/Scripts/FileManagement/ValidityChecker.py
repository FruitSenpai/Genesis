import os

##Checks if its a valid PCA evec graph
def CheckPcaValid(fileName):
    namelist = fileName.split('.')
    valid= False
    for i in range(0,len(namelist)):
        if(namelist[i] == 'pca'):
            valid = True
    #ext = fileName.find(".pca.evec")
    if(valid == False):
       print('Invalid PCA')
       return False
    else:
        print('Valid PCA')
        return True
       

##Checks if its a valid phen graph
def CheckPhenValid(fileName):
    namelist = fileName.split('.')
    valid= False
    for i in range(0,len(namelist)):
        if(namelist[i] == 'phe'):
            valid = True
    #ext = fileName.find(".phe")
    if(valid == False):
       print('Invalid Phen')
       return False
    else:
        print('Valid Phen')
        return True

##Checks if its a valid fam graph
def CheckFamValid(fileName):
    namelist = fileName.split('.')
    valid= False
    for i in range(0,len(namelist)):
        if(namelist[i] == 'fam'):
            valid = True
    #ext = fileName.find(".fam")
    if(valid == False):
       print('Invalid Fam')
       return False
    else:
        print('Valid Fam')
        return True

##Checks if its a valid admix evec graph
def CheckAdmixValid(fileName):
    namelist = fileName.split('.')
    valid= False
    for i in range(0,len(namelist)):
        if(namelist[i] == 'Q'):
            valid = True
    #ext = fileName.find(".Q.")
    if(valid == False):
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
