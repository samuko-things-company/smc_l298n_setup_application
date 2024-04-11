import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from pages.I2CSetupPage import I2CSetupFrame
from pages.ResetSetupPage import ResetSetupFrame
from pages.EncSetupPage import EncSetupFrame
from pages.PidSetupPage import PidSetupFrame




class MainAppFrame(tb.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)


    # SIDEBAR NAVIGATION FRAME
    self.sideNavFrame = tb.LabelFrame(self, borderwidth=10)

    # MIAN CONTENT FRAME
    self.mainContentFrame = tb.Frame(self)


    #create widgets to be added to the sideNavFrame
    self.label = tb.Label(self.sideNavFrame, text="MENU", font=('Monospace',20, 'bold') ,bootstyle="secondary")

    buttonStyle = tb.Style()
    buttonStyleName = 'primary.Link.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',12, 'bold'))

    self.button1 = tb.Button(self.sideNavFrame, text="MOTOR A ENC", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button1, self.displayMotorAEncSetupPage))
    
    self.button2 = tb.Button(self.sideNavFrame, text="MOTOR A PID", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button2, self.displaymotorAPidSetupPage))
    
    self.button3 = tb.Button(self.sideNavFrame, text="MOTOR B ENC", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button3, self.displayMotorBEncSetupPage))
    
    self.button4 = tb.Button(self.sideNavFrame, text="MOTOR B PID", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button4, self.displaymotorBPidSetupPage))
    
    self.button5 = tb.Button(self.sideNavFrame, text="I2C SETUP", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button5, self.displayI2CSetupPage))
    
    self.button6 = tb.Button(self.sideNavFrame, text="RESET PARAMS", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button6, self.displayResetPage))
    
    
    # add widget to sideNavFrame
    self.label.pack(side="top", fill="x", padx=(40,0), pady=(0,25))
    self.button1.pack(side="top", fill="x", padx=5, pady=10)
    self.button2.pack(side="top", fill="x", padx=5, pady=(10,35))
    self.button3.pack(side="top", fill="x", padx=5, pady=10)
    self.button4.pack(side="top", fill="x", padx=5, pady=(10,35))
    self.button5.pack(side="top", fill="x", padx=5, pady=10)
    self.button6.pack(side="top", fill="x", padx=5, pady=10)


    
    ############Initialize the mainContentFrame ################
    self.displayPage(self.button6, self.displayResetPage)
    ############################################################


    #add framed widgets to MainAppFrame
    self.sideNavFrame.pack(side="left", fill="y", padx=10)
    self.mainContentFrame.pack(side="left", expand=True, fill="both", padx=5)


  
  def enable_all_nav_buttons(self):
    self.button1.configure(state="normal")
    self.button2.configure(state="normal")
    self.button3.configure(state="normal")
    self.button4.configure(state="normal")
    self.button5.configure(state="normal")
    self.button6.configure(state="normal")
  
  def displayPage(self, button, page):
    self.enable_all_nav_buttons()
    button.configure(state='disabled') # disable the clicked nav button
    self.delete_pages()
    page()

  def delete_pages(self):
    for frame in self.mainContentFrame.winfo_children():
      frame.destroy()


  def displayResetPage(self):
    self.resetFrame = ResetSetupFrame(self.mainContentFrame)
    self.resetFrame.pack(side="left", expand=True, fill="both")
  
  def displayI2CSetupPage(self):
    self.i2cSetupFrame = I2CSetupFrame(self.mainContentFrame)
    self.i2cSetupFrame.pack(side="left", expand=True, fill="both")
  
  def displayMotorAEncSetupPage(self):
    self.motorAEncSetupFrame = EncSetupFrame(self.mainContentFrame, motorNo=0)
    self.motorAEncSetupFrame.pack(side="left", expand=True, fill="both")

  def displayMotorBEncSetupPage(self):
    self.motorBEncSetupFrame = EncSetupFrame(self.mainContentFrame, motorNo=1)
    self.motorBEncSetupFrame.pack(side="left", expand=True, fill="both")

  def displaymotorAPidSetupPage(self):
    self.motorAPidSetupFrame = PidSetupFrame(self.mainContentFrame, motorNo=0)
    self.motorAPidSetupFrame.pack(side="left", expand=True, fill="both")

  def displaymotorBPidSetupPage(self):
    self.motorBPidSetupFrame = PidSetupFrame(self.mainContentFrame, motorNo=1)
    self.motorBPidSetupFrame.pack(side="left", expand=True, fill="both")