from customtkinter import*
from tkinter import filedialog,ttk,font
from PIL import Image
from Tools import Image_to_text,Screenshot
import pyperclip as pc

class Splash_Frame():
    def __init__(self,app):
        app.configure(fg_color="#58001D")
        app.geometry('600x200+400+200')
        app.overrideredirect(True)

        self.label = CTkLabel(app,width=600,height=200,text="Lyrics Editor v2.0",font=('Times',35))
        self.label.place(x=0,y=0)
        app.update()
        app.tkraise()


class Image_Frame():
    def __init__(self,frame,app):
        self.Image_converter = Image_to_text()

        self.master = frame
        self.App = app

        self.img0 = CTkImage(Image.open("Icons\\ad_image.png"),size=(22,22))
        self.img1 = CTkImage(Image.open("Icons\capture.png"),size=(23,23))
        self.img2 = CTkImage(Image.open("Icons\copy.png"),size=(23,23))
        self.img3 = CTkImage(Image.open("Icons\clear.png"),size=(23,23))
        self.img4 = CTkImage(Image.open("Icons\convert.png"),size=(23,23))
        self.img5 = CTkImage(Image.open("Icons\\next.png"),size=(22,22))

        self.Row = 0
        self.Screenshot = Screenshot(app,self.add_image)
        self.check_boxes = []
        self.all_images = []
        self.selected_images = []

        self.Frame = CTkFrame(self.master,width=1054,height=600,fg_color="#58001D",corner_radius=0)

        self.text = CTkLabel(self.Frame,text="Convert images to text(Lyrics)",width=1100,height=40,fg_color="#58001D",font=('Times',19))
        self.text.place(x=-46,y=0)

        self.browse = CTkButton(self.Frame,width=140,height=32,text="Browse",anchor=W,font=('Times',16),image=self.img0,compound=LEFT,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6,command=self.browse_file)
        self.browse.place(x=67,y=40)

        self.screen = CTkButton(self.Frame,width=140,height=32,text="Screenshot",anchor=E,font=('Times',16),image=self.img1,compound=RIGHT,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6,command=self.get_screenshot)
        self.screen.place(x=212,y=40)
       
        self.frame_1  = CTkFrame(self.Frame,width=400,height=510,fg_color="#790028",corner_radius=10)
        self.frame_1.place(x=12,y=80)

        self.text_1 = CTkLabel(self.frame_1,text="Images",width=390,height= 25,fg_color="#790028",font=('Times',18))
        self.text_1.place(x=5,y=5)

        self.all = CTkCheckBox(self.frame_1,text="All",font=('Times',15),corner_radius=50,fg_color="#790028",height=25,checkbox_height=20,checkbox_width=20,onvalue='All',offvalue='None',command=lambda :self.select_all(self.all))

        self.img_frame = CTkScrollableFrame(self.frame_1,width=370,height=455,fg_color="#4F0018",corner_radius=10)
        self.img_frame.place(x=2,y=33)

        self.copy = CTkButton(self.Frame,width=120,height=32,text="Copy",anchor=W,font=('Times',16),compound=LEFT,image=self.img2,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6,command= self.copy_text)
        self.copy.place(x=760,y=40)

        self.clear = CTkButton(self.Frame,width=120,height=32,text="Clear",anchor=E,font=('Times',16),compound=RIGHT,image=self.img3,fg_color="#790028",border_width=0,hover_color="#4F0018",corner_radius=6,command= self.clear_text)
        self.clear.place(x=885,y=40)

        self.frame_2  = CTkFrame(self.Frame,width=320,height=510,fg_color="#790028",corner_radius=10)
        self.frame_2.place(x=720,y=80)

        self.text_2 = CTkLabel(self.frame_2,text="Text",width=310,height= 25,fg_color="#790028",font=('Times',18))
        self.text_2.place(x=5,y=5)

        self.lyr_frame = CTkFrame(self.frame_2,width=316,height=475,fg_color="#4F0018",corner_radius=10)
        self.lyr_frame.place(x=2,y=33)

        self.text_area = CTkTextbox(self.lyr_frame,width=311,height=465,font=('Times',19),wrap='word',border_spacing=0,fg_color="#4F0018",corner_radius=10)
        self.text_area.place(x=2,y=2)
        self.text_area.bind('<KeyRelease>',lambda event: self.check_textarea(event))

        self.conv = CTkButton(self.Frame,width=150,height=32,text="Convert (0)",font=('Times',16),compound=RIGHT,fg_color="#790028",border_width=0,hover_color="#4F0018",text_color_disabled="white",corner_radius=6,command=self.convert_img_to_text)
        self.conv.place(x=491,y=521)

        self.next = CTkButton(self.Frame,width=150,height=32,text="Next",font=('Times',16),compound=RIGHT,fg_color="#4F0018",state=DISABLED,border_width=0,hover_color="#4F0018",text_color_disabled="white",corner_radius=6)
        # self.next.place(x=491,y=558)

    def place(self):
        self.Frame.tkraise()
        self.Frame.place(x=46,y=0)

    def hide(self):
        self.Frame.place_forget()

    def copy_text(self):
        pc.copy(self.text_area.get(0.0,END))
        self.copy.configure(text="Copied")

    def clear_text(self):
        self.text_area.delete(0.0,END)
        self.next.configure(fg_color="#4F0018",state=DISABLED)
        
    def browse_file(self):
        self.file_location = filedialog.askopenfilenames(filetypes=[('PNG','.png'),('JPG','.jpg')]) 
        if self.file_location:
            for i in self.file_location:
                self.image = Image.open(i)
                self.add_image(self.image)

    def get_screenshot(self):
        self.image = self.Screenshot.create_window()

    def add_image(self,image):
        self.width,self.height = image.size
        
        if self.width > 340:
            self.perc = ((self.width-340)/self.width)*100

            self.width = 340
            self.height = ((100-self.perc)/100)*self.height

        img = CTkImage(image,size=(self.width,self.height))
        self.all_images.append(image)

        self.image_frame = CTkFrame(self.img_frame,width=340,height=self.height,fg_color="#4F0018",corner_radius=0)
        self.image_frame.grid(row=self.Row,column=0,pady=5,padx=5)

        self.image_label = CTkLabel(self.image_frame,image = img,text='')
        self.image_label.place(x=0,y=0)

        check = CTkCheckBox(self.img_frame,height=25,width=25,fg_color="#4F0018",checkbox_height=20,checkbox_width=20,corner_radius=50,text='',onvalue='on',offvalue='off')
        check.configure(command=lambda check=check,image=image: self.select_image(check,image))
        check.grid(row=self.Row,column=1,padx=0,)
        self.check_boxes.append(check)

        self.Row= self.Row + 1
        self.all.place(x=340,y=5)

    def select_all(self,button):
        if button.get() == "All":
            for i in self.check_boxes:
                i.select()

            for i in self.all_images:
                if i not in self.selected_images:
                    self.selected_images.append(i)

        elif button.get() == "None":
            for i in self.check_boxes:
                i.deselect()

            self.selected_images.clear()

        self.conv.configure(text=f"Convert ({len(self.selected_images)})")

    def select_image(self,button,image):
        if button.get() == 'on':
            self.selected_images.append(image)
        elif button.get() == 'off':
            self.selected_images.remove(image)

        self.conv.configure(text=f"Convert ({len(self.selected_images)})")

    def convert_img_to_text(self):
        if len(self.selected_images) > 0:
            for i in self.check_boxes:
                i.configure(state=DISABLED)

            self.all.configure(state=DISABLED)
            self.count = len(self.selected_images)
            self.conv.configure(fg_color="#4F0018",state=DISABLED)

            self.Image_converter.convert(self.selected_images,self.get_converted_text)

    def get_converted_text(self,text,status): 
        self.text_area.insert(END,text)
        self.text_area.insert(END,"\n")

        self.next.configure(fg_color="#790028",state=NORMAL)

        if status == "Done":
            self.count = self.count - 1

        self.conv.configure(fg_color="#4F0018",state=DISABLED,text=f"Convert ({str(self.count)})")

        if self.count == 0:
            self.selected_images.clear()
            for i in self.check_boxes:
                i.configure(state=NORMAL)
                i.deselect()

            self.all.configure(state=NORMAL)
            self.all.deselect()
            self.conv.configure(state=NORMAL,fg_color="#790028")

    def check_textarea(self,Event):
        if int(len(self.text_area.get(0.0,END))-1) > 0:
            self.next.configure(fg_color="#790028",state=NORMAL)
        else:
            self.next.configure(fg_color="#4F0018",state=DISABLED)


