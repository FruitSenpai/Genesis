import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import os

######################################################################################
#########Plotting of graph with respect to attained information START#################
######################################################################################

def PlotPca(NamesFirst,Groups,dictPhen):
    EvecString = os.getcwd()
    EvecString= EvecString+'\..\Data\comm-SYMCL.pca.evec'

    ##takes all x and y values that were specified (NOTE THIS IS WHERE THE COLOUMNS FOR THE EVEC FOLDER WOULD BE CHANGED)
    x, y = np.genfromtxt(EvecString,unpack=True, usecols = (1,2),skip_header=1)


    ##Checks each individual group
    ##Per group each indiviual is checked to see if it belongs to the group
    ##If this is the case then its x and y co-ords are added to the x and y lists to be plotted 

    for group in range(len(Groups)):
        xtemp =[]
        ytemp= []
        
        for i in range(len(NamesFirst)):
            if(NamesFirst[i] in dictPhen):
                if(dictPhen.get(NamesFirst[i]) == Groups[group]):
                    ##add x and y value to dictionary
                    xtemp.append(x[i])
                    ytemp.append(y[i])

    ##just a check to make sure that we dont plot groups with 0 components
        if(len(xtemp) >0):
        
            plt.scatter(xtemp, ytemp, marker='^', label=Groups[group], s=1)
            
######################################################################################
#########Plotting of graph with respect to attained information END###################
################################################################################



###############################################################################
#####################################Render Graph##############################
###############################################################################

def RenderGraph(Heading,xLabel,yLabel):
    # Plots graph
    plt.title(Heading)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
    plt.show()
