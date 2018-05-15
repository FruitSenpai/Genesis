"""This is the main script for the Genesis2 program.

This script will handle multiple jobs such as handling all the UI for the main interface.
It also contains the classes needed to embed graphs into the main UI.
Finally the script also provides access to all other areas of the program through its UI."""
import os
import wx
from wx.lib.pubsub import pub
import matplotlib.pyplot as plt
from GUIFrames.AppearenceFrame import AppearFrame as AppFrame
from GUIFrames.AdmixMain import ChildFrame as AdmixFrame
from GUIFrames.ExportFrame import ExportFrame as EXFrame
from GUIFrames.AdmixData import AdmixGraphFrame as AdmixDataFrame
from GUIFrames.PCADataFrame import PCADataFrame as PCADataFrame
from GUIFrames.PCAAppear import PCAAppearFrame as PCAAppearFrame
from GUIFrames.PCAMain import PCAFrame as PCAFrame
from GUIFrames.PcaCustom.PcaCustomScript import PcaCustom as PcaCustom
from GUIFrames.AdmixCustom.AdmixCustomMainScript import AdmixMainMenu as admixMM
from GUIFrames import DataHolder
from Annotation import Annotation as An
from FileManagement.FileImporter import FileImporter
from Graph import GraphSaver
from Graph.PcaGraphing.PcaGraph import PcaGraph as PCA
from Graph.admix.AdmixGraph import AdmixGraph as Admix

import ntpath

###################Import for embedding 
import wx.lib.mixins.inspection as wit

if 'phoenix' in wx.PlatformInfo:
    import wx.lib.agw.aui as aui
    
else:
    import wx.aui as aui
    

import matplotlib as mpl
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
########################3
wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"

pcaSaveWildcard = "PCA Graph file (*.gpf)|*.gpf|" \
            "All files (*.*)|*.*"

admixSaveWildcard = "Admixture Graph file (*.gaf)|*.gaf|" \
            "All files (*.*)|*.*"

loadWildcard = "Admixture Graph file (*.gaf)|*.gaf|" \
            "PCA Graph file (*.gpf)|*.gpf|" \
            "All files (*.*)|*.*"

class windowClass(wx.Frame):
    """ Creates the main interface for the program."""
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.Size = (3000,4500)   
        self._panel =self.basicGUI()
        self.AdmixPath = AdmixPath = ''
        #find data holder
        self._DH = DataHolder
        #create a fileimporter to hold graphs
        self._FI = FileImporter()
        self.Graphs = {}
        #the main graph is listening so that it can get file importers PCA and ADMIX main
        pub.subscribe(self.mylistener, "panelListener")
        #create a list of ids
        self._cid = []
        #create a notebook to store graphs
        self.plotter = PlotNotebook(self._panel)

        currentGraphName = ""

        self.currentDirectory = os.getcwd()

        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText("Genesis2.o")


    def returnPanel(self):
        """ Returns the panel for the main UI frame. """
        return self._panel
        
    def basicGUI(self):
        """Initialises GUI for the main frame. """

        panel= wx.Panel(self)

        menuBar = wx.MenuBar()

        #Declare new buttons 
        fileButton = wx.Menu()
        graphButton = wx.Menu()
        helpButton = wx.Menu()

        #File Button options
        Save_Item = fileButton.Append(wx.ID_ANY,'Save Project','status msg...')
        Load_Item = fileButton.Append(wx.ID_ANY,'Load Project','status msg...')
        Export_Item = fileButton.Append(wx.ID_ANY,'Export image','status msg...')
        Exit_Item = fileButton.Append(wx.ID_ANY,'Exit','status msg...')

        self.Bind(wx.EVT_TOOL,self.SaveEvent, Save_Item)
        self.Bind(wx.EVT_TOOL,self.LoadEvent, Load_Item)
        self.Bind(wx.EVT_TOOL,self.ExportEvent, Export_Item)
        self.Bind(wx.EVT_TOOL,self.QuitEvent, Exit_Item)

        #Toolbars
        importItem = wx.Menu()
        Import_Admix = importItem.Append(wx.ID_ANY,'New Admixture Graph')
        Import_PCA = importItem.Append(wx.ID_ANY,'New PCA Graph')

        self.Bind(wx.EVT_TOOL,self.PCAEvent, Import_PCA)
        self.Bind(wx.EVT_TOOL,self.AdmixEvent, Import_Admix)
          
        fileButton.Append(wx.ID_ANY,'New Graph',importItem )

        self.Makebar()

        
        #Graph Button options
        Data_Options_Item = graphButton.Append(wx.ID_ANY,'Data options','status msg...')#Append new items to buttons
        Appearance_Options_Item = graphButton.Append(wx.ID_ANY,'Appearence options','status msg...')
        Delete_Annotations_Item = graphButton.Append(wx.ID_ANY,'Delete Annotations','status msg...')
        self.Bind(wx.EVT_TOOL,self.AppearenceEvent,  Appearance_Options_Item)
        self.Bind(wx.EVT_TOOL,self.DataOptionsEvent,  Data_Options_Item)
        self.Bind(wx.EVT_TOOL,self.DelAnnotationsEvent,  Delete_Annotations_Item)
        
        #Help Button options
        Help_Item = helpButton.Append(wx.ID_EXIT,'Help','status msg...')
        About_Item = helpButton.Append(wx.ID_EXIT,'About','status msg...')

        #Add buttons to menubar
        menuBar.Append(fileButton,'File')
        menuBar.Append(graphButton,'Graph')
        menuBar.Append(helpButton,'Help')
        
        self.SetMenuBar(menuBar)
        #self.Bind(wx.EVT_MENU, self.QuitEvent, exitItem)

        self.SetTitle('Genesis')
        self.Show(True)

        return panel
         
    def Makebar(self):
        """Initialises tool bar at the top of the GUI """
        toolBar = self.CreateToolBar()
        #toolBar.SetBackgroundColour((0xff,0xcc,0xcc))
        #Declare all toolbar buttons
        InputAdmixButton = toolBar.AddTool(wx.ID_ANY,'Quite', wx.Bitmap('../images/admix.bmp'))
        self.Bind(wx.EVT_ENTER_WINDOW,self.OnMouseEnter,InputAdmixButton)
        #InputAdmixButton.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseEnter)

        InputPCAButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/pca.bmp'), shortHelp='PCA')
        toolBar.AddSeparator()
        SaveButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/save.bmp'),shortHelp='Save')
        OpenFilesButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/open.bmp'),shortHelp='Open Files')
        toolBar.AddSeparator()
        DataOptionsButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/dataOp.bmp'),shortHelp='Data Options')
        AppearenceButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/appearanceOp.bmp'), shortHelp='Appearence')
        RefreshButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/refresh.bmp'),shortHelp='Refresh')
        ShowHideButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/hiddenInd.bmp'),shortHelp='Show/Hide Individual')
        SearchIndividualButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/search.bmp'),shortHelp='Search for Individual')
        SearchHiddenIndividualButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/hiddenInd.bmp'),shortHelp='Search Hidden Individual')
        toolBar.AddSeparator()
        DrawLineButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/drawLine.bmp'),shortHelp='Draw Line')
        DrawArrowButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/drawArrow.bmp'),shortHelp='Draw Arrow')
        toolBar.AddSeparator()
        ExportButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/Export.bmp'),shortHelp='Export')
        CloseProjectButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/closeProject.bmp'),shortHelp='Close Project')
        UndoButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/Undo.bmp'),shortHelp='Undo')
        RedoButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('../images/redo.bmp'),shortHelp='Redo')
        toolBar.Realize()
        
        #Bind functions to buttons
        self.Bind(wx.EVT_TOOL,self.AdmixEvent, InputAdmixButton)
        self.Bind(wx.EVT_TOOL,self.PCAEvent, InputPCAButton)
        self.Bind(wx.EVT_TOOL,self.SaveEvent, SaveButton)
        self.Bind(wx.EVT_TOOL,self.LoadEvent, OpenFilesButton)
        self.Bind(wx.EVT_TOOL,self.DataOptionsEvent, DataOptionsButton)
        self.Bind(wx.EVT_TOOL,self.AppearenceEvent, AppearenceButton)
        self.Bind(wx.EVT_TOOL,self.RefreshEvent, RefreshButton)
        self.Bind(wx.EVT_TOOL,self.ShowHideEvent, ShowHideButton)
        self.Bind(wx.EVT_TOOL,self.SearchIndividualEvent, SearchIndividualButton)
        self.Bind(wx.EVT_TOOL,self.SearchHiddenIndividualEvent, SearchHiddenIndividualButton)
        self.Bind(wx.EVT_TOOL,self.DrawLineEvent, DrawLineButton)
        self.Bind(wx.EVT_TOOL,self.DrawArrowEvent, DrawArrowButton)
        self.Bind(wx.EVT_TOOL,self. ExportEvent,  ExportButton)
        self.Bind(wx.EVT_TOOL,self.QuitEvent,  CloseProjectButton)
        self.Bind(wx.EVT_TOOL,self. UndoEvent,  UndoButton)
        self.Bind(wx.EVT_TOOL,self. RedoEvent,  RedoButton)

        

