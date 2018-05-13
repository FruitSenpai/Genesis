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
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
        '''
        This is the code to generate the Pca custom frame.

        This only contains the code to generate the frame nothing else
        '''
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PCA Customization", pos = wx.DefaultPosition, size = wx.Size( 188,221 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		GroupComboChoices = []
		self.GroupCombo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, GroupComboChoices, 0 )
		bSizer3.Add( self.GroupCombo, 1, wx.ALL|wx.EXPAND, 5 )
		
		ColourComboChoices = []
		self.ColourCombo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, ColourComboChoices, 0 )
		bSizer3.Add( self.ColourCombo, 1, wx.ALL|wx.EXPAND, 5 )
		
		MarkerComboChoices = []
		self.MarkerCombo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, MarkerComboChoices, 0 )
		bSizer3.Add( self.MarkerCombo, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.AcceptButton = wx.Button( self, wx.ID_ANY, u"Accept", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.AcceptButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.ExitButton = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.ExitButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.FillBoxes )
		self.GroupCombo.Bind( wx.EVT_COMBOBOX, self.SetGroup )
		self.ColourCombo.Bind( wx.EVT_COMBOBOX, self.SetColour )
		self.MarkerCombo.Bind( wx.EVT_COMBOBOX, self.SetMarker )
		self.AcceptButton.Bind( wx.EVT_BUTTON, self.onAccept )
		self.ExitButton.Bind( wx.EVT_BUTTON, self.onExit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FillBoxes( self, event ):
		event.Skip()
	
	def SetGroup( self, event ):
		event.Skip()
	
	def SetColour( self, event ):
		event.Skip()
	
	def SetMarker( self, event ):
		event.Skip()
	
	def onAccept( self, event ):
		event.Skip()
	
	def onExit( self, event ):
		event.Skip()
	

