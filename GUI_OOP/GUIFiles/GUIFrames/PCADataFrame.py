import os
import wx
wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
class PCADataFrame(wx.Frame):

    def __init__(self, parent, title):
        super(PCADataFrame, self).__init__(parent, title= 'Graph Options', 
            size=(250, 350))

        self.InitUI()
        self.Centre()

    def InitUI(self):
        
        panel = wx.Panel(self,wx.ID_ANY)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        Columns = ['column1', 'column2', 'column3', "none"]

        fgs = wx.FlexGridSizer(6,1,10,10)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)
        fgsInner = wx.FlexGridSizer(1,2,10,10)

        ColumnLabel = wx.StaticText(panel,label = "Select PCAs")
        self.PCA1 = wx.ComboBox(panel, choices = Columns)
        self.PCA1.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.PCA2 = wx.ComboBox(panel, choices = Columns)
        self.PCA2.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.PCA3 = wx.ComboBox(panel, choices = Columns)
        self.PCA3.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.PheColumn = wx.ComboBox(panel, choices = Columns)
        self.PheColumn.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        FinishBtn = wx.Button(panel,wx.ID_ANY, 'Finish')
        FinishBtn.Bind(wx.EVT_BUTTON, self.PCAAccept)
        ExitBtn = wx.Button(panel,wx.ID_EXIT, 'Exit')
        ExitBtn.Bind(wx.EVT_BUTTON, self.QuitEvent)

        fgsInner.AddMany([(FinishBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                          (ExitBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)])
       

        fgs.AddMany([(ColumnLabel,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.PCA1,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.PCA2,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.PCA3,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.PheColumn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                      (fgsInner,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)])

        #fgs.AddGrowableRow(1, 1)
        #fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(0, 1)

        hbox.Add(fgs, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def OnCombo(self, event):
        print(self.PCA1.GetValue())
       # self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox")

    def QuitEvent(self,e):
        self.Destroy()

    def PCAAccept(self,event):
        print(self.PCA1.GetValue())
        print(self.PCA2.GetValue())
        print(self.PCA3.GetValue())
        print(self.PCA4.GetValue())
