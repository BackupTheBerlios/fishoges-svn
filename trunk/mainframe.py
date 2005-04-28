#Boa:Frame:Mainframe

import wx
import wx.grid
import getdata
import sqlite
import globalfunc
import  wx.lib.dialogs

def create(parent):
    return Mainframe(parent)

[wxID_MAINFRAME, wxID_MAINFRAMEBITMAPBUTTON1, wxID_MAINFRAMELISTCTRL1, 
 wxID_MAINFRAMELISTCTRL2, wxID_MAINFRAMESTATICBITMAP1, 
 wxID_MAINFRAMETEXTCTRL1, wxID_MAINFRAMETEXTCTRL2, wxID_MAINFRAMETEXTCTRL3, 
 wxID_MAINFRAMETEXTCTRL4, wxID_MAINFRAMETEXTCTRL5, wxID_MAINFRAMETEXTCTRL6, 
] = [wx.NewId() for _init_ctrls in range(11)]


[wxID_MAINFRAMEMENUFISHAJOUTERPOISSON] = [wx.NewId() for _init_coll_menuFISH_Items in range(1)]

class Mainframe(wx.Frame):
    def _init_coll_menuBarGEN_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFISH, title=u'Poissons')
        parent.Append(menu=wx.Menu(), title=u'Plantes')

    def _init_coll_menuFISH_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Ajouter un poisson',
              id=wxID_MAINFRAMEMENUFISHAJOUTERPOISSON, kind=wx.ITEM_NORMAL,
              text=u'Ajouter un poisson')
        self.Bind(wx.EVT_MENU, self.OnMenuPOISSONSAjouterpoissonMenu,
              id=wxID_MAINFRAMEMENUFISHAJOUTERPOISSON)

    def _init_utils(self):
        # generated method, don't edit
        self.menuFISH = wx.Menu(title=u'')

        self.menuBarGEN = wx.MenuBar()

        self._init_coll_menuFISH_Items(self.menuFISH)
        self._init_coll_menuBarGEN_Menus(self.menuBarGEN)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINFRAME, name=u'Mainframe',
              parent=prnt, pos=wx.Point(429, 161), size=wx.Size(794, 599),
              style=wx.DEFAULT_FRAME_STYLE, title=u'FishOges')
        self._init_utils()
        self.SetClientSize(wx.Size(786, 571))
        self.SetIcon(wx.Icon(u'fish.ico', wx.BITMAP_TYPE_ICO))
        self.SetStatusBarPane(0)
        self.SetMenuBar(self.menuBarGEN)

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
              name='listCtrl1', parent=self, pos=wx.Point(8, 336),
              size=wx.Size(440, 192), style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.listCtrl1.SetAutoLayout(True)
        self.listCtrl1.Bind(wx.EVT_LIST_COL_CLICK, self.OnListCtrl1ListColClick,
              id=wxID_MAINFRAMELISTCTRL1)
        self.listCtrl1.Bind(wx.EVT_LEFT_DCLICK, self.OnListCtrl1LeftDclick)
        self.listCtrl1.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnListCtrl1ListItemSelected, id=wxID_MAINFRAMELISTCTRL1)

        self.listCtrl2 = wx.ListCtrl(id=wxID_MAINFRAMELISTCTRL2,
              name='listCtrl2', parent=self, pos=wx.Point(464, 336),
              size=wx.Size(320, 208), style=wx.LC_ICON)

        self.textCtrl6 = wx.TextCtrl(id=wxID_MAINFRAMETEXTCTRL6,
              name='textCtrl6', parent=self, pos=wx.Point(464, 160),
              size=wx.Size(320, 168), style=wx.TE_MULTILINE, value='textCtrl6')

    def __init__(self, parent):
        self._init_ctrls(parent)
        #self._init_utils(parent)
        #self.lig_donnees = ()

       
        
        db = getdata.query("select nom,nom_commun,male,femelle from Popu")
        index = 0
        i=0
        self.listCtrl1.Show(True)
       
        nop=0
        taillefish=(195,120,40,40,40)
        for item in db.fields:
            nop=nop+1
            self.listCtrl1.InsertColumn(index,item[0].replace("_"," "),width=taillefish[(nop-1)])
            index += 1
        self.listCtrl1.InsertColumn((index+1), "Total",width=taillefish[(nop)])
        nop=0
        nopold=9
        for row in range(len(db.data)):
            nop=nop+1
            for col in range(len(db.data[row])):
                values = db.data[row][col] 
                if nop!=nopold :
                    nopold=nop
                    self.listCtrl1.InsertStringItem((nop-1), str(values))
                else:
                    self.listCtrl1.SetStringItem(row, col, str(values))
   
            self.listCtrl1.SetStringItem(row, (col+1), str(values+db.data[row][(col-1)]))    

    def OnMenuPOISSONSAjouterpoissonMenu(self, event):
        event.Skip()

    def OnListCtrl1ListColClick(self, event):
        #quand on clique sur les title de la liste de poissons.
        event.Skip()

    def OnListCtrl1LeftDclick(self, event):        
        #nomfiche = globalfunc.Fiche(self,"poisson",self.lig_donnees)
        donn = self.lig_donnees
        requete = "SELECT nom , descripteur , famille , synonyme , taille , origine , temperature , PH , durete , zone , description , vie , comportement , reproduction , dimorphisme , url FROM Fiche_POISSON WHERE nom LIKE '" + donn + "'"
        db = getdata.query(requete)
        donnees = db.data
        msg="\n"
        nop=0
        for item in db.fields:
            msg=msg + item[0].replace("_"," ") + " : "
            try:
                msg=msg +  donnees[0][nop] 
            except :
                msg=msg + "\n"   
            nop=nop+1
            msg=msg + "\n\n"

        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "Fiche du Poisson")
        dlg.Show()
        

        #self.main = MiniFramedetailpoisson.create(None)
        #self.main.Show()
        #self.SetTopWindow(self.main)
        #event.Skip()

    def OnListCtrl1ListItemSelected(self, event):
        #print "selected"
        self.item_courant = event.m_itemIndex
        #self.lig_donnees = donnees[self.item_courant]['nom']
        db = getdata.query("select nom from Popu")
        #print db.data[self.item_courant]['nom']
        self.lig_donnees = db.data[self.item_courant]['nom']
                           
        #event.Skip()
        
        
 
