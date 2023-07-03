from customtkinter import*
from PIL import Image
from Selection_window import Selection_window

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

        self.Frame = CTkFrame(self.App,width=900,height=500,fg_color="#58001D",corner_radius=0) # "#4F0018"
        self.Frame.place(x=0,y=0)

        self.menubar = CTkFrame(self.Frame,width=45,height=500,fg_color="#790028",corner_radius=0)
        self.menubar.place(x=0,y=0)

        self.home = CTkButton(self.menubar,width=44,height=45,text="",fg_color="#790028",corner_radius=0,image=self.img0,hover_color="#A00035",command= lambda: self.App.destroy())
        self.home.place(x=0,y=0)
        self.menu_buttons.append(self.home)

        self.image = CTkButton(self.menubar,width=44,height=45,text="",fg_color="#790028",corner_radius=0,image=self.img1,hover_color="#A00035",command= lambda: self.App.destroy())
        self.image.place(x=0,y=46)
        self.menu_buttons.append(self.image)

        self.lyric = CTkButton(self.menubar,width=44,height=45,text="",fg_color="#790028",corner_radius=0,image=self.img2,hover_color="#A00035",command= lambda: self.App.destroy())
        self.lyric.place(x=0,y=92)
        self.menu_buttons.append(self.lyric)

        self.exit = CTkButton(self.menubar,width=44,height=45,text="",fg_color="#790028",corner_radius=0,image=self.img3,hover_color="#A00035",command= lambda: self.App.destroy())
        self.exit.place(x=0,y=456)

        self.text = CTkLabel(self.Frame,height=80,width=600,text="Lyrics Editor",font=('Times',32),fg_color="#58001D")
        self.text.place(x=125,y=0)

        self.image_frame = CTkFrame(self.Frame,width=250,height=170,corner_radius=7,fg_color="#790028")
        self.image_frame.place(x=100,y=100)

        self.image_1 = CTkLabel(self.image_frame,image=self.img1a,text="",fg_color="#790028")
        self.image_1.place(x=60,y=5)

        self.text_1 = CTkLabel(self.image_frame,font=('Times',18),text="Convert images to text",width=230,fg_color="#790028")
        self.text_1.place(x=10,y=140)

        self.lyric_frame = CTkFrame(self.Frame,width=250,height=170,corner_radius=7,fg_color="#790028")
        self.lyric_frame.place(x=360,y=100)

        self.image_1 = CTkLabel(self.lyric_frame,image=self.img2a,text="",fg_color="#790028")
        self.image_1.place(x=60,y=5)

        self.text_1 = CTkLabel(self.lyric_frame,font=('Times',18),text="Edit lyrics",width=230,fg_color="#790028")
        self.text_1.place(x=10,y=140)

        self.screenshot_window = Selection_window(self.App)

        self.App.mainloop()

    def op(self):
        self.screenshot_window.create_window()

# App = CTk()
# sc = Selection_window(App)
# sc.create_window()

# App.mainloop()
APP = Main_Window()