#All button and label functions

    def DelAnnotationsEvent(self,e):
        """Delete annotations from program """
        #Not currently implemented
        pass
    
    def OnMouseEnter(self,e):
        """ Shows a description of the icons function."""
        self.Statusbar.SetStatusText("TRIGGERED")
        e.Skip()
        
    def AdmixEvent(self,e):
        """Runs admix creator GUI. """
      
        self.child = AdmixFrame(self, title='Admix')
        self.child.Show()
        self.child.SetFocus()
        pub.sendMessage('GetPanelAdmix',message=self.plotter)

    def PCAEvent(self,e):
        """Runs the pca creator GUI. """
        self.child = PCAFrame(self, title='PCA')
        self.child.Show()
        pub.sendMessage('GetPanelPca',message=self.plotter)

    def SaveEvent(self,e):
        """Saves the current graph. """
        
        graph = DataHolder.Graphs[windowClass.currentGraphName]
        
        defName = ""
        #determines graph type
        if(type(graph) is Admix):
            wildcard = admixSaveWildcard
            defName = windowClass.currentGraphName + ".gaf"
        elif(type(graph) is PCA):
            wildcard = pcaSaveWildcard
            defName = windowClass.currentGraphName + ".gpf"

        dlg = wx.FileDialog(
            self, message="Select a save locations",
            defaultDir = self.currentDirectory, 
            defaultFile=defName,

            wildcard=wildcard,

            style=wx.FD_SAVE | wx.FD_CHANGE_DIR
            )
        
        if dlg.ShowModal() == wx.ID_OK:
                filePath = dlg.GetPath()
                baseName = ntpath.basename(filePath) #get base name               

                #update dictionary key for graph and figure
                
                graph.setName(baseName, windowClass.currentGraphName)
        #Set notebook as  none so it can be pickled
                graph.setNotebook(None)

                GraphSaver.saveGraph(graph, filePath)

                nb = self.plotter.getNoteBook()
                #reset notebook
                graph.setNotebook(self.plotter)
                pageIndex = nb.GetSelection()
                nb.SetPageText(pageIndex, baseName)
                windowClass.currentGraphName = baseName

        dlg.Destroy()
        
    

    def OpenFileEvent(self,e):
        """ Opens extra files GUI."""
        wx.MessageBox('Open file')
        
    
    def DataOptionsEvent(self,e):
        """Opens data options GUI"""
        self.child = AdmixDataFrame(self, title='Graph Options')
        self.child.Show()

    def AppearenceEvent(self,e):
        """Opens up the relevant customization options GUI. """
        graph = self._DH.Graphs.get(windowClass.currentGraphName)

        #Checks graph type and chooses relevant window to display
        if( isinstance( graph , PCA)):
            self.child = PcaCustom(self,windowClass.currentGraphName,self.plotter.nb.GetCurrentPage(),self.plotter.nb,self.plotter.nb.GetSelection())
            self.child.Show()
        elif(isinstance( graph , Admix)):
            self.child = admixMM(self, graph, self.plotter, self.plotter.nb)
            self.child.Show()


        
    def RefreshEvent(self,e):
        """ Opens refresh GUI."""
        wx.MessageBox('Refresh file')

    def ShowHideEvent(self,e):
        """ Opens Show hiders GUI."""
        wx.MessageBox('Hide file')
    
    def SearchIndividualEvent(self,e):
        """ Opens search individual GUI."""
        wx.MessageBox('Search Individual file')

    def SearchHiddenIndividualEvent(self,e):
        """ Opens search hidden individuals GUI."""
        wx.MessageBox('Search Hidden Individual file')

    def DrawLineEvent(self,e):
        """Turns on ability to draw a line. """
        An.Annotate(self._DH.Figures)
        
            
        
    def DrawArrowEvent(self,e):
        """ Turns on ability to draw an arrow."""
        An.AnnotateArrow(self._DH.Figures)
                  
        
    def ExportEvent(self,e):
        """Ooens export GUI. """
        wx.MessageBox('Export file')
        self.child = EXFrame(self, title='Export as')
        self.child.Show()

    def QuitEvent(self,e):
        """Exits the program."""
        wx.MessageBox('Exit')
        self.Destroy()

    def UndoEvent(self,e):
        """Will undo previous action. """
        wx.MessageBox('Undo')

    def RedoEvent(self,e):
        """Will redo previous undo action. """
        wx.MessageBox('Redo')        

    def LoadEvent(self, e):
        """ Load graph object into the scene."""                 

        #Creates a dialog to locate previous projects
        dlg = wx.FileDialog(
        self, message="Select a Genesis graph file",
        defaultDir = self.currentDirectory, 
        defaultFile="",

        wildcard=loadWildcard,

        style=wx.FD_OPEN | wx.FD_CHANGE_DIR
        )

        if dlg.ShowModal() == wx.ID_OK:
            filePath = dlg.GetPath()
            graph = GraphSaver.loadGraph(filePath)
            
            nb = self.plotter
            
            graph.setNotebook(nb)
            if type(graph) is Admix:    
                phenoCol = graph.getPhenoColumn()
                graph.plotGraph(False,phenoCol = phenoCol)
            elif type(graph) is PCA:
                graph.PlotPca(False) #False indicates this graph is not being plotted the first time

            self._DH.Graphs.update({graph.getName():graph})

    
    def mylistener(self,message, arg2 = None):
        """Gets file managers returned from graphing frames. """
        
        _temp = message.GetManagers()
        for i in range(0,len(_temp)):
            self._FI.AddFileManager(_temp[i])
        self._FI.PrintFileManagers()
                


