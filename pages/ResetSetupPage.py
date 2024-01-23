import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

from globalParams import g





# class DriverParamsSetupFrame(customtkinter.CTkFrame):
#   def __init__(self, parent):
#     super().__init__(parent, width=500, height=700)

#     # add heading
#     self.heading = customtkinter.CTkLabel(self, text="OTHER PARAMS SETUP", font=customtkinter.CTkFont(size=24, weight="bold", underline=False))
#     self.heading.grid(row=0, column=0, padx=10, pady=(5,25))

#     # add set card frame for i2c settings
#     g.i2cAddress = int(g.serClient.get("i2c"))
#     self.setPwmCardFrame = SetDataCardFrame(self, "I2C_ADDRESS", g.i2cAddress,
#                                             placeHolderText="enter I2C_ADDRESS",
#                                             inputBoxWidth=200, set_func=setI2Caddress)
#     self.setPwmCardFrame.grid(row=1, column=0, pady=20)

#     # add reset button
#     self.resetButton = customtkinter.CTkButton(self, text="RESET ALL PARAMETERS", font=customtkinter.CTkFont(size=12, weight="bold"),
#                                                    fg_color='#9BABB8', text_color='black', hover_color='#EEEEEE',
#                                                    command=self.open_reset_dialog_event)
#     self.resetButton.grid(row=2, column=0, pady=(50, 20), padx=10, ipadx=10, ipady=10)


#   def open_reset_dialog_event(self):
#     dialog = customtkinter.CTkInputDialog(text="This will reset all parameters to default.\nEnter 'reset' to continue", title="RESET WARNING!!!")
#     val = dialog.get_input()
#     if val == "reset":
#       isSuccessful = resetAllParams()
#       if isSuccessful:
#         # print(isSuccessful)
#         tkinter.messagebox.showinfo("showinfo", "SUCCESS:\n\nParameters Reset was successful.\n\nRestart gui application\n\nReset controller with the reset button\nor turn off and on the controller")
#       else:
#         tkinter.messagebox.showerror("showerror", "ERROR:\n\nSomething went wrong\nAttempt to reset was unsuccessful\nTry again")




class ResetSetupFrame(tk.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)

    self.label = tb.Label(self, text="RESET ALL PARAMETERS", font=('Monospace',16, 'bold') ,bootstyle="dark")
    self.frame = tb.Frame(self)

    #create widgets to be added to frame1
    buttonStyle = tb.Style()
    buttonStyleName = 'primary.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',10,'bold'))
    self.resetButton = tb.Button(self.frame, text="RESET ALL PARAMETERS",
                               style=buttonStyleName, padding=20,
                               command=self.open_reset_dialog_event)

    #add framed widgets to frame
    self.resetButton.pack(side='top', expand=True, fill="both")

    #add frame1, frame2 and frame3 to MainFrame
    self.label.pack(side="top", fill="x", padx=(220,0), pady=(5,0))
    self.frame.place(relx=0.5, rely=0.5, anchor="center")


  def open_reset_dialog_event(self):
    dialog = Messagebox.show_question(title="RESET WARNING!!!", message="This will reset all parameters on the controller's EEPROM to default.\nAre you sure you want to continue?")

    if dialog == "Yes":
      isSuccessful = self.resetAllParams()
      if isSuccessful:
        Messagebox.show_info("SUCCESS:\n\nParameters Reset was successful.\n\nRestart gui application\n\nReset controller with the reset button\nor turn off and on the controller", "SUCCESS")
      else:
        Messagebox.show_error("ERROR:\n\nSomething went wrong\nAttempt to reset was unsuccessful\nTry again", "ERROR")


  def resetAllParams(self):
    isSuccessful = g.serClient.send("reset")
    return isSuccessful
