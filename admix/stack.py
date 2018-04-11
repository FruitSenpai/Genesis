import numpy as np
import matplotlib.pyplot as plt


fileName = "small.Q.2"
#numIndex = fileName.rfind('.') + 1

#qNum = int(fileName[numIndex:])
#print("The Q of the file is ", qNum)


qFile = open(fileName, "r")

individualList = [] #empty list of individuals

#read in each individual from the input file
for line in qFile:
	individualList.append(np.fromstring(line, dtype= float, sep="  "))

qFile.close()

#scale all ancestry values for individuals so that the sum of ancestry points equals 1.0 (100%)
for i in range(len(individualList)):
	sum = 0
	for j in range(len(individualList[i])):
		sum += individualList[i][j]
	#print(i+1, ": ", sum)
	
	scalingFactor = 1.0 / sum #scaling factor to apply for the individual's ancestry points

	for j in range(len(individualList[i])):
		individualList[i][j] *= scalingFactor
#end scaling portion


individuals_x = np.arange(len(individualList))
individuals_y = np.column_stack(individualList) #stack each individual's ancestry data as a single column

#plot on the stack plot
fig, ax = plt.subplots()
ax.stackplot(individuals_x, individuals_y)
plt.show()
