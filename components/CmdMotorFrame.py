import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from globalParams import g


class CmdMotorFrame(tb.LabelFrame):
  def __init__(self, parentFrame, motorNo):
    super().__init__(master=parentFrame, borderwidth=5, bootstyle='secondary')

    self.motorNo = motorNo
    self.frame = tb.Frame(self)

    # create widgets
    self.text = tb.Label(self.frame, text="MANUAL MOTOR CONTROL", font=('Monospace',12, 'bold') ,bootstyle="danger")
      
    buttonStyle = tb.Style()
    buttonStyleName = 'primary.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',12,'bold'))
    self.leftButton = tb.Button(self.frame, text="<|", style=buttonStyleName)
    self.rightButton = tb.Button(self.frame, text="|>", style=buttonStyleName)

    # Bind the Mouse events with the Handler
    self.leftButton.bind('<ButtonPress-1>', self.startForwardCommand)
    self.leftButton.bind('<ButtonRelease-1>', self.stopForwardCommand)

    self.rightButton.bind('<ButtonPress-1>', self.startReverseCommand)
    self.rightButton.bind('<ButtonRelease-1>', self.stopReverseCommand)

    # add widgets to Frames
    self.text.pack(side='left', fill='both', padx=(80,10))
    self.leftButton.pack(side='left', padx=(10,2))
    self.rightButton.pack(side='left', padx=(2,10))


    self.frame.pack(side='left', expand=True, fill='both')

  def startForwardCommand(self, e):
    # print("start forward command")
    if self.motorNo == 0:
      if int(g.motorDirConfig[self.motorNo]) == 1:
        isSuccess = g.serClient.send("/pwm", g.motorTestPwm[self.motorNo], 0)
      elif int(g.motorDirConfig[self.motorNo]) == -1:
        isSuccess = g.serClient.send("/pwm", -g.motorTestPwm[self.motorNo], 0)
    elif self.motorNo == 1:
      if int(g.motorDirConfig[self.motorNo]) == 1:
        isSuccess = g.serClient.send("/pwm", 0, g.motorTestPwm[self.motorNo])
      elif int(g.motorDirConfig[self.motorNo]) == -1:
        isSuccess = g.serClient.send("/pwm", 0, -g.motorTestPwm[self.motorNo])

  def stopForwardCommand(self, e):
    # print("stop forward command")
    isSuccess = g.serClient.send("/pwm", 0, 0)

  def startReverseCommand(self, e):
    # print("start reverse command")
    if self.motorNo == 0:
      if int(g.motorDirConfig[self.motorNo]) == 1:
        isSuccess = g.serClient.send("/pwm", -g.motorTestPwm[self.motorNo], 0)
      elif int(g.motorDirConfig[self.motorNo]) == -1:
        isSuccess = g.serClient.send("/pwm", g.motorTestPwm[self.motorNo], 0)
    elif self.motorNo == 1:
      if int(g.motorDirConfig[self.motorNo]) == 1:
        isSuccess = g.serClient.send("/pwm", 0, -g.motorTestPwm[self.motorNo])
      elif int(g.motorDirConfig[self.motorNo]) == -1:
        isSuccess = g.serClient.send("/pwm", 0, g.motorTestPwm[self.motorNo])

  def stopReverseCommand(self, e):
    # print("stop reverse command")
    isSuccess = g.serClient.send("/pwm", 0, 0)
    



# motorCommandButton.pack(side="top", fill="x", padx=(100,100), pady=(20,50))
