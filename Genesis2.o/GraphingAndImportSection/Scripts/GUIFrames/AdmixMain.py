import os
import wx
import csv
import matplotlib.pyplot as plt
from wx.lib.pubsub import pub
from FileManagement.FileImporter import FileImporter
from GUIFrames import DataHolder
from GUIFrames.PCAAppear import PCAAppearFrame as PCAAppearFrame
from FileManagement  import ValidityChecker as VC
wildcard = "All files (*.*)|*.*" 
           
            
class ChildFrame(wx.Dialog):
    
   
    
    def __init__(self, parent, title):
        super(ChildFrame, self).__init__(parent, title= 'admix', 
            size=(300, 250),style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)

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
        self.combo = wx.ComboBox(panel, choices = self.Columns)
        self.combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)

        ColumnLabel = wx.StaticText(panel,label = "Phenotype Column") 

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgsWhole = wx.FlexGridSizer(3,1,10,10)
        fgs = wx.FlexGridSizer(5,2,10,10)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)
        fgsBot = wx.FlexGridSizer(1,2,10,10)
        
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
        
        NextBtn = wx.Button(panel,wx.ID_ANY, label ='Next')
        NextBtn.Bind(wx.EVT_BUTTON, self.AppearFrame)

        self.Nametc = wx.TextCtrl(panel, value="Name")
        self.tc1 = wx.TextCtrl(panel)
        self.tc2 = wx.TextCtrl(panel)
        self.tc3 = wx.TextCtrl(panel)

        fgsBot.AddMany([(AcceptBtn),
                         (ExitBtn)])

        fgs.AddMany([(OpenFileBtn), (self.tc1, 1, wx.EXPAND),
                     (OpenFamBtn), 
                     (self.tc2, 1, wx.EXPAND),
                     (OpenPheBtn, 1, wx.EXPAND),
                     ( self.tc3, 1, wx.EXPAND),
                     (ColumnLabel,1,wx.EXPAND) ,
                     (self.combo,1,wx.EXPAND),
                     (NextBtn),
                     (fgsBot)])

        fgsWhole.AddMany([(self.Nametc, 1, wx.EXPAND),
                     (fgs), 
                     (fgsBot)])

        #fgs.AddGrowableRow(1, 1)
        #fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgsWhole, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def AppearFrame(self,event):
        self.child = PCAAppearFrame(self, title='Appearance')
        self.child.ShowModal()
        self.child.Show()
        
    def Quit(self,event):
        self.Destroy()
    
    def OnCombo(self, event):
        print(self.combo.GetValue())
       # self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox") 

    def onAcceptFile(self,event):
        print('AcceptedData')
        print(self.tc1.Value)
        print(self.tc2.Value)
        print(self.tc3.Value)
        print(self.combo.Value)
        print(self.Nametc.Value)
        name = "File" + str(self._FI.FindLength())
        col = self.combo.Value.split(' ')
        Figure = ""
        if (self.tc3.Value != ""):
            Figure = self._FI.CreateAdmix(self._FI,self.tc1.Value,self.tc2.Value,self.tc3.Value,name,int(col[1]))
        else:
            Figure = self._FI.CreateAdmix(self._FI,self.tc1.Value,self.tc2.Value,None,name,3)

        self._DH.Figures.update({name:Figure})
        plt.show()
        

    def onOpenFile(self, event):
       
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
            button = event.GetEventObject()

            if button.parameterVal == 'Data':
                if(VC.CheckAdmixValid(self.DataFilePath)):
                    self.tc1.SetValue(self.DataFilePath)
                    self.CountColumns()
                else:
                    dlg = wx.MessageDialog(None,"Invalid Admix File","ERROR",wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()

            if button.parameterVal == 'Fam':
                if(VC.CheckFamValid(self.DataFilePath)):
                    self.tc2.SetValue(self.DataFilePath)
                    self.CountColumns()
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
                
            
            #print(button.parameterVal)
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
        self.scombo.Value = self.Columns[2]
        #self.Columns = ['none']

    def GetPanel(self,message, arg2 = None):
        print("HI")
        self._panel = message
