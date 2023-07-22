from tkinter import *
import pygame
pygame.mixer.init()

root = Tk()
root.title("Arc Timer LITE")
iconwindow=PhotoImage(file="icon.png")
root.iconphoto(False,iconwindow)

sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()

root.overrideredirect(1)
root.geometry(f"1000x500+{0}+{0}")
#root.state("zoomed")
root.config(bg="white")

#global nmin
#global nsec


#Define GUI objects
style=Label(root,bg="#2F4F4F",padx=680,pady =20)
style.place(x=0,y=730)
playing=PhotoImage(file="pause.png")
paused=PhotoImage(file="play.png")
colour=PhotoImage(file="color.png")
fontimg=PhotoImage(file="fontimg.png")
skipbreak=PhotoImage(file="skip break.png")
Reset=PhotoImage(file="reset.png")
Start=PhotoImage(file="start.png")
Info=PhotoImage(file="info.png")

space=Label(root,padx=220,pady=350,bg="white")
space.grid(row=0,column=0)


secdis=Label(root,text="S",fg= "black",bg="white",font=("Roboto", 150)) # second display
mindis=Label(root,text="M",fg="black",bg="white",font=("Roboto", 150))# minute display



sep=Label(root,text=" : ",fg= "grey",bg="white",anchor="center",font=("Arial", 70))        # seperator display


brtime=Label(root,text="",bg="white",font=("Roboto",50))                 #Break time text display


pause_sec= Label(root,text="Eroor Sec",fg= "grey",bg="white",font=("Arial", 90))
pause_min= Label(root,text="Eroor Min",fg= "grey",bg="white",font=("Arial", 90))


# Pause button code
print(secdis["font"])

print("pause need a change")






def pause():
    global count
    count +=1
    global Save_Passcheck
    global passcheck
    global  Save_reload
    global reload
    if count%2!=0:
        Save_Passcheck=passcheck
        Save_reload=reload
        x=secdis["text"]
        y=mindis["text"]
        if x=="00":
            x=0
        if y=="00":
            y=0
        pygame.mixer.music.stop()
        Passbut.config(image=paused)
        secdis.grid_forget()
        mindis.grid_forget()
        pause_sec.config(font=secdis["font"])
        pause_min.config(font=secdis["font"])
        pause_sec.config(text=x)
        pause_min.config(text=y)
        pause_sec.grid(row=0,column=3)
        pause_min.grid(row=0,column=1)
        passcheck="Freeze"
        reload="Freeze"
    if count%2==0:
        passcheck = Save_Passcheck
        reload = Save_reload
        secdis.config(text="S")
        mindis.config(text="M")
        Passbut.config(image=playing)
        global nsec
        nsec=pause_sec["text"]          
        global nmin
        nmin=pause_min["text"]
        pause_sec.grid_forget()
        secdis.grid(row=0,column=3)
        pause_min.grid_forget()
        mindis.grid(row=0,column=1)
global count
count=0

global Passbut 
Passbut=Button(root,image=playing,command=pause,bg="white",borderwidth=0)


    


#Minute code

def minu():
    global nmin
    mindis.config(text=nmin)
    if secdis["text"]==0:
        nmin=nmin-1
        mindis.config(text=nmin)
                       
    if mindis["text"] in range(1,10):
        pmin=str(mindis["text"] )
        mindis.config(text="0"+pmin)

    root.after(1000,minu)
     # reschedule event in 1 seconds
    if nmin <=0:
        mindis.config(text="00")
root.after(1000,minu)


#Seconds code

def sec():
    global nsec
    if nsec!=1000:
            secdis.config(text=nsec)
            nsec=nsec-1
            secdis.config(text=nsec)
            root.after(1000,sec)
    if secdis["text"]<=0 and mindis["text"]=="00":
        secdis.config(text="00")
        global reload
        if reload != "Freeze":
            reload+=1
            if reload %2!=0:
                breaktime()
            if reload %2==0:
                brtime.place_forget()
                global Val_min
                global Val_sec
                global nmin
                nmin=int(Val_min)
                nsec=int(Val_sec)
    if  nsec in range(1,10):
        psec=str(nsec)
        secdis.config(text="0"+psec)           
    if nsec<=0  and secdis["text"]!="00":
        nsec=60   
