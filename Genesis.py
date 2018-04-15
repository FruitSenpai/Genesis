import os
import wx

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
        self.child = ChildFrame(self, title='Admix')
        self.child.Show()

    def PCAEvent(self,e):
        wx.MessageBox('Input PCA')

    def SaveEvent(self,e):
        wx.MessageBox('Save file')

    def OpenFileEvent(self,e):
        wx.MessageBox('Open file')
    
    def DataOptionsEvent(self,e):
        self.child = AdmixGraphFrame(self, title='Graph Options')
        #self.child = PCADataFrame(self, title='Graph Options')
        self.child.Show()

    def AppearenceEvent(self,e):
        print('Pretty things')
        self.child = AppearFrame(self, title='Export as')
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
        self.child = ExportFrame(self, title='Export as')
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


class ChildFrame(wx.Frame):
    
   
    
    def __init__(self, parent, title):
        super(ChildFrame, self).__init__(parent, title= 'admix', 
            size=(300, 250))

        #pan = wx.Panel(self,wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        self.InitUI()
        self.Centre()
       
        
    def InitUI(self):
        
        
        panel = wx.Panel(self,wx.ID_ANY)

        Columns = ['column1', 'column2', 'column3']
        self.combo = wx.ComboBox(panel, choices = Columns)
        self.combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)

        ColumnLabel = wx.StaticText(panel,label = "Phenotype Column") 

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(5,2,10,10)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)

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

        #fgs.AddGrowableRow(1, 1)
        #fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def Quit(self,event):
        self.Destroy()
    
    def OnCombo(self, event):
        print(self.combo.GetValue())
       # self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox") 

    def onAcceptFile(self,event):
        print('AcceptedData')

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
            windowClass.AdmixPath = DataFilePath
            button = event.GetEventObject()

            if button.parameterVal == 'Data':
                self.tc1.SetValue(DataFilePath)
            if button.parameterVal == 'Fam':
                self.tc2.SetValue(DataFilePath)
            if button.parameterVal == 'Phe':
                self.tc3.SetValue(DataFilePath)
            
            print(button.parameterVal)
        dlg.Destroy()
    

class ExportFrame(wx.Frame):

    def __init__(self, parent, title):
        super(ExportFrame, self).__init__(parent, title= 'Export as', 
            size=(100, 250))

        self.InitUI()
        self.Centre()

    def InitUI(self):
        
        panel = wx.Panel(self,wx.ID_ANY)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(4,1,10,10)#Wx.FlexiGridSizer(rows, cols, vgap, hgap)

        PDFBtn = wx.Button(panel,wx.ID_ANY, 'PDF')
        PNGBtn = wx.Button(panel,wx.ID_ANY, 'PNG')
        SVGBtn = wx.Button(panel,wx.ID_ANY, 'SVG')
        ExitBtn = wx.Button(panel,wx.ID_EXIT, 'Exit')
        

        fgs.AddMany([(PDFBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (PNGBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (SVGBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5),
                     (ExitBtn,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)])

        #fgs.AddGrowableRow(1, 1)
        #fgs.AddGrowableRow(2, 3)
        #fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=2, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)
        
        
        
class AppearFrame(wx.Frame):

    def __init__(self, parent, title):
        super(AppearFrame, self).__init__(parent, title= 'Appearence', 
            size=(350, 650))

        self.InitUI()
        self.Centre()

    def InitUI(self):
        
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
        print(self.SetGraphHeighttext.GetValue())
        print(self.Thicknesstext.GetValue())
        print(self.Distancetext.GetValue())
    
    def QuitEvent(self,e):
        self.Destroy()

    def FinishEvent(self, e):
        print(self.Headingtext.GetValue())
        print(self.SetGraphHeighttext.GetValue())
        print(self.Thicknesstext.GetValue())
        print(self.Distancetext.GetValue())
        print(self.BorderCb.GetValue())
        print(self.PopCb.GetValue())
        print(self.combo.GetValue())
        #print(self.HeadingPathtext.GetValue())
      
class AdmixGraphFrame(wx.Frame):


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
            windowClass.AdmixPath = DataFilePath
            button = event.GetEventObject()
            self.FilePathtext.SetValue(DataFilePath)
         
        dlg.Destroy()

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

class PCAAppearFrame(wx.Frame):

    def __init__(self, parent, title):
        super(PCAAppearFrame, self).__init__(parent, title= 'Graph Options', 
            size=(400, 500))

        self.InitUI()
        self.Centre()

    def InitUI(self):
        
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
        print(self.KeyPlace.GetValue())
       # self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox")

    def onChecked(self, e):
        cb = e.GetEventObject() 
        print (cb.GetLabel(),' is clicked',cb.GetValue())

    def QuitEvent(self,e):
        self.Destroy()

    def FinishEvent(self, e):
        print(self.ShowAxes.GetValue())
        print(self.ShowAxisLabels.GetValue())
        print(self.ShowBorder.GetValue())
        print(self.ShowGrid.GetValue())
        print(self.ShowScale.GetValue())
        print(self.HeadingPathtext.GetValue())
    


def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()

main()


