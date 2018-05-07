import os
import wx
import matplotlib.pyplot as plt

cid = []
cid2 = []
#list for drawing the lines
xVar = []
yVar = []
lines = []
isDrawingLine = False
isDrawingArrow = False

def onButtonDown(event):
    xVar.clear()
    yVar.clear()
    xVar.append(event.xdata)
    yVar.append(event.ydata)

def onButtonUpLine(event):
    xVar.append(event.xdata)
    yVar.append(event.ydata)

    print(str( xVar[0])+"-->"+str( xVar[1]))
    print(str(yVar[0])+"-->"+str(yVar[1]))
    line = plt.plot(xVar,yVar)
    event.canvas.figure.canvas.draw()
    lines.append(line)

def onButtonUpArrow(event):
    xVar.append(event.xdata)
    yVar.append(event.ydata)

    dx = xVar[1]-xVar[0]
    dy = yVar[1]-yVar[0]
    
    print(str( xVar[0])+"-->"+str( xVar[1]))
    print(str(yVar[0])+"-->"+str(yVar[1]))
    line = plt.arrow(xVar[0],yVar[0],dx,dy,width=0.0001,head_width=0.001,head_length=0.002)
    event.canvas.figure.canvas.draw()
    lines.append(line)

def Annotate():
    figs = list(map(plt.figure,plt.get_fignums()))
    cid.clear()
    cid2.clear()
    
    for i in range(0, len(figs)):          
        cid.append( figs[i].canvas.mpl_connect('button_press_event',onButtonDown))
        cid2.append( figs[i].canvas.mpl_connect('button_release_event',onButtonUpLine))

def AnnotateOff():
    figs = list(map(plt.figure,plt.get_fignums()))
    
    global isDrawingLine
    isDrawingLine = False
    global isDrawingArrow
    isDrawingArrow=False
    print(str(isDrawingArrow) + " "+ str(isDrawingLine)+" /////////")
    for i in range(0, len(figs)):     
        figs[i].canvas.mpl_disconnect(cid[i])
        figs[i].canvas.mpl_disconnect(cid2[i])
        

def AnnotateArrow():
    figs = list(map(plt.figure,plt.get_fignums()))
    cid.clear()
    cid2.clear()
    for i in range(0, len(figs)):          
        cid.append( figs[i].canvas.mpl_connect('button_press_event',onButtonDown))
        cid2.append( figs[i].canvas.mpl_connect('button_release_event',onButtonUpArrow))

def isCids():
    if(len(cid) >0 and len(cid2)>0):
        return True
    else:
        return False

        
