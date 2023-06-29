from customtkinter import*
from PIL import Image,ImageGrab

class Selection_window():
    def __init__(self,app):
        self.App = app

    def create_window(self):
        self.Window = CTkToplevel(fg_color="White")
        self.Window.state("zoomed")
        self.Window.overrideredirect(True)
        self.Window.wm_attributes("-alpha",0.2)
        self.Window.grab_set()
        self.Window.bind('<Escape>',lambda event: self.exit(event))

        self.canvas = CTkCanvas(self.Window,height=self.Window.winfo_height(),width=self.Window.winfo_width())
        self.canvas.place(x=0,y=0)
        self.canvas.bind('<Button-1>',lambda event: self.select_area(event))

        self.App.iconify()

    def select_area(self,event):
        if self.area_is_selected():
            self.delete_selected_area()

        self.x_pos = event.x
        self.y_pos = event.y
        self.rect = self.canvas.create_rectangle(event.x,event.y,event.x,event.y,width=3) 

        self.canvas.bind('<Motion>',lambda event: self.resize_area(event)) 

    def resize_area(self,event):
        self.canvas.coords(self.rect,self.x_pos,self.y_pos,event.x,event.y)

    def area_is_selected(self):
        try:
            self.canvas.coords(self.rect)
            return True
        
        except:
            return False
        
    def delete_selected_area(self):
        self.canvas.delete(self.rect)

    def exit(self,event):
        self.Window.destroy()
        self.App.deiconify()
