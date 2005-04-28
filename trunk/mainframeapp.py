#Boa:Frame:Mainframe

import wx
import wx.grid
import getdata
import sqlite

def create(parent):
    return Mainframe(parent)

[wxID_MAINFRAME, wxID_MAINFRAMEBITMAPBUTTON1, wxID_MAINFRAMELISTCTRL1, 
 wxID_MAINFRAMELISTCTRL2, wxID_MAINFRAMESTATICBITMAP1, 
 wxID_MAINFRAMETEXTCTRL1, wxID_MAINFRAMETEXTCTRL2, wxID_MAINFRAMETEXTCTRL3, 
 wxID_MAINFRAMETEXTCTRL4, wxID_MAINFRAMETEXTCTRL5, wxID_MAINFRAMETEXTCTRL6, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Mainframe(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=wx.Menu(), title=u'Aquarium')
        parent.Append(menu=wx.Menu(), title=u'Edition')

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINFRAME, name=u'Mainframe',
              parent=prnt, pos=wx.Point(178, 126), size=wx.Size(794, 599),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self._init_utils()
        self.SetClientSize(wx.Size(786, 571))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_MAINFRAMESTATICBITMAP1, name='staticBitmap1', parent=self,
              pos=wx.Point(16, 56), size=wx.Size(440, 272), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_MAINFRAMETEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(488, 48),
              size=wx.Size(100, 21), style=0, value='textCtrl1')

        self.textCtrl2 = wx.TextCtrl(id=wxID_MAINFRAMETEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(680, 48),
              size=wx.Size(100, 21), style=0, value='textCtrl2')

        self.textCtrl3 = wx.TextCtrl(id=wxID_MAINFRAMETEXTCTRL3,
              name='textCtrl3', parent=self, pos=wx.Point(488, 88),
              size=wx.Size(100, 21), style=0, value='textCtrl3')

        self.textCtrl4 = wx.TextCtrl(id=wxID_MAINFRAMETEXTCTRL4,
              name='textCtrl4', parent=self, pos=wx.Point(680, 88),
              size=wx.Size(100, 21), style=0, value='textCtrl4')

        self.textCtrl5 = wx.TextCtrl(id=wxID_MAINFRAMETEXTCTRL5,
              name='textCtrl5', parent=self, pos=wx.Point(680, 128),
              size=wx.Size(100, 21), style=0, value='textCtrl5')

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_MAINFRAMEBITMAPBUTTON1, name='bitmapButton1', parent=self,
              pos=wx.Point(488, 128), size=wx.Size(24, 24),
              style=wx.BU_AUTODRAW)

        self.listCtrl1 = wx.ListCtrl(id=wxID_MAINFRAMELISTCTRL1,
              name='listCtrl1', parent=self, pos=wx.Point(16, 336),
              size=wx.Size(440, 208), style=wx.LC_ICON)
        db = getdata.query("select * from Popu")
        
        index = 0
        i=0
        #for i in db:
        #    self.listCtrl1.InsertStringItem(index, item[0])
        #    index += 1
        
        self.listCtrl1.InsertStringItem(0, "George")
        self.listCtrl1.SetStringItem(0, 1, "1234ABC")
        self.listCtrl1.SetStringItem(0, 2, "100 Maple Ave.")
        self.listCtrl1.SetStringItem(0, 3, "New York")
        
        #for item in db.fields:
        #    self.listCtrl1.SetColLabelValue(index, item[0])
        #    index += 1
        
for row in range(len(db.data)):
    for col in range(len(db.data[row])):
        values = db.data[row][col] 
        self.grid1.SetCellValue(row,col,str(values))    
        self.listCtrl2 = wx.ListCtrl(id=wxID_MAINFRAMELISTCTRL2,
              name='listCtrl2', parent=self, pos=wx.Point(464, 336),
              size=wx.Size(320, 224), style=wx.LC_ICON)

        self.textCtrl6 = wx.TextCtrl(id=wxID_MAINFRAMETEXTCTRL6,
              name='textCtrl6', parent=self, pos=wx.Point(464, 160),
              size=wx.Size(320, 168), style=wx.TE_MULTILINE, value='textCtrl6')

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        
    
