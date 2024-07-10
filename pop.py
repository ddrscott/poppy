#!/usr/bin/env pythonw
import click
import wx
import wx.html2

@click.command()
@click.argument('url')
@click.option('--height', default=800, help='Height of the window')
@click.option('--width', default=480, help='Width of the window')
def run(url, height, width):
    app = wx.App(False)
    frm = wx.Frame(
        None,
        title=url,
        style=wx.DEFAULT_FRAME_STYLE,
        size=(width, height)
    )

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
    run()
