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
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 284,204 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetWindowStyle(wx.STAY_ON_TOP)
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.Group_Label = wx.StaticText( self, wx.ID_ANY, u"Group", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Group_Label.Wrap( -1 )
		gbSizer1.Add( self.Group_Label, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Icon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.SizeLabel = wx.StaticText( self, wx.ID_ANY, u"Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SizeLabel.Wrap( -1 )
		gbSizer1.Add( self.SizeLabel, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.SizeBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SizeBox.SetMinSize( wx.Size( 112,-1 ) )
		
		gbSizer1.Add( self.SizeBox, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.AcceptButton = wx.Button( self, wx.ID_ANY, u"Accept", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.AcceptButton, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.ExitButton = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.ExitButton, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		GroupComboChoices = []
		self.GroupCombo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, GroupComboChoices, 0 )
		gbSizer1.Add( self.GroupCombo, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		ColourComboChoices = []
		self.ColourCombo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, ColourComboChoices, 0 )
		gbSizer1.Add( self.ColourCombo, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		MarkerComboChoices = []
		self.MarkerCombo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, MarkerComboChoices, 0 )
		gbSizer1.Add( self.MarkerCombo, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.FillBoxes )
		self.SizeBox.Bind( wx.EVT_TEXT_ENTER, self.SetSize )
		self.AcceptButton.Bind( wx.EVT_BUTTON, self.onAccept )
		self.ExitButton.Bind( wx.EVT_BUTTON, self.onExit )
		self.GroupCombo.Bind( wx.EVT_COMBOBOX, self.SetGroup )
		self.ColourCombo.Bind( wx.EVT_COMBOBOX, self.SetColour )
		self.MarkerCombo.Bind( wx.EVT_COMBOBOX, self.SetMarker )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FillBoxes( self, event ):
		event.Skip()
	
	def SetSize( self, event ):
		event.Skip()
	
	def onAccept( self, event ):
		event.Skip()
	
	def onExit( self, event ):
		event.Skip()
	
	def SetGroup( self, event ):
		event.Skip()
	
	def SetColour( self, event ):
		event.Skip()
	
	def SetMarker( self, event ):
		event.Skip()
	