root.after(1000,sec)
global reload
reload=0




# break time code
def breaktime():
    global passcheck
    global count
    global Val_min
    if passcheck!="Freeze":
        if count%2==0:
            passcheck +=1
            if passcheck==3:
                brtime.place(x=380,y=110)
                global nmin
                global nsec
                newmin=int(Val_min)
                nmin= 2*(int(newmin/5))
                newsec=int(Val_sec)
                nsec=8+(2*(int(newsec/5)))
                brtime.config(text="B  r  e  a  k     T  i  m  e")
                pygame.mixer.music.load("alarm.wav")
                pygame.mixer.music.play(loops=1)
                print(nmin)
            if passcheck==1 or passcheck == 2:
                brtime.place(x=380,y=110)
                newmin=int(Val_min)
                nmin= int(newmin/5)
                newsec=int(Val_sec)
                nsec=8+(int(newsec/5))
                brtime.config(text="B  r  e  a  k     T  i  m  e")
               # pygame.mixer.music.load("alarm.wav")
                #pygame.mixer.music.play(loops=1)
global passcheck
passcheck=0


def Alert():
    if brtime["text"]=="B  r  e  a  k     T  i  m  e":
        if mindis["text"]=="00" and  secdis["text"]=="05":
            brtime.config(text="Break  Time  Ends  In")
            pygame.mixer.music.load("reload.wav")
            pygame.mixer.music.play(loops=1)
    root.after(1000,Alert)
root.after(1000,Alert)
            


#skip break

def SkipBreak():
    global passcheck
    
    if passcheck!=0 and count%2==0:
        pygame.mixer.music.stop()
        global Val_sec
        global nsec
        nsec=Val_sec
        global Val_min
        global nmin
        nmin=Val_min
skip_break= Button(root,bg="white",image=skipbreak,command=SkipBreak,borderwidth=0)


# colour change code

def ChangeColor():
    global color
    color+=1
     #green
    if color==1:
        mindis.config(fg="#2F4F4F")
        secdis.config(fg="#2F4F4F")     #lavender
    if color==2:
        mindis.config(fg="#00FFFF")     #blue
        secdis.config(fg="#00FFFF")
    if color==3:
        mindis.config(fg="#1C1C1E")    #black and red
        secdis.config(fg="#B22B27")
    if color==4:
        mindis.config(fg="#2E8B57")
        secdis.config(fg="#2E8B57")
    if color==5:
        mindis.config(fg="black")
        secdis.config(fg="black")
        color=0
color=0

color_change=Button(root,image=colour,bg="white",command=ChangeColor,borderwidth=0)



# Font change code

def Changefont():
    global font
    font+=1
    if font==1:
        mindis.config(font=("lcd",115))
        secdis.config(font=("lcd",115))
    if font==2:
        mindis.config(font=("Big Shoulders Stencil Display Black ExtraBold",160))
        secdis.config(font=("Big Shoulders Stencil Display Black",160))
    if font==3:
        mindis.config(font=("Nova Square",130))
        secdis.config(font=("Nova Square",130))
    if font==4:
        mindis.config(font=("Roboto Thin",150))
        secdis.config(font=("Roboto Thin",150))
        font=0
        
                                           

font_change=Button(root,image=fontimg,bg="white",borderwidth=0,command=Changefont)
  
font=0




nmin=1000
nsec=10


#WWWWWWWWWWWWWWWWWWAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRNNNNNNNNNIIIIIIIINNNNG


       

#Create Entry Widgets 

esec = StringVar()
sec_entry=Entry(root,textvariable=esec,width=2,font=("Roboto Thin",150),borderwidth=0)

