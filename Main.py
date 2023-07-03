from customtkinter import*
from PIL import Image
from Windows import Image_Frame

class Main_Window():
    def __init__(self):       
        self.App = CTk()
        self.App.title("Lyrics Editor")
        self.App.geometry('900x500+250+100')
        self.App.resizable(False,False)

        self.img0 = CTkImage(Image.open("Icons\home.png"),size=(26,26))
        self.img1 = CTkImage(Image.open("Icons\image.png"),size=(26,26))
        self.img1a = CTkImage(Image.open("Icons\image.png"),size=(128,128))
        self.img2 = CTkImage(Image.open("Icons\music.png"),size=(26,26))
        self.img2a = CTkImage(Image.open("Icons\music.png"),size=(128,128))
        self.img3 = CTkImage(Image.open("Icons\close.png"),size=(26,26))

        self.menu_buttons = []
        self.frames = []

        self.Frame = CTkFrame(self.App,width=900,height=500,fg_color="#58001D",corner_radius=0) # "#4F0018"
        self.Frame.place(x=0,y=0)

        self.menubar = CTkFrame(self.Frame,width=45,height=500,fg_color="#790028",corner_radius=0)
        self.menubar.place(x=0,y=0)

        self.home = CTkButton(self.menubar,width=44,height=45,text="",fg_color="#58001D",corner_radius=0,image=self.img0,hover_color="#A00035",state=DISABLED,command= lambda: [self.select_button(self.home),self.home_button()])
        self.home.place(x=0,y=0)
        self.menu_buttons.append(self.home)

        self.image = CTkButton(self.menubar,width=44,height=45,text="",fg_color="#790028",corner_radius=0,image=self.img1,hover_color="#A00035",command= lambda: [self.select_button(self.image),self.Img_Frame.place()])
        self.image.place(x=0,y=45)
        self.menu_buttons.append(self.image)

        self.lyric = CTkButton(self.menubar,width=44,height=45,text="",fg_color="#790028",corner_radius=0,image=self.img2,hover_color="#A00035",command= lambda: self.select_button(self.lyric))
        self.lyric.place(x=0,y=90)
        self.menu_buttons.append(self.lyric)

        self.exit = CTkButton(self.menubar,width=44,height=45,text="",fg_color="#790028",corner_radius=0,image=self.img3,hover_color="#A00035",command= lambda: self.App.destroy())
        self.exit.place(x=0,y=456)

        self.text = CTkLabel(self.Frame,height=80,width=600,text="Lyrics Editor",font=('Times',32),fg_color="#58001D")
        self.text.place(x=125,y=0)

        self.image_frame = CTkFrame(self.Frame,width=250,height=170,corner_radius=7,fg_color="#790028")
        self.image_frame.place(x=100,y=100)
        self.image_frame.bind('<Enter>',lambda event: self.highlight_tool(event,self.image_frame))
        self.image_frame.bind('<Leave>',lambda event: self.unhighlight_tool(event,self.image_frame))

        self.image_1 = CTkLabel(self.image_frame,image=self.img1a,text="",fg_color="#790028")
        self.image_1.place(x=60,y=5)
        self.image_1.bind('<Enter>',lambda event: self.highlight_tool(event,self.image_frame))
        self.image_1.bind('<Leave>',lambda event: self.unhighlight_tool(event,self.image_frame))

        self.text_1 = CTkLabel(self.image_frame,font=('Times',18),text="Convert images to text",width=230,fg_color="#790028")
        self.text_1.place(x=10,y=140)
        self.text_1.bind('<Enter>',lambda event: self.highlight_tool(event,self.image_frame))
        self.text_1.bind('<Leave>',lambda event: self.unhighlight_tool(event,self.image_frame))

        self.lyric_frame = CTkFrame(self.Frame,width=250,height=170,corner_radius=7,fg_color="#790028")
        self.lyric_frame.place(x=360,y=100)
        self.lyric_frame.bind('<Enter>',lambda event: self.highlight_tool(event,self.lyric_frame))
        self.lyric_frame.bind('<Leave>',lambda event: self.unhighlight_tool(event,self.lyric_frame))

        self.image_2 = CTkLabel(self.lyric_frame,image=self.img2a,text="",fg_color="#790028")
        self.image_2.place(x=60,y=5)
        self.image_2.bind('<Enter>',lambda event: self.highlight_tool(event,self.lyric_frame))
        self.image_2.bind('<Leave>',lambda event: self.unhighlight_tool(event,self.lyric_frame))

        self.text_2 = CTkLabel(self.lyric_frame,font=('Times',18),text="Edit lyrics",width=230,fg_color="#790028")
        self.text_2.place(x=10,y=140)
        self.text_2.bind('<Enter>',lambda event: self.highlight_tool(event,self.lyric_frame))
        self.text_2.bind('<Leave>',lambda event: self.unhighlight_tool(event,self.lyric_frame))

        self.Img_Frame = Image_Frame(self.Frame)
        self.frames.append(self.Img_Frame)

        self.App.mainloop()

    def select_button(self,button):
        for i in self.menu_buttons:
            if i == button:
                i.configure(fg_color="#58001D",state=DISABLED)
            else:
                i.configure(fg_color="#790028",state=NORMAL)

    def home_button(self):
        for i in self.frames:
            i.hide()

    def highlight_tool(self,event,frame):
        frame.configure(fg_color="#4F0018")
        for i in frame.winfo_children():
            i.configure(fg_color="#4F0018")

    def unhighlight_tool(self,event,frame):
        frame.configure(fg_color="#790028")
        for i in frame.winfo_children():
            i.configure(fg_color="#790028")

APP = Main_Window()