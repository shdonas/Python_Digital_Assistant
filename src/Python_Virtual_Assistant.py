import wx

# importing class
from src import PVA_Frame

if __name__ == '__main__':
    myFrame = PVA_Frame.MyFrame

    app = wx.App(True)
    frame = myFrame()
    app.MainLoop()
