import os
import wx
wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
class AppearFrame(wx.Frame):
    '''
    This frame contains the code generate the admix appearence frame.
    '''

    def __init__(self, parent, title):
        super(AppearFrame, self).__init__(parent, title= 'Appearence', 
            size=(350, 650))

        self.InitUI()
        self.Centre()
        

    def InitUI(self):
        '''Initialises user interface.'''
        
        panel = wx.Panel(self,wx.ID_ANY)

        vbox = wx.BoxSizer(wx.VERTICAL)

        fgs = wx.FlexGridSizer(10,1,10,10)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)
        fgsInner = wx.FlexGridSizer(3,2,10,10)
        fgsBot = wx.FlexGridSizer(1,2,10,10)

        HeadingLabel = wx.StaticText(panel,label = "Set Heading")
        self.Headingtext = wx.TextCtrl(panel, value="Heading Text")
        HeadingFontBtn = wx.Button(panel,wx.ID_ANY, 'Select Heading Font')
        self.BorderCb = wx.CheckBox(panel, label = 'Show Borders')
        self.PopCb = wx.CheckBox(panel, label = 'Show population group labels') 

        SetGraphHeightLabel = wx.StaticText(panel,label = "Set Graph Height")
        ThicknessLabel = wx.StaticText(panel,label = "Set thickness of each subject")
        DistanceLabel = wx.StaticText(panel,label = "Set distance between graph")
        self.SetGraphHeighttext = wx.SpinCtrl(panel, value ='0')
        self.Thicknesstext = wx.SpinCtrl(panel, value ='0')
        self.Distancetext = wx.SpinCtrl(panel, value ='0')
        
        fgsInner.AddMany([(SetGraphHeightLabel,2,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                          (self.SetGraphHeighttext,2,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                          (ThicknessLabel,2,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                          (self.Thicknesstext,2,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                          (DistanceLabel,2,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                          (self.Distancetext,2,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)])
        
        PopFontBtn = wx.Button(panel,wx.ID_ANY, 'Select Population Group Font')
        SetMarginsBtn = wx.Button(panel,wx.ID_ANY, 'Set Margins')
        SetMarginsBtn.Bind(wx.EVT_BUTTON, self.SetMargins)
        
        AcceptBtn = wx.Button(panel,wx.ID_EXIT, 'Accept')
        AcceptBtn.Bind(wx.EVT_BUTTON, self.FinishEvent)
        ExitBtn = wx.Button(panel,wx.ID_EXIT, 'Exit')
        ExitBtn.Bind(wx.EVT_BUTTON, self.QuitEvent)
        Orientation = ['Horizontal', 'Vertical']
        self.combo = wx.ComboBox(panel, choices = Orientation)

        fgsBot.AddMany([(AcceptBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                        (ExitBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)])
        

        fgs.AddMany([(HeadingLabel,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                    (self.Headingtext,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                    (HeadingFontBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                    (self.BorderCb,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                    (self.PopCb ,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                    (PopFontBtn ,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                    (fgsInner ,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                    (SetMarginsBtn ,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                    (self.combo ,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                    (fgsBot ,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)])

        #fgs.AddGrowableRow(1, 1)
        #fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(0, 1)
        fgsInner.AddGrowableCol(1, 2)

        vbox.Add(fgs, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(vbox)


    def SetMargins(self,e):
        '''Sets graph height and thickness and distance of margins.'''
        print(self.SetGraphHeighttext.GetValue())
        print(self.Thicknesstext.GetValue())
        print(self.Distancetext.GetValue())
    
    def QuitEvent(self,e):
        '''Exits frame.'''
        self.Destroy()

    def FinishEvent(self, e):
        '''Outputs selected appearence data.'''
        print(self.Headingtext.GetValue())
        print(self.SetGraphHeighttext.GetValue())
        print(self.Thicknesstext.GetValue())
        print(self.Distancetext.GetValue())
        print(self.BorderCb.GetValue())
        print(self.PopCb.GetValue())
        print(self.combo.GetValue())
        #print(self.HeadingPathtext.GetValue())
