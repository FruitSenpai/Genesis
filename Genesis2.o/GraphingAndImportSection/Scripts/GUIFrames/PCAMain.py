import os
import wx
from wx.lib.pubsub import pub
import csv
import sys
import matplotlib.pyplot as plt
from GUIFrames.AppearenceFrame import AppearFrame as AppFrame
from FileManagement  import ValidityChecker as VC
#print(os.getcwd())

#import FileImporter as fileImp
from FileManagement.FileImporter import FileImporter
from GUIFrames import DataHolder

wildcard =  "All files (*.*)|*.*"
class PCAFrame(wx.Dialog):
    
   
    
    def __init__(self, parent, title):
        super(PCAFrame, self).__init__(parent, title= 'Pca', 
            size=(400, 700),style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)

        #pan = wx.Panel(self,wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        self.InitUI()
        self.Centre()
        #creates File Importer for now
        self._FI = FileImporter()
        self._DH = DataHolder
        pub.subscribe(self.GetPanel, "GetPanelPca")
        
    def InitUI(self):
        
        
        panel = wx.Panel(self,wx.ID_ANY)

        self.Columns = []

        self.comboPCA1 = wx.ComboBox(panel, choices = self.Columns)
        self.comboPCA1.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.comboPCA2 = wx.ComboBox(panel, choices = self.Columns)
        self.comboPCA2.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.comboPCA3 = wx.ComboBox(panel, choices = self.Columns)
        self.comboPCA3.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.comboPhe = wx.ComboBox(panel, choices = self.Columns)
        self.comboPhe.Bind(wx.EVT_COMBOBOX, self.OnCombo)

        self.comboPCA1.Hide()
        self.comboPCA2.Hide()
        self.comboPCA3.Hide()
        self.comboPhe.Hide()

        self.ColumnLabel = wx.StaticText(panel,label = "Select PCAs")
        self.ColumnLabel.Hide()
        self.PheLabel = wx.StaticText(panel,label = "Which Column is the phenotype")
        self.PheLabel.Hide()

        self.vbox = wx.BoxSizer(wx.VERTICAL)

        fgsTop = wx.FlexGridSizer(2,2,10,10)
        fgs = wx.FlexGridSizer(8,1,10,10)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)
        fgsBotPhe = wx.FlexGridSizer(1,2,10,10)
        fgsBot = wx.FlexGridSizer(1,2,10,10)
        fgsBotRight = wx.FlexGridSizer(1,2,10,10)
        
        OpenFileBtn = wx.Button(panel,wx.ID_ANY, label ='Import Data File')
        OpenFileBtn.parameterVal = 'Data'
        OpenPheBtn = wx.Button(panel,wx.ID_ANY, label ='Import Phe File')
        OpenPheBtn.parameterVal = 'Phe'
        AcceptBtn = wx.Button(panel,wx.ID_ANY, label ='Accept')
        ExitBtn = wx.Button(panel,wx.ID_EXIT, label ='Exit')
        OpenFileBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        OpenPheBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        AcceptBtn.Bind(wx.EVT_BUTTON, self.onAcceptFile)
        ExitBtn.Bind(wx.EVT_BUTTON, self.Quit)

        NextBtn = wx.Button(panel,wx.ID_ANY, label ='Next')
        NextBtn.Bind(wx.EVT_BUTTON, self.AppearFrame)

        self.Nametc = wx.TextCtrl(panel, value="Name")
        self.tc1 = wx.TextCtrl(panel)    
        self.tc3 = wx.TextCtrl(panel)

        fgsTop.AddMany([(OpenFileBtn),
                        (self.tc1, 1, wx.EXPAND),
                        (OpenPheBtn, 1, wx.EXPAND),
                        ( self.tc3, 1, wx.EXPAND)])
                     

        fgsBotPhe.AddMany([(self.PheLabel,1,wx.EXPAND),
                         (self.comboPhe,1,wx.EXPAND)
                         ])
        fgsBot.AddMany([(NextBtn),
                        (fgsBotRight)])

        fgsBotRight.AddMany([(AcceptBtn),
                             (ExitBtn)])

        fgs.AddMany([( self.Nametc,1,wx.EXPAND),
                      (fgsTop,1,wx.EXPAND),
                     (self.ColumnLabel,1,wx.EXPAND),
                     (self.comboPCA1,1,wx.EXPAND),
                     (self.comboPCA2,1,wx.EXPAND),
                     (self.comboPCA3,1,wx.EXPAND),
                     (fgsBotPhe,1,wx.EXPAND),
                     (fgsBot,1,wx.EXPAND)
                    ])

        #fgs.AddGrowableRow(1, 1)
        #fgs.AddGrowableRow(2, 3)
        fgsBotPhe.AddGrowableCol(1,2)
        fgsTop.AddGrowableCol(1,2)
        fgs.AddGrowableCol(0, 1)

        self.vbox.Add(fgs, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(self.vbox)

    def AppearFrame(self,event):
        self.child = AppFrame(self, title='Appearance')
        self.child.ShowModal()
        self.child.Show()

    def Quit(self,event):
        self.Destroy()
        pub.sendMessage('panelListener',message=self._FI)
    
    def OnCombo(self, event):
        print(self.comboPhe.GetValue())

    def onAcceptFile(self,event):
        print('AcceptedData')
        print(self.comboPCA1.Value)
        print(self.comboPCA2.Value)
        print(self.comboPCA3.Value)
        print(self.comboPhe.Value)
        print(self.tc1.Value)
        print(self.tc3.Value)

        name = "File" + str(self._FI.FindLength())
        pheCol = self.comboPhe.Value.split(' ')
        Col1 = self.comboPCA1.Value.split(' ')
        Col2 = self.comboPCA2.Value.split(' ')
        Col3 = self.comboPCA3.Value.split(' ')
        #returns figure
        Figure = ''
        #creates graph dependant on if there is phen data
        if(self.tc3.Value != ""):
            self._FI.CreatePca( self._FI,self.tc1.Value,self.tc3.Value,name,int(Col1[1]),int(Col2[1]),int(pheCol[1]),self._panel)

        else:
            self._FI.CreatePca( self._FI,self.tc1.Value,None,name,int(Col1[1]),int(Col2[1]),3,self._panel)


        
        #pub.sendMessage('panelListener',message="Ronan was HEre")
        plt.show()
        ##I need to give option to put in names ,headings and Name of Graph.

        #self.Destroy()

    def onOpenFile(self, event):
       
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir = self.currentDirectory, 
            defaultFile="",

            wildcard=wildcard,

            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            self.DataFilePath = dlg.GetPath()
            print ('You chose the following file:')
            print(self.DataFilePath)
           
            self.button = event.GetEventObject()

            if self.button.parameterVal == 'Data':
                if(VC.CheckPcaValid(self.DataFilePath)):
                    self.tc1.SetValue(self.DataFilePath)
                    self.CountColumns(self.button)
                else:
                    dlg = wx.MessageDialog(None,"Invalid Admix File","ERROR",wx.OK | wx.ICON_ERROR)
                    dlg.ShowsModal()
                    
            if self.button.parameterVal == 'Phe':
                if(VC.CheckPhenValid(self.DataFilePath)):
                    self.tc3.SetValue(self.DataFilePath)
                    self.CountColumns(self.button)
                else:
                    dlg = wx.MessageDialog(None,"Invalid Phe File","ERROR",wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()
            
            print(self.button.parameterVal)
        dlg.Destroy()
        #CountsColumns
    
        
#counts coloumns in the file
    def CountColumns(self,val):
        self.Columns.clear()
        with open(self.DataFilePath) as myFile:
            reader = csv.reader(myFile,delimiter=' ', skipinitialspace = True )
            first_row = next(reader)
            num_cols = len(first_row)
            print(num_cols)

            for index in range(0,num_cols):
                
                self.Columns.insert(index,'Column ' +str(index+1))
                print(self.Columns)

            
        if self.button.parameterVal == 'Data':
            self.comboPCA1.Clear()      
            self.comboPCA1.AppendItems (self.Columns)
            self.comboPCA1.Value = self.Columns[0]

            self.comboPCA2.Clear()      
            self.comboPCA2.AppendItems (self.Columns)
            self.comboPCA2.Value = self.Columns[1]

            self.comboPCA3.Clear()      
            self.comboPCA3.AppendItems (self.Columns)

            self.comboPCA1.Show()
            self.comboPCA2.Show()
            self.comboPCA3.Show()

            #self.Columns = ['none']

        if self.button.parameterVal == 'Phe':
            self.comboPhe.Clear()      
            self.comboPhe.AppendItems (self.Columns)
            self.comboPhe.Value = self.Columns[2]
            self.comboPhe.Show()
            #self.Columns = ['none']

    def GetPanel(self,message, arg2 = None):
        print("HI")
        self._panel = message

