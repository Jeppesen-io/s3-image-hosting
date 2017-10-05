#!/usr/bin/env python
import wx, sys

class FooApp(wx.App):

	# called when the 'change' button is pressed
	def changeImage(self,event):
		img = wx.Image("foo.jpg")
		self.image = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img))

	def __init__(self):
		# setup code for the window
		wx.App.__init__(self)
		self.frame = wx.Frame(None, title='Demo')
		self.panel = wx.Panel(self.frame)

		# load an image
		img = wx.Image(sys.argv[1])
		self.image = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img))

		# create a Sizer to hold one (or more) button
		self.buttons = wx.BoxSizer(wx.VERTICAL)
		self.changeButton = wx.Button(self.panel, -1, "Change")
		self.changeButton.Bind(wx.EVT_BUTTON,self.changeImage)
		self.buttons.Add(self.changeButton)

		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.mainSizer.Add(self.image)
		self.mainSizer.Add(self.buttons)

		# more generic setupcode
		self.panel.SetSizer(self.mainSizer)
		self.mainSizer.Fit(self.frame)
		self.panel.Layout()
		self.frame.Show(True)

if __name__ == '__main__':
    app = FooApp()
    app.MainLoop()
