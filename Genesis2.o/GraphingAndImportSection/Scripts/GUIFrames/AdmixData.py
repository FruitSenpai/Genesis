import os
import wx
wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
class AdmixGraphFrame(wx.Frame):
'''  This is the admix graph options frame.'''

    def __init__(self, parent, title):
        super(AdmixGraphFrame, self).__init__(parent, title= 'Graph Options', 
            size=(400, 200))

        self.currentDirectory = os.getcwd()
        self.InitUI()
        self.Centre()

    def InitUI(self):
        
        panel = wx.Panel(self,wx.ID_ANY)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        Columns = ['column1', 'column2', 'column3']

        fgs = wx.FlexGridSizer(4,2,10,10)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)

        ImportBtn = wx.Button(panel,wx.ID_ANY, 'Import Additional Files')
        ImportBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        self.FilePathtext = wx.TextCtrl(panel)
        ColumnLabel = wx.StaticText(panel,label = "Phenotype Column")
        self.combo = wx.ComboBox(panel, choices = Columns)
        self.combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        FinishBtn = wx.Button(panel,wx.ID_ANY, 'Finish')
        FinishBtn.Bind(wx.EVT_BUTTON, self.FinishEvent)
        ExitBtn = wx.Button(panel,wx.ID_EXIT, 'Exit')
        ExitBtn.Bind(wx.EVT_BUTTON, self.QuitEvent)
       

        fgs.AddMany([(ImportBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.FilePathtext,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (ColumnLabel,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.combo,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                      (FinishBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                      (ExitBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)])

        #fgs.AddGrowableRow(1, 1)
        #fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def OnCombo(self, event):
        print(self.combo.GetValue())
       # self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox")

    def QuitEvent(self,event):
        self.Destroy()


    def FinishEvent(self,event):
        print(self.combo.GetValue())
        print(self.FilePathtext.GetValue())

    
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
            #windowClass.AdmixPath = DataFilePath
            button = event.GetEventObject()
            self.FilePathtext.SetValue(DataFilePath)
         
        dlg.Destroy()
