# taken from https://github.com/janbodnar/wxPython-examples/blob/master/widgets/button_wid.py

import wx

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        closeButton = wx.Button(pnl, label='Close', pos=(20, 20))
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

        testButton = wx.Button(pnl, label="Click Me!", pos = (20,50))
        testButton.Bind(wx.EVT_BUTTON, self.onClick)
        
        self.SetSize((350, 250))
        self.SetTitle('wx.Button')
        self.Centre()

    def OnClose(self, e):
        self.Close(True)

    def onClick(self, e):
        print(e)
        

def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
