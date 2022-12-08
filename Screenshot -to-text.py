import time
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageGrab, ImageTk
import easyocr
import pyperclip as pc

def trans():
    Win.wm_attributes("-alpha",0.5)

def click(event,frm):
    try:
        frm.delete(txt)
    except:
        pass
    
    global rect
    try:
        if frm.coords(rect)==[]:
            x = Win.winfo_pointerx()
            y = Win.winfo_pointery()-23

            rect= frm.create_rectangle(x, y,0,0,width=4)
            while True:
                Win.update()
                frm.coords(rect,x,y,Win.winfo_pointerx(),(Win.winfo_pointery()-23))    

    except:
        x = Win.winfo_pointerx()
        y = Win.winfo_pointery()-23

        rect= frm.create_rectangle(x, y,0,0,width=4)
        while True:
            Win.update()
            frm.coords(rect,x,y,Win.winfo_pointerx(),(Win.winfo_pointery()-23))

def destroy(event):
    try:
        canvas.delete(rect)
    except:
        pass

    try:
        canvas2.delete(rect)
    except:
        pass

def capture(frm):
    coordinates=frm.coords(rect)

    screenshot=ImageGrab.grab()
    global z
    nm="screen"+str(z)+".png"
    screenshot.save(nm,"PNG")
    screenshot.close()

    img=Image.open(nm)
    cropped=img.crop(coordinates)

    global nm2
    nm2="screen"+str(z)+"a"+".png"
    cropped.save(nm2,"PNG")
    cropped.close()

    open2img=Image.open(nm2)
    global lb
    lb= ImageTk.PhotoImage(open2img)

    z=z+1

def place():

    global name
    name="Image "+str(z)
    global label2
    label2=Label(frame2,image=lb,text=name,compound=BOTTOM,font=("Times 15 bold"),bg="#0754AB")
    label2.place(x=10,y=20)

def con2():
    Win.iconify()
    global Win2 
    Win2=Toplevel(bg="white")
    Win2.state("zoomed")
    Win2.wm_attributes("-alpha",0.5)
    Win2.bind("<Escape>",destroy)
    Win2.bind("<Return>",enter2)

    global canvas2
    canvas2=Canvas(Win2,height=800,width=1400,bg="white",cursor="plus")
    canvas2.bind("<Button-1>",lambda event:click(event,canvas2))
    canvas2.pack()

    cp.configure(text="Copy")

def enter(event):
    Win.unbind("<Escape>")
    Win.unbind("<Return>")

    try:
        coordinates=canvas.coords(rect)

        Win.iconify()
        time.sleep(1)

        capture(canvas)
        
        Win.wm_attributes("-alpha",1)
        Win.deiconify()
        Win.resizable(True,True)

        global frame2
        frame2=Frame(Win,height=800,width=1400,bg="#0754AB")
        frame2.place(x=0,y=2)

        place()

        global conv
        conv=Button(frame2,text="Convert",bd=0,font=("Times 15"),bg="#031F46",fg="white",command=con)
        conv.place(x=10,y=700,width=200)

        global convan
        convan=Button(frame2,text="Take more screenshots",bd=0,font=("Times 15"),bg="#031F46",fg="white",command=con2,state="disabled")
        convan.place(x=250,y=700,width=300)
        
        textlabel=Label(frame2,text="Text output should be below",bg="#0754AB",font=("Times 15"))
        textlabel.place(x=1000,y=4)

        global text
        text=Text(frame2,width=42,height=29,wrap=WORD,bg="#031F46",fg="white",font=("Times 15"),bd=0)
        text.place(x=900,y=35)

        global cp
        cp=Button(frame2,text="Copy",bd=0,font=("Times 15"),bg="#031F46",fg="white",command=copy)
        cp.place(x=900,y=700,width=140)

        clr=Button(frame2,text="Clear",bd=0,font=("Times 15"),bg="#031F46",fg="white",command=clear)
        clr.place(x=1184,y=700,width=140)

        global lbtxt
        lbtxt=Label(frame2,bg="#0754AB",font=("Times 16"))
        lbtxt.place(x=592,y=700)
    except:
        messagebox.showerror("Error","Ensure you have selected the area you want to capture")
        Win.deiconify()

def enter2(event):
    try:
        coordinates=canvas2.coords(rect)

        Win2.iconify()
        Win.iconify
        time.sleep(1)
        capture(canvas2)

        global name
        name="Image "+str(z)
        label2.configure(image=lb,text=name)
        Win2.destroy()
        Win.deiconify()

        conv.configure(state="normal")
        convan.configure(state="disabled")
        
    except:
        messagebox.showerror("Error","Ensure you have selected the area you want to capture")
        Win2.deiconify()

def con():
    conv.configure(state="disabled")
    
    global convert
    convert="Converting "+name+"..."
    lbtxt.configure(text=convert)

    global complete
    complete=name+" conversion is complete"

    Win.update()
    result = reader.readtext(nm2, paragraph=True ,detail= 0)
    for i in result:
        text.insert(END, i + "\n")

    text.insert(END,"\n")
    
    lbtxt.configure(text=complete)
    convan.configure(state="normal")

def clear():
    text.delete("1.0","end")

def copy():
    pc.copy(text.get("1.0","end"))
    cp.configure(text="Copied")

Win=Tk()
Win.title("Lyrics")
Win.state("zoomed")
Win.resizable(False,False)

Win.bind("<Escape>",destroy)
Win.bind("<Return>",enter)

z=0
p=0.0

frame=Frame(Win,bg="white",height=900,width=1600)
frame.place(x=0,y=0)

canvas=Canvas(frame,height=800,width=1400,bg="white",cursor="plus")
canvas.bind("<Button-1>",lambda event:click(event,canvas))
canvas.pack()

txt=canvas.create_text(680,50,text="Left click to select the area you want to capture after the screen becomes transparent.",font=("Times 20 bold"))

reader = easyocr.Reader(['en'])

Win.after(2000,trans)

mainloop()