#!/usr/bin/env python2
import sys
import wx
import wx.html2


def run(url):
    app = wx.App(False)
    frm = wx.Frame(None, title=url, style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP, size=(300, 480))

    wv = wx.html2.WebView.New(frm)
    wv.LoadURL(url)

    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(wv, 1, wx.EXPAND)
    frm.SetSizer(sizer)
    frm.SetMenuBar(wx.MenuBar())
    frm.Center()
    frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    run(sys.argv[1])
