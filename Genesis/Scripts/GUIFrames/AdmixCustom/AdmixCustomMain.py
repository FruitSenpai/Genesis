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
## Class AdmixMainMenu
###########################################################################

class AdmixMainMenu ( wx.Frame ):
        '''
        Main customisation frame for the admix.

        This frame is used to access the other parts of the admix customisation options.
        This class only contains the code required to make the frame none of the functionality.
        '''
        
        def __init__( self, parent ):
                wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 267,91 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
                
                self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
                
                gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
                
                self.AncestryButton = wx.Button( self, wx.ID_ANY, u"Ancestry", wx.DefaultPosition, wx.DefaultSize, 0 )
                gSizer5.Add( self.AncestryButton, 1, wx.ALL|wx.EXPAND, 5 )
                
                self.GroupButton = wx.Button( self, wx.ID_ANY, u"Groups", wx.DefaultPosition, wx.DefaultSize, 0 )
                gSizer5.Add( self.GroupButton, 1, wx.ALL|wx.EXPAND, 5 )
                
                
                self.SetSizer( gSizer5 )
                self.Layout()
                
                self.Centre( wx.BOTH )
                
                # Connect Events
                self.AncestryButton.Bind( wx.EVT_BUTTON, self.LoadAncestryOptions )
                self.GroupButton.Bind( wx.EVT_BUTTON, self.LoadGroupOptions )
        
        def __del__( self ):
                pass
        
        
        # Virtual event handlers, overide them in your derived class
        def LoadAncestryOptions( self, event ):
                event.Skip()
        
        def LoadGroupOptions( self, event ):
                event.Skip()
        

