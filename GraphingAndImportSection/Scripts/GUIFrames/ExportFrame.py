import os
import wx
wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
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
        
