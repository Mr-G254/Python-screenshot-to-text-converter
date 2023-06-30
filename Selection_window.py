from customtkinter import*
from PIL import Image,ImageGrab
from time import sleep

class Selection_window():
    def __init__(self,app):
        self.App = app

    def create_window(self):
        self.App.iconify()
        self.Window = CTkToplevel(self.App,fg_color="White")
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
        self.canvas.bind('<Return>',lambda event: self.get_screenshot(event))

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

    def get_screenshot(self,event):
        if self.canvas.coords(self.rect):
            self.coordinates = self.canvas.coords(self.rect)
            self.Window.destroy()
            self.App.iconify()

            sleep(1)

            self.screenshot = ImageGrab.grab()
            self.crop = self.screenshot.crop(self.coordinates)
            self.crop.save("image.png")

            self.App.deiconifiy()

    def exit(self,event):
        self.Window.destroy()
        self.App.deiconify()
