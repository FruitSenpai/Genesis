import os
import wx
wildcard = "All files (*.*)|*.*"

class PCAAppearFrame(wx.Dialog):
    '''
    This script cotains the code to generate the PCA appearence frame
    '''

    def __init__(self, parent, title):
        super(PCAAppearFrame, self).__init__(parent, title= 'Graph Options', 
            size=(400, 500),style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)

        
        self.InitUI()
        self.Centre()

    def InitUI(self):
        '''Initialises user interface'''
        
        panel = wx.Panel(self,wx.ID_ANY)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        Columns = ['column1', 'column2', 'column3', "none"]

        fgs = wx.FlexGridSizer(12,1,10,10)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)
        fgsInner = wx.FlexGridSizer(1,2,10,10)

        self.HeadingPathtext = wx.TextCtrl(panel, value='Set Heading')
        HeadingBtn = wx.Button(panel,wx.ID_ANY, 'Select Heading Font')
        self.ShowAxes = wx.CheckBox(panel, label = 'Show Axes')
        self.ShowAxisLabels = wx.CheckBox(panel, label = 'Show Axis Labels')
        self.ShowBorder = wx.CheckBox(panel, label = 'Show Border')
        self.ShowGrid = wx.CheckBox(panel, label = 'Show Grid')
        self.ShowScale = wx.CheckBox(panel, label = 'Show Scale') 
        self.KeyPlace = wx.ComboBox(panel, choices = Columns)
        self.KeyPlace.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        KeyBtn = wx.Button(panel,wx.ID_ANY, 'Select Key Font')
        ScaleBtn = wx.Button(panel,wx.ID_ANY, 'Select Scale Font')
        AxisBtn = wx.Button(panel,wx.ID_ANY, 'Select AxisLabel Font')
        self.FinishBtn = wx.Button(panel,wx.ID_ANY, 'Finish')
        self.ExitBtn = wx.Button(panel,wx.ID_EXIT, 'Exit')

        self.ShowAxes.Bind(wx.EVT_CHECKBOX,self.onChecked)
        self.ShowAxisLabels.Bind(wx.EVT_CHECKBOX,self.onChecked)
        self.ShowBorder.Bind(wx.EVT_CHECKBOX,self.onChecked)
        self.ShowGrid.Bind(wx.EVT_CHECKBOX,self.onChecked)
        self.ShowScale.Bind(wx.EVT_CHECKBOX,self.onChecked)
        self.ExitBtn.Bind(wx.EVT_BUTTON, self.QuitEvent)
        self.FinishBtn.Bind(wx.EVT_BUTTON, self.FinishEvent)

        

        fgsInner.AddMany([(self.FinishBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                          (self.ExitBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)])
       

        fgs.AddMany([( self.HeadingPathtext,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (HeadingBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.ShowAxes,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.ShowAxisLabels,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.ShowBorder,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.ShowGrid,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.ShowScale,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (self.KeyPlace,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (KeyBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (ScaleBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     ( AxisBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                      (fgsInner,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)])

        #fgs.AddGrowableRow(1, 1)
        #fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(0, 1)

        hbox.Add(fgs, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def OnCombo(self, event):
        '''Gets values from combobox.'''
        print(self.KeyPlace.GetValue())
       # self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox")

    def onChecked(self, e):
        '''Checks if checkbox is selected.'''
        cb = e.GetEventObject() 
        print (cb.GetLabel(),' is clicked',cb.GetValue())

    def QuitEvent(self,e):
        '''Exits frame.'''
        self.Destroy()

    def FinishEvent(self, e):
        '''Outputs all appearence data'''
        print(self.ShowAxes.GetValue())
        print(self.ShowAxisLabels.GetValue())
        print(self.ShowBorder.GetValue())
        print(self.ShowGrid.GetValue())
        print(self.ShowScale.GetValue())
        print(self.HeadingPathtext.GetValue())
