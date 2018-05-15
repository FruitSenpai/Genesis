# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Group Frame
###########################################################################

class GroupFrame ( wx.Frame ):
    '''
    Contains the code for the Admix Group Custom Frame.

    Only contains code for the generation of the frame.
    '''
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Group Customization ", pos = wx.DefaultPosition, size = wx.Size( 345,167 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetWindowStyle(wx.STAY_ON_TOP)
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Group Name", wx.Point( 200,200 ), wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.GroupLeftButton = wx.Button( self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.GroupLeftButton.SetMinSize( wx.Size( 20,-1 ) )
        
        gbSizer1.Add( self.GroupLeftButton, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.Group_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Group_textCtrl.Enable( False )
        
        gbSizer1.Add( self.Group_textCtrl, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.GroupRightButton = wx.Button( self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.GroupRightButton.SetMinSize( wx.Size( 20,-1 ) )
        
        gbSizer1.Add( self.GroupRightButton, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Order", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.Order_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Order_textCtrl1.Enable( False )
        
        gbSizer1.Add( self.Order_textCtrl1, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.OrderLeftButton1 = wx.Button( self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.OrderLeftButton1.SetMinSize( wx.Size( 20,-1 ) )
        
        gbSizer1.Add( self.OrderLeftButton1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.OrderRightButton1 = wx.Button( self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.OrderRightButton1.SetMinSize( wx.Size( 20,-1 ) )
        
        gbSizer1.Add( self.OrderRightButton1, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.SortDominanceButton = wx.Button( self, wx.ID_ANY, u"Sort By Dominance", wx.DefaultPosition, wx.Size( 260,-1 ), 0 )
        gbSizer1.Add( self.SortDominanceButton, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )
        
        self.CheckBox_Group = wx.CheckBox( self, wx.ID_ANY, u"Sort Most Dominant to least", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.CheckBox_Group, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

        self.CheckBox_Hide = wx.CheckBox( self, wx.ID_ANY, u"Hide Group", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.CheckBox_Hide, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.ExitButton = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )  
        gbSizer1.Add( self.ExitButton, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
        

        self.SetSizer( gbSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.GroupLeftButton.Bind( wx.EVT_BUTTON, self.PrevGroup )
        self.GroupRightButton.Bind( wx.EVT_BUTTON, self.NextGroup )
        self.OrderLeftButton1.Bind( wx.EVT_BUTTON, self.ShiftGroupLeft )
        self.OrderRightButton1.Bind( wx.EVT_BUTTON, self.ShiftGroupRight )
        self.SortDominanceButton.Bind( wx.EVT_BUTTON, self.sortByGroupDominance )
        self.CheckBox_Group.Bind( wx.EVT_CHECKBOX, self.ChangeSortDirection )
        self.CheckBox_Hide.Bind(wx.EVT_CHECKBOX, self.HideGroup)
        self.ExitButton.Bind( wx.EVT_BUTTON, self.Exit )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def PrevGroup( self, event ):
        event.Skip()
    
    def NextGroup( self, event ):
        event.Skip()
    
    def ShiftGroupLeft( self, event ):
        event.Skip()
    
    def ShiftGroupRight( self, event ):
        event.Skip()
    
    def sortByGroupDominance( self, event ):
        event.Skip()
    
    def ChangeSortDirection( self, event ):
        event.Skip()

    def HideGroup( self, event ):
        event.Skip()

    def Exit(self, event):
        self.Destroy()
    

