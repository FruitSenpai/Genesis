import os
import wx
import sys
import matplotlib.pyplot as plt
#print(os.getcwd())

#import FileImporter as fileImp
from FileManagement.FileImporter import FileImporter
wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
class PCAFrame(wx.Frame):
    
   
    
    def __init__(self, parent, title):
        super(PCAFrame, self).__init__(parent, title= 'admix', 
            size=(300, 250))

        #pan = wx.Panel(self,wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        self.InitUI()
        self.Centre()

        self._FI = FileImporter()
       
        
    def InitUI(self):
        
        
        panel = wx.Panel(self,wx.ID_ANY)

        Columns = ['column1', 'column2', 'column3']
        self.comboPCA1 = wx.ComboBox(panel, choices = Columns)
        self.comboPCA1.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.comboPCA2 = wx.ComboBox(panel, choices = Columns)
        self.comboPCA2.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.comboPCA3 = wx.ComboBox(panel, choices = Columns)
        self.comboPCA3.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.comboPhe = wx.ComboBox(panel, choices = Columns)
        self.comboPhe.Bind(wx.EVT_COMBOBOX, self.OnCombo)

        ColumnLabel = wx.StaticText(panel,label = "Select PCAs")
        PheLabel = wx.StaticText(panel,label = "Which Column is the phenotype")

        vbox = wx.BoxSizer(wx.VERTICAL)

        fgsTop = wx.FlexGridSizer(2,2,10,10)
        fgs = wx.FlexGridSizer(7,1,10,10)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)
        fgsBotPhe = wx.FlexGridSizer(1,2,10,10)
        fgsBot = wx.FlexGridSizer(1,2,10,10)
        
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

        self.tc1 = wx.TextCtrl(panel)
        
        self.tc3 = wx.TextCtrl(panel)

        fgsTop.AddMany([(OpenFileBtn), (self.tc1, 1, wx.EXPAND),
                     (OpenPheBtn, 1, wx.EXPAND),( self.tc3, 1, wx.EXPAND)])
                     

        fgsBotPhe.AddMany([(PheLabel,1,wx.EXPAND),
                         (self.comboPhe,1,wx.EXPAND)
                         ])
        fgsBot.AddMany([(AcceptBtn),
                        (ExitBtn)])

        fgs.AddMany([(fgsTop,1,wx.EXPAND),
                     (ColumnLabel,1,wx.EXPAND),
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

        vbox.Add(fgs, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(vbox)

    def Quit(self,event):
        self.Destroy()
    
    def OnCombo(self, event):
        print(self.combo.GetValue())

    def onAcceptFile(self,event):
        print('AcceptedData')
        print(self.comboPCA1.Value)
        print(self.comboPCA1.Value)
        print(self.comboPCA1.Value)
        print(self.comboPhe.Value)
        print(self.tc1.Value)
        print("-"+self.tc3.Value+"-")

        name = "File" + str(self._FI.FindLength())

        if(self.tc3.Value != ""):
            self._FI.CreatePca( self._FI,self.tc1.Value,self.tc3.Value,name)

        else:
            self._FI.CreatePca( self._FI,self.tc1.Value,None,name)
            
        plt.show()
        #self.Destroy()

    def onOpenFile(self, event):
       
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            DataFilePath = dlg.GetPath()
            print ('You chose the following file:')
            print(DataFilePath)
           # windowClass.AdmixPath = DataFilePath
            button = event.GetEventObject()

            if button.parameterVal == 'Data':
                self.tc1.SetValue(DataFilePath)
            if button.parameterVal == 'Fam':
                self.tc2.SetValue(DataFilePath)
            if button.parameterVal == 'Phe':
                self.tc3.SetValue(DataFilePath)
            
            print(button.parameterVal)
        dlg.Destroy()
