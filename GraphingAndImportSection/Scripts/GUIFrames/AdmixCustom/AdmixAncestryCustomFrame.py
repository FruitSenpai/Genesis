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
## Class AdmixAncestryCustom
###########################################################################

class AdmixAncestryCustom ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 253,204 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.Anc_Label = wx.StaticText( self, wx.ID_ANY, u"Ancestor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Anc_Label.Wrap( -1 )
		gbSizer2.Add( self.Anc_Label, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Anc_ButtonLeft = wx.Button( self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Anc_ButtonLeft.SetMinSize( wx.Size( 20,-1 ) )
		
		gbSizer2.Add( self.Anc_ButtonLeft, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.Anc_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Anc_textCtrl.Enable( False )
		
		gbSizer2.Add( self.Anc_textCtrl, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.Anc_ButtonRight = wx.Button( self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Anc_ButtonRight.SetMinSize( wx.Size( 20,-1 ) )
		
		gbSizer2.Add( self.Anc_ButtonRight, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.Order_Label = wx.StaticText( self, wx.ID_ANY, u"Order", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Order_Label.Wrap( -1 )
		gbSizer2.Add( self.Order_Label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.order_ButtonLeft = wx.Button( self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.order_ButtonLeft.SetMinSize( wx.Size( 20,-1 ) )
		
		gbSizer2.Add( self.order_ButtonLeft, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.Order_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Order_textCtrl.Enable( False )
		
		gbSizer2.Add( self.Order_textCtrl, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.Order_ButtonRight = wx.Button( self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Order_ButtonRight.SetMinSize( wx.Size( 20,-1 ) )
		
		gbSizer2.Add( self.Order_ButtonRight, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.Colour_Label = wx.StaticText( self, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Colour_Label.Wrap( -1 )
		gbSizer2.Add( self.Colour_Label, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		Colour_ComboBoxChoices = []
		self.Colour_ComboBox = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, Colour_ComboBoxChoices, 0 )
		gbSizer2.Add( self.Colour_ComboBox, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.SortDom_Button = wx.Button( self, wx.ID_ANY, u"Sort By Dominance", wx.DefaultPosition, wx.Size( 235,-1 ), 0 )
		gbSizer2.Add( self.SortDom_Button, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )
		
		self.Dom_CheckBox = wx.CheckBox( self, wx.ID_ANY, u"Most to least dominant", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.Dom_CheckBox, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )
		
		
		self.SetSizer( gbSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.FillColours )
		self.Anc_ButtonLeft.Bind( wx.EVT_BUTTON, self.PrevAncestry )
		self.Anc_ButtonRight.Bind( wx.EVT_BUTTON, self.NextAncestry )
		self.order_ButtonLeft.Bind( wx.EVT_BUTTON, self.ShiftAncestryDown )
		self.Order_ButtonRight.Bind( wx.EVT_BUTTON, self.ShiftAncestryUp )
		self.Colour_ComboBox.Bind( wx.EVT_COMBOBOX, self.SetColour )
		self.SortDom_Button.Bind( wx.EVT_BUTTON, self.SortByAncestryDominance )
		self.Dom_CheckBox.Bind( wx.EVT_CHECKBOX, self.ChangeSortDirection )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FillColours( self, event ):
		event.Skip()
	
	def PrevAncestry( self, event ):
		event.Skip()
	
	def NextAncestry( self, event ):
		event.Skip()
	
	def ShiftAncestryDown( self, event ):
		event.Skip()
	
	def ShiftAncestryUp( self, event ):
		event.Skip()
	
	def SetColour( self, event ):
		event.Skip()
	
	def SortByAncestryDominance( self, event ):
		event.Skip()
	
	def ChangeSortDirection( self, event ):
		event.Skip()
	