def sec_write(*args):                     # limit sec entry
    global esec
    global Val_sec
    Val_sec = esec.get()
    Str_sec=str(Val_sec)
    if len(Val_sec) > 2:
        esec.set(Str_sec[:1])
esec.trace_variable("w", sec_write)
global Val_sec
print(esec.get())

def some_callback(event):             # "s" delete on click
    sec_entry.delete(0, "end")
    return None

sec_entry.bind("<Button-1>", some_callback)
esec.set("0")
sec_entry.insert(0,"0")
sec_entry.grid(row=0,column=3)



sep.grid(row=0,column=2)



mins= StringVar()
min_entry=Entry(root,textvariable = mins,width=2,font=("Roboto Thin",150),borderwidth=0)
max_len=2

def on_write(*args):                          # limit min entry
    global mins
    global Val_min
    Val_min = mins.get()
    print(Val_min)
    Str_min=str(Val_min)
    if len(Str_min) > 2:
        mins.set(Str_min[:1])
mins.trace_variable("w", on_write)
min_entry.grid(row=0,column=1)
mins.set("0")

def some_callback(event):        # "M" delete on click
    min_entry.delete(0, "end")
    return None
min_entry.bind("<Button-1>", some_callback)
mins.set("0")
min_entry.insert(0,"0")



page=Label(root,text="Enter   Time   for   One   Session",fg="#2F4F4F",bg="white",font=("Roboto", 35))
page.place(x=380,y=80)

warning=Label(root,text="",fg="red",bg="white",font=("Nova square", 14))
warning.place(x=520, y=200)
def transfer():
    global Val_min
    global Val_sec
    if Val_sec=="00" or Val_sec=="":
              Val_sec="1"
    if  int(Val_min) not in range(15,60) or int(Val_sec) not in range(0,60):
        if int(Val_min) in range(0,15):
            warning.config(text="Minimum time for a session is 15 minutes")
        if int(Val_min) not in range(0,60):
            warning.config(text="Make sure you have entered a Valid time")
    if  int(Val_min) in range(15,60) and int(Val_sec) in range(0,60):
        warning.config(text="")
        sec_entry.grid_forget()
        min_entry.grid_forget()
        page.place_forget()
        start.place_forget()
        mindis.config(text="M")
        secdis.config(text="S")
        global nmin
        nmin=0
        nmin=int(Val_min)
        global nsec
        nsec=int(Val_sec)
        mindis.grid(row=0,column=1)
        secdis.grid(row=0,column=3)
        sep.grid(row=0,column=2)
        resetbut.place(x=790,y=35)
        font_change.place(x=880,y=35)
        color_change.place(x=480,y=35)
        Passbut.place(x=690,y=30)
        skip_break.place(x=580,y=35)


start=Button(root,image=Start,bg="white",borderwidth=0,command=transfer)
start.place(x=665,y=480)


def reset():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("ding.mp3")
    pygame.mixer.music.play(loops=1)
    secdis.grid_forget()
    mindis.grid_forget()
    Passbut.place_forget()
    skip_break.place_forget()
    color_change.place_forget()
    font_change.place_forget()
    resetbut.place_forget()
    sec_entry.grid(row=0,column=3)
    min_entry.grid(row=0,column=1)
    start.place(x=665,y=480)
    
    
resetbut=Button(root,image=Reset,command=reset,bg="white",borderwidth=0)

def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("Info")
    pop.config(bg="white")
    #pop.geometry("")
    global me
    me = PhotoImage(file="credits.png")
    credit=Label(pop,image=me,bg="white")
    credit.pack()

info=Button(root,image=Info,bg ="white",bd=0,command=clicker)
info.place(x=1300,y=670)
    

def exito():
    root.destroy()
Exito= Button(root,text="exit",command=exito)
Exito.place(x=20,y=20)
    
root.mainloop()    
        
        
                   
        

