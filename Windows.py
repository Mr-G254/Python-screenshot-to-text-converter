from customtkinter import*
from PIL import Image

class Image_Frame():
    def __init__(self,frame):
        self.master = frame

        self.img0 = CTkImage(Image.open("Icons\\ad_image.png"),size=(22,22))
        self.img1 = CTkImage(Image.open("Icons\capture.png"),size=(23,23))
        self.img2 = CTkImage(Image.open("Icons\copy.png"),size=(23,23))
        self.img3 = CTkImage(Image.open("Icons\clear.png"),size=(23,23))
        self.img4 = CTkImage(Image.open("Icons\convert.png"),size=(23,23))
        self.img5 = CTkImage(Image.open("Icons\\next.png"),size=(22,22))

        self.Frame = CTkFrame(self.master,width=1054,height=600,fg_color="#58001D",corner_radius=0)

        self.text = CTkLabel(self.Frame,text="Convert images to text(Lyrics)",width=1100,height=40,fg_color="#58001D",font=('Times',19))
        self.text.place(x=-46,y=0)

        self.browse = CTkButton(self.Frame,width=140,height=32,text="Browse",anchor=W,font=('Times',16),image=self.img0,compound=LEFT,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6)
        self.browse.place(x=67,y=40)

        self.screen = CTkButton(self.Frame,width=140,height=32,text="Screenshot",anchor=E,font=('Times',16),image=self.img1,compound=RIGHT,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6)
        self.screen.place(x=212,y=40)
       
        self.frame_1  = CTkFrame(self.Frame,width=400,height=510,fg_color="#790028",corner_radius=10)
        self.frame_1.place(x=12,y=80)

        self.text_1 = CTkLabel(self.frame_1,text="Images",width=390,height= 25,fg_color="#790028",font=('Times',18))
        self.text_1.place(x=5,y=5)

        img_frame = CTkScrollableFrame(self.frame_1,width=370,height=455,fg_color="#4F0018",corner_radius=10)
        img_frame.place(x=2,y=33)

        self.copy = CTkButton(self.Frame,width=120,height=32,text="Copy",anchor=W,font=('Times',16),compound=LEFT,image=self.img2,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6)
        self.copy.place(x=760,y=40)

        self.clear = CTkButton(self.Frame,width=120,height=32,text="Clear",anchor=E,font=('Times',16),compound=RIGHT,image=self.img3,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6)
        self.clear.place(x=885,y=40)

        self.frame_2  = CTkFrame(self.Frame,width=320,height=510,fg_color="#790028",corner_radius=10)
        self.frame_2.place(x=720,y=80)

        self.text_2 = CTkLabel(self.frame_2,text="Text",width=310,height= 25,fg_color="#790028",font=('Times',18))
        self.text_2.place(x=5,y=5)

        self.lyr_frame = CTkFrame(self.frame_2,width=316,height=475,fg_color="#4F0018",corner_radius=10)
        self.lyr_frame.place(x=2,y=33)

        self.text_area = CTkTextbox(self.lyr_frame,width=311,height=465,font=('Times',19),wrap='word',border_spacing=0,fg_color="#4F0018",corner_radius=10)
        self.text_area.place(x=2,y=2)

        self.conv = CTkButton(self.Frame,width=150,height=32,text="Convert",font=('Times',16),compound=RIGHT,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6)
        self.conv.place(x=491,y=521)

        self.next = CTkButton(self.Frame,width=150,height=32,text="Next",font=('Times',16),compound=RIGHT,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6)
        self.next.place(x=491,y=558)

    def place(self):
        self.Frame.place(x=46,y=0)

    def hide(self):
        self.Frame.place_forget()
