#Boa:MiniFrame:MiniFramedetailpoisson

import wx

def create(parent):
    return MiniFramedetailpoisson(parent)

[wxID_MINIFRAMEDETAILPOISSON] = [wx.NewId() for _init_ctrls in range(1)]

class MiniFramedetailpoisson(wx.MiniFrame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MiniFrame.__init__(self, id=wxID_MINIFRAMEDETAILPOISSON,
              name=u'MiniFramedetailpoisson', parent=prnt, pos=wx.Point(337,
              186), size=wx.Size(400, 490), style=wx.DEFAULT_FRAME_STYLE,
              title=u'DETAIL DU POISSON')
        self.SetClientSize(wx.Size(392, 462))

    def __init__(self, parent):
        self._init_ctrls(parent)
