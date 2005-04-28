# -*- coding: utf-8 -*-

import wx
from wxPython.wx import *
import time
import types
import getdata

#############################################################
# procédure des messagebox ##################################
#############################################################
from wxPython.wx import wxApp, wxMessageDialog, wxDefaultPosition, NULL, \
                        wxOK, wxCANCEL, wxYES_NO, wxYES, wxNO, wxNO_DEFAULT, \
                        wxCENTRE, wxICON_HAND, \
                        wxICON_QUESTION, wxICON_INFORMATION, \
                        wxID_OK, wxID_CANCEL, wxID_YES, wxID_NO

from string import upper, find


class _App(wxApp):
    def OnInit(self):
        return 1

    def __del__(self):
        self.MainLoop()
        wxApp.__del__(self)

def _GetApp():
    try:
        return _App(0)
    except:
        return None

class MessageBox:
    style_info={
                'wxOK': wxOK,
                'wxCANCEL': wxCANCEL,
                'wxYES_NO': wxYES_NO,
                'wxNO': wxNO,
                'wxYES': wxYES,
                'wxNO_DEFAULT': wxNO_DEFAULT,
                'wxCENTRE': wxCENTRE,
                'wxICON_HAND': wxICON_HAND,
                'wxICON_QUESTION': wxICON_QUESTION,
                'wxICON_INFORMATION':  wxICON_INFORMATION,
                'OK': wxOK,
                'CANCEL': wxCANCEL,
                'YES_NO': wxYES_NO,
                'YESNO': wxYES_NO,
                'NO': wxNO,
                'YES': wxYES,
                'NO_DEFAULT': wxNO_DEFAULT,
                'CENTRE': wxCENTRE,
                'ICON_HAND': wxICON_HAND,
                'ICON_QUESTION': wxICON_QUESTION,
                'ICON_INFORMATION':  wxICON_INFORMATION,
                'HAND': wxICON_HAND,
                'QUESTION': wxICON_QUESTION,
                'INFORMATION':  wxICON_INFORMATION
                }

    retval = {wxID_OK: 'ok', wxID_CANCEL: 'cancel', wxID_YES: 'yes', wxID_NO: 'no'}

    def __init__(self,caption='',pos=wxDefaultPosition,style=wxOK | wxICON_INFORMATION):
        self.caption = caption
        self.pos = pos
        if type(style)==type(''):
            s = upper(style)
            try:
                style=eval(s)
            except:
                style = 0
                for i in self.style_info.keys():
                    if find(s,i)>=0:
                        style = style | self.style_info[i]

        self.style = style

    
    def show(self,msg):
        app = _GetApp()
        dlg = wxMessageDialog(NULL, msg, self.caption,self.style,self.pos)
        val = dlg.ShowModal()
        dlg.Destroy()
        return self.retval[val]

#############################################################
#############################################################


