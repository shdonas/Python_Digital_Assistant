import wx

# importing class
from src import PVA_GUI

if __name__ == '__main__':
    myFrame = PVA_GUI.MyFrame

    app = wx.App(True)
    frame = myFrame()
    app.MainLoop()