class Lyrics_Frame():
    def __init__(self,frame,app):
        self.master = frame
        self.App = app

        self.img0 = CTkImage(Image.open("Icons\\bold.png"),size=(20,20))
        self.img1 = CTkImage(Image.open("Icons\\italic.png"),size=(20,20))
        self.img2 = CTkImage(Image.open("Icons\\underline.png"),size=(20,20))
        self.img3 = CTkImage(Image.open("Icons\\strike.png"),size=(24,24))
        self.img4 = CTkImage(Image.open("Icons\\align-left.png"),size=(24,24))
        self.img5 = CTkImage(Image.open("Icons\\align-right.png"),size=(24,24))
        self.img6 = CTkImage(Image.open("Icons\\center-align.png"),size=(24,24))
        self.img7 = CTkImage(Image.open("Icons\\justify.png"),size=(24,24))

        self.current_font_size = 20
        self.current_font_type = "Times New Roman"
        self.alignment = ""

        self.align_buttons = []

        self.Frame = CTkFrame(self.master,width=1054,height=600,fg_color="#58001D",corner_radius=0)

        self.ribbon = CTkFrame(self.Frame,fg_color="#790028",width=1044,height=80,corner_radius=5)
        self.ribbon.place(x=4,y=5)

        self.font = CTkComboBox(self.ribbon,values=font.families(),fg_color=['#F9F9FA', '#343638'],font=('Times',15),border_width=0,command=self.change_font_type,corner_radius=0)
        self.font.place(x=8,y=5)
        self.font.set("Times New Roman")

        self.size = CTkEntry(self.ribbon,fg_color=['#F9F9FA', '#343638'],width=30,height=28,font=('Times',15),border_width=0,corner_radius=0)
        self.size.place(x=153,y=5)
        self.size.bind('<KeyRelease>',lambda event: self.change_font_size(event))
        self.size.insert(0,"12")

        self.bold = CTkButton(self.ribbon,height=35,width=40,text='',image=self.img0,fg_color="#790028",hover_color="#58001D",corner_radius=0)
        self.bold.place(x=8,y=40)

        self.italic = CTkButton(self.ribbon,height=35,width=40,text='',image=self.img1,fg_color="#790028",hover_color="#58001D",corner_radius=0)
        self.italic.place(x=53,y=40)

        self.underline = CTkButton(self.ribbon,height=35,width=40,text='',image=self.img2,fg_color="#790028",hover_color="#58001D",corner_radius=0)
        self.underline.place(x=98,y=40)

        self.strike = CTkButton(self.ribbon,height=35,width=40,text='',image=self.img3,fg_color="#790028",hover_color="#58001D",corner_radius=0)
        self.strike.place(x=143,y=40)

        self.sep = ttk.Separator(self.ribbon,orient=HORIZONTAL)
        self.sep.place(x=193,y=5,height=70,width=1)

        self.left = CTkButton(self.ribbon,height=35,width=40,text='',image=self.img4,fg_color="#790028",hover_color="#58001D",corner_radius=0,command=lambda: self.align_text(self.left,"left"))
        self.left.place(x=203,y=5)
        self.align_buttons.append(self.left)

        self.center = CTkButton(self.ribbon,height=35,width=40,text='',image=self.img6,fg_color="#790028",hover_color="#58001D",corner_radius=0,command=lambda: self.align_text(self.center,"center"))
        self.center.place(x=243,y=5)
        self.align_buttons.append(self.center)

        self.right = CTkButton(self.ribbon,height=35,width=40,text='',image=self.img5,fg_color="#790028",hover_color="#58001D",corner_radius=0,command=lambda: self.align_text(self.right,"right"))
        self.right.place(x=283,y=5)
        self.align_buttons.append(self.right)

        self.editor = CTkTextbox(self.Frame,width=600,height=480,fg_color='white',text_color='black',corner_radius=0,font=("Times",self.current_font_size))
        self.editor.place(x=50,y=100)
        self.editor.bind('<KeyRelease>',lambda event: self.adjust_align)

        self.editor.tag_add("All","1.0","end")

        self.center.invoke()

    def change_font_size(self,Event):
        try:
            if self.size.get() != "":
                size = int(self.size.get())
                self.current_font_size = size
                self.edit_font()

        except:
            self.size.delete(0,END)
            self.size.insert(0,f"{self.current_font_size}")

    def change_font_type(self,value):
        self.current_font_type = value
        self.edit_font()

    def edit_font(self):
        self.editor.configure(font=(self.current_font_type,self.current_font_size))

    def align_text(self,button,value):
        for i in self.align_buttons:
            if i == button:
                i.configure(fg_color="#58001D",state=DISABLED)
            else:
                i.configure(fg_color="#790028",state=NORMAL)

        self.alignment = value
    
    def adjust_align(self,Event):
        self.editor.tag_delete("All")
        self.editor.tag_add("All","1.0","end")
        self.editor.tag_config("All",justify=self.alignment)

    def place(self):
        self.Frame.tkraise()
        self.Frame.place(x=46,y=0)

    def hide(self):
        self.Frame.place_forget()
