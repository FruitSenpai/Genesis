import os
import wx
import csv
from GUIFrames.AppearenceFrame import AppearFrame as AppFrame
from GUIFrames.AdmixMain import ChildFrame as AdmixFrame
from GUIFrames.ExportFrame import ExportFrame as EXFrame
from GUIFrames.AdmixData import AdmixGraphFrame as AdmixDataFrame
from GUIFrames.PCADataFrame import PCADataFrame as PCADataFrame
from GUIFrames.PCAAppear import PCAAppearFrame as PCAAppearFrame
from GUIFrames.PCAMain import PCAFrame as PCAFrame

wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
            
        self.basicGUI()
        self.AdmixPath = AdmixPath = ''
    def basicGUI(self):

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

        self.Bind(wx.EVT_TOOL,self.AppearenceEvent,  Appearance_Options_Item)
        self.Bind(wx.EVT_TOOL,self.DataOptionsEvent,  Data_Options_Item)
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
         
    def Makebar(self):
        toolBar = self.CreateToolBar()
        #Declare all toolbar buttons
        InputAdmixButton = toolBar.AddTool(wx.ID_ANY,'Quite', wx.Bitmap('test.bmp'))
        InputPCAButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        SaveButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        OpenFilesButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        DataOptionsButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        AppearenceButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        RefreshButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        ShowHideButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        SearchIndividualButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        SearchHiddenIndividualButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        DrawLineButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        DrawArrowButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        ExportButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        CloseProjectButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        UndoButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        RedoButton = toolBar.AddTool(wx.ID_ANY,'Import', wx.Bitmap('test.bmp'))
        toolBar.Realize()
        
        #Bind functions to buttons
        self.Bind(wx.EVT_TOOL,self.AdmixEvent, InputAdmixButton)
        self.Bind(wx.EVT_TOOL,self.PCAEvent, InputPCAButton)
        self.Bind(wx.EVT_TOOL,self.SaveEvent, SaveButton)
        self.Bind(wx.EVT_TOOL,self.OpenFileEvent, OpenFilesButton)
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
    def AdmixEvent(self,e):
      #  wx.MessageBox('Inputs Admix')
        print(self.AdmixPath)
        self.child = AdmixFrame(self, title='Admix')
        self.child.Show()

    def PCAEvent(self,e):
        wx.MessageBox('Input PCA')
        self.child = PCAFrame(self, title='PCA')
        self.child.Show()

    def SaveEvent(self,e):
        wx.MessageBox('Save file')

    def OpenFileEvent(self,e):
        wx.MessageBox('Open file')
    
    def DataOptionsEvent(self,e):
        self.child = AdmixDataFrame(self, title='Graph Options')
        #self.child = PCADataFrame(self, title='Graph Options')
        self.child.Show()

    def AppearenceEvent(self,e):
        print('Pretty things')
        self.child = AppFrame(self, title='Export as')
        #self.child = PCAAppearFrame(self, title='Export as')
        self.child.Show()

    def RefreshEvent(self,e):
        wx.MessageBox('Refresh file')

    def ShowHideEvent(self,e):
        wx.MessageBox('Hide file')
    
    def SearchIndividualEvent(self,e):
        wx.MessageBox('Search Individual file')

    def SearchHiddenIndividualEvent(self,e):
        wx.MessageBox('Search Hidden Individual file')

    def DrawLineEvent(self,e):
        wx.MessageBox('Draw lin')

    def DrawArrowEvent(self,e):
        wx.MessageBox('Draw Arrow')
        
    def ExportEvent(self,e):
        #wx.MessageBox('Export file')
        print('ExportFile')
        self.child = EXFrame(self, title='Export as')
        self.child.Show()

    def QuitEvent(self,e):
        wx.MessageBox('Rekt')
        self.Destroy()

    def UndoEvent(self,e):
        wx.MessageBox('Undo')

    def RedoEvent(self,e):
        wx.MessageBox('Redo')

    def LoadEvent(self, e):
        wx.MessageBox('Load Files')

def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()

main()


