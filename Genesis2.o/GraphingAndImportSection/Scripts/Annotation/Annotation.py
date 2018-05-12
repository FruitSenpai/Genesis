import os
import wx
import matplotlib.pyplot as plt
from GUIFrames import DataHolder

cid = {}
cid2 = {}
#list for drawing the lines
xVar = []
yVar = []
lines = []
isDrawingLine = False
isDrawingArrow = False
DH = DataHolder

#finds line/Arrow starting position
def onButtonDown(event):
    xVar.clear()
    yVar.clear()
    xVar.append(event.xdata)
    yVar.append(event.ydata)

#Draws line when mouse button is released
def onButtonUpLine(event):
    xVar.append(event.xdata)
    yVar.append(event.ydata)

    line = event.canvas.figure.gca().plot(xVar,yVar,c = "xkcd:black")
    event.canvas.figure.canvas.draw()
    lines.append(line)
#Draws Arrow when mouse button is released
def onButtonUpArrow(event):
    xVar.append(event.xdata)
    yVar.append(event.ydata)
    #Arrow length and dir
    dx = xVar[1]-xVar[0]
    dy = yVar[1]-yVar[0]
    #Getting the scaling factor for the arrow
    labels = event.canvas.figure.gca().get_yticklabels()
    #gets the first 2 values and determines scaling factor and then arrow size from it
    pos0 = labels[0].get_text()
    if(pos0[0] == '−'):
        pos0 = pos0[1:]
        pos0 =float(pos0)
        pos0 = -pos0
    else:
        pos0 = float(pos0)
        
    pos1 = labels[1].get_text()
    if(len(pos1)>4):
        pos1 = pos1[1:]
        pos1 =float(pos1)
        pos1 = -pos1
    else:
        pos1 = float(pos1)
        
    dist = pos1 - pos0
    arrowSize = (dist/40)
    
    #creating the arrow on the correct axes
    line = event.canvas.figure.gca().arrow(xVar[0],yVar[0],dx,dy,width=0.0001,head_width=arrowSize,head_length=arrowSize)
    event.canvas.figure.canvas.draw()
    #append the lines list so that they can be deleted
    lines.append(line)

#attaches the line drawing functions when annotate line is clicked
def Annotate(FigDic):
    AnnotateOff()
    cid.clear()
    cid2.clear()

    for key in FigDic:

        cid.update({key:( FigDic.get(key).canvas.mpl_connect('button_press_event',onButtonDown))})
        cid2.update({key:( FigDic.get(key).canvas.mpl_connect('button_release_event',onButtonUpLine))})
        

#turns off annotation 
def AnnotateOff():
    for key in DH.Figures:

        DH.Figures.get(key).canvas.mpl_disconnect(cid.get(key))
        DH.Figures.get(key).canvas.mpl_disconnect(cid2.get(key))
        

        
#attaches the arrow drawing functions when annotate arrow is clicked
def AnnotateArrow(FigDic):
    AnnotateOff()
    cid.clear()
    cid2.clear()
    for key in FigDic:

        cid.update({key:( FigDic.get(key).canvas.mpl_connect('button_press_event',onButtonDown))})
        cid2.update({key:( FigDic.get(key).canvas.mpl_connect('button_release_event',onButtonUpArrow))})

#checks annotation has been used before
def isCids():
    if(len(cid) >0 and len(cid2)>0):
        return True
    else:
        return False

        
