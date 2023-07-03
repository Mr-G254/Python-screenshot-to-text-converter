from customtkinter import*
from PIL import Image

class Image_Frame():
    def __init__(self,frame):
        self.master = frame

        self.img0 = CTkImage(Image.open("Icons\\ad_image.png"),size=(22,22))
        self.img1 = CTkImage(Image.open("Icons\capture.png"),size=(23,23))

        self.Frame = CTkFrame(self.master,width=854,height=500,fg_color="#58001D",corner_radius=0)

        self.text = CTkLabel(self.Frame,text="Convert images to text(Lyrics)",width=900,height=40,fg_color="#58001D",font=('Times',17))
        self.text.place(x=-46,y=0)

        self.browse = CTkButton(self.Frame,width=140,height=32,text="Browse",anchor=W,font=('Times',14),image=self.img0,compound=LEFT,fg_color="#4F0018",border_width=0,border_color="#790028",corner_radius=6)
        self.browse.place(x=265,y=50)
        self.browse.bind('<Enter>', lambda event: self.highlight_button(event,self.browse))
        self.browse.bind('<Leave>', lambda event: self.unhighlight_button(event,self.browse))

        self.screen = CTkButton(self.Frame,width=140,height=32,text="Screenshot",anchor=E,font=('Times',14),image=self.img1,compound=RIGHT,fg_color="#4F0018",border_width=0,border_color="#790028",corner_radius=6)
        self.screen.place(x=410,y=50)
        self.screen.bind('<Enter>', lambda event: self.highlight_button(event,self.screen))
        self.screen.bind('<Leave>', lambda event: self.unhighlight_button(event,self.screen))

    def place(self):
        self.Frame.place(x=46,y=0)

    def hide(self):
        self.Frame.place_forget()

    def highlight_button(self,event,button):
        button.configure(border_width=2)

    def unhighlight_button(self,event,button):
        button.configure(border_width=0)