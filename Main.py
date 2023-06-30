from customtkinter import*
from Selection_window import Selection_window

class Main_Window():
    def __init__(self):       
        self.App = CTk()
        self.App.title("Screenshot to Text")
        self.App.geometry('900x500+250+100')
        self.App.resizable(False,False)

        self.Frame = CTkFrame(self.App,width=900,height=500,fg_color="#032C58") # "#4F0018"
        self.Frame.place(x=0,y=0)

        self.topbar = CTkFrame(self.Frame,width=300,height=40,border_width=0,border_color="#351100",corner_radius=8)
        self.topbar.place(x=300,y=5)

        self.screenshot_window = Selection_window(self.App)

        self.App.mainloop()

    def op(self):
        self.screenshot_window.create_window()

App = CTk()
sc = Selection_window(App)
sc.create_window()

App.mainloop()