#Most of the Plot class as well as some of the plotNotebook class have been taken from
#the matplotlib documentation. This code can be found at:
#https://matplotlib.org/gallery/user_interfaces/embedding_in_wx5_sgskip.html
class Plot(wx.Panel):
    """Creates a new page in the notebook to plot on."""
    def __init__(self, parent, id=-1, dpi=None, **kwargs):
        locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        wx.Panel.__init__(self, parent, id=id, **kwargs)
        self.figure = mpl.figure.Figure(dpi=dpi, figsize=(2, 2))
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(sizer)
        
        #configure to make the graph cover full screen
        self.figure.subplots_adjust(left=0.03,right=0.95,top=0.94, bottom = 0.1)
        

class PlotNotebook(wx.Panel):
    """ Creates a notebook to place pages in."""
    
    def __init__(self, parent, id=-1):
        #Made the notebook stretch to approximately a full screen
        wx.Panel.__init__(self, parent, id=id,size=(1900,900))	
        self.nb = aui.AuiNotebook(self, size=(2000,500))
        sizer = wx.BoxSizer()
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.currPage = None

        self.nb.Bind(aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.onTabChange)
        self.Fit()

    def add(self, name="plot"):
        """Adds a plot to the notebook. """
        
        page = Plot(self.nb)
        self.nb.AddPage(page, name)
        self.nb.SetSelection(self.nb.GetPageCount() - 1)
        return page.figure

    def onTabChange(self,event):
        """ Register when tab changes and updates what tab is currently open."""
        
        self.currPage =self.nb.GetPageText(event.GetSelection())
        windowClass.currentGraphName = self.nb.GetPageText(event.GetSelection())
        event.Skip()

    def getNoteBook(self):
        """ Returns notebook. """
        return self.nb


def main():
    app = wx.App()   
    windowClass(None)


    app.MainLoop()


        

main()


