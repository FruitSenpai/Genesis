import os
import wx
from wx.lib.pubsub import pub
import csv
import matplotlib.pyplot as plt
from FileManagement.FileImporter import FileImporter
from GUIFrames import DataHolder
from GUIFrames.PCAAppear import PCAAppearFrame as PCAAppearFrame
from FileManagement  import ValidityChecker as VC
'''wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"'''

wildcard = ""

admixWildcard = "Q file (*.Q.n)|*.Q.*|" \
            "All files (*.*)|*.*"

famWildcard = "fam file (*.fam)|*.fam|" \
            "All files (*.*)|*.*"

pheWildcard = "phenotype file (*.phe)|*.phe|" \
            "All files (*.*)|*.*"

class ChildFrame(wx.Frame):
    
   
    
    def __init__(self, parent, title):
        super(ChildFrame, self).__init__(parent, title= 'admix', 
            size=(300, 300))

        #pan = wx.Panel(self,wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        self.InitUI()
        self.Centre()
        self._DH = DataHolder
        self._FI = FileImporter()
        pub.subscribe(self.GetPanel, "GetPanelAdmix")
        
    def InitUI(self):
        
        
        panel = wx.Panel(self,wx.ID_ANY)

        self.Columns = []

        self.m_textCtrl1 = wx.TextCtrl( panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl1.Value = "Name"

        self.combo = wx.ComboBox(panel, choices = self.Columns)
        self.combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)

        ColumnLabel = wx.StaticText(panel,label = "Phenotype Column") 

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        
        fgs = wx.FlexGridSizer(6,2,15,15)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)
        fgsWhole = wx.FlexGridSizer(2,1,15,15)

        OpenFileBtn = wx.Button(panel,wx.ID_ANY, label ='Import Data File')
        OpenFileBtn.parameterVal = 'Data'
        OpenFamBtn = wx.Button(panel,wx.ID_ANY, label ='Import Fam File')
        OpenFamBtn.parameterVal = 'Fam'
        OpenPheBtn = wx.Button(panel,wx.ID_ANY, label ='Import Phe File')
        OpenPheBtn.parameterVal = 'Phe'
        AcceptBtn = wx.Button(panel,wx.ID_ANY, label ='Accept')
        ExitBtn = wx.Button(panel,wx.ID_EXIT, label ='Exit')
        OpenFileBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        OpenFamBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        OpenPheBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        AcceptBtn.Bind(wx.EVT_BUTTON, self.onAcceptFile)
        ExitBtn.Bind(wx.EVT_BUTTON, self.Quit)

        self.tc1 = wx.TextCtrl(panel)
        self.tc2 = wx.TextCtrl(panel)
        self.tc3 = wx.TextCtrl(panel)

        fgs.AddMany([(OpenFileBtn), (self.tc1, 1, wx.EXPAND),
                     (OpenFamBtn), 
                     (self.tc2, 1, wx.EXPAND),
                     (OpenPheBtn, 1, wx.EXPAND),
                     ( self.tc3, 1, wx.EXPAND),
                     (ColumnLabel,1,wx.EXPAND) ,
                     (self.combo,1,wx.EXPAND),
                     (AcceptBtn),
                     (ExitBtn)])
        fgsWhole.AddMany([(self.m_textCtrl1, 1, wx.EXPAND),
                     (fgs, 1, wx.EXPAND)
                     ])

        #fgs.AddGrowableRow(1, 2)
        fgsWhole.AddGrowableCol(0,2)
        #fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(1, 0)

        hbox.Add(fgsWhole, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def Quit(self,event):
        pub.sendMessage('panelListener',message=self._FI)
        self.Destroy()

    def AppearFrame(self,event):
        self.child = PCAAppearFrame(self, title='Appearance')
        #self.child.ShowModal()
        self.child.Show()
    
    def OnCombo(self, event):
        print(self.combo.GetValue())
       # self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox") 

    def onAcceptFile(self,event):
        print('AcceptedData')
        print(self.tc1.Value)
        print(self.tc2.Value)
        print(self.tc3.Value)
        print(self.combo.Value)
        name = self.m_textCtrl1.Value
        #name = "File" + str(self._FI.FindLength())
        col = self.combo.Value.split(' ')
        if(self.tc1.Value != "" and self.tc2.Value != ""):
            try:
                if (self.tc3.Value != ""):
                    self._FI.CreateAdmix(self._FI,self.tc1.Value,self.tc2.Value,self.tc3.Value,name,int(col[1]),self._panel)
                else:
                    self._FI.CreateAdmix(self._FI,self.tc1.Value,self.tc2.Value,None,name,3,self._panel)
            except IndexError:
                print("Index Error")
        else:
            print("No Fam and Data File")
        plt.show()

        

    def onOpenFile(self, event):
        button = event.GetEventObject()
        if button.parameterVal == 'Data':
                wildcard = admixWildcard
        if button.parameterVal == 'Fam':
                wildcard = famWildcard
        if button.parameterVal == 'Phe':
                wildcard = pheWildcard
                self.CountColumns()

        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            self.DataFilePath = dlg.GetPath()
            print ('You chose the following file:')
            print(self.DataFilePath)
           # windowClass.AdmixPath = DataFilePath
            

            if button.parameterVal == 'Data':
                if(VC.CheckAdmixValid(self.DataFilePath)):
                    self.tc1.SetValue(self.DataFilePath)
                    #self.CountColumns()
                else:
                    dlg = wx.MessageDialog(None,"Invalid Admix File","ERROR",wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()

            if button.parameterVal == 'Fam':
                if(VC.CheckFamValid(self.DataFilePath)):
                    self.tc2.SetValue(self.DataFilePath)
                   # self.CountColumns()
                else:
                    dlg = wx.MessageDialog(None,"Invalid Fam File","ERROR",wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()

            if button.parameterVal == 'Phe':
                if(VC.CheckPhenValid(self.DataFilePath)):
                    self.tc3.SetValue(self.DataFilePath)
                    self.CountColumns()
                else:
                    dlg = wx.MessageDialog(None,"Invalid Phe File","ERROR",wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()
            
            print(button.parameterVal)
        dlg.Destroy()

    def CountColumns(self):
        with open(self.DataFilePath) as myFile:
            reader = csv.reader(myFile,delimiter=' ', skipinitialspace = True )
            first_row = next(reader)
            num_cols = len(first_row)
            print(num_cols)

            for index in range(0,num_cols):
                
                self.Columns.insert(index,'Column ' +str(index+1))
                print(self.Columns)

      
        self.combo.Clear()      
        self.combo.AppendItems (self.Columns)
        self.combo.Value = self.Columns[2]
        #self.Columns = ['none']

    def GetPanel(self,message, arg2 = None):
        print("HI")
        self._panel = message
