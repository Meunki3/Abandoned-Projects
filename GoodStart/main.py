import sys
import os
import platform
import time
import psutil
import platform
import customtkinter as ctr 
import subprocess


def liveCpu():
    global lablTwo
    global count
    global lablTwo
    cpuPercent = psutil.cpu_percent()
    lablTwo.configure(text = "Cpu: " + str(cpuPercent) + " %")
    lablTwo.after(2000, liveCpu)

processOr = platform.processor()


def dialog():
    dialogPath = ctr.CTkInputDialog(text='Software Location', title='test')
    softpath=dialogPath.get_input()
    return softpath


def extern():
    subprocess.Popen([softpath])
    

oldXPos = 18
oldYPos = 10
bCount = 0

def addApp():
    global oldXPos
    global oldYPos
    global bCount
    bCount += 1 
    if bCount > 1 :
        oldYPos += 70
    elif bCount < 1:
        oldYPos += 10
        
    appFrame = ctr.CTkButton(master=fram2, width=284, height=52, cursor='hand2', command=dialog)
    appFrame.place(x=oldXPos, y=oldYPos)
    appFrame.configure(command=extern())



    

ctr.set_appearance_mode("dark")
ctr.set_default_color_theme("blue")

root = ctr.CTk()
root.geometry("350x600+1500+400")
root.title("Good Start")

lablTwo = ctr.CTkLabel(root, text=liveCpu, font=('', 16))
lablTwo.place(x=13,y=561)

#PcInfo
frame = ctr.CTkFrame(master=root, width=325, height=125)
frame.place(x=13, y=19)

frmGrp = ctr.CTkFrame(master=frame, width=313, height=78, fg_color='transparent')
frmGrp.place(x=6,y=10)


lablThre = ctr.CTkLabel(frame, text= "Processor: " + processOr, font=('', 10.5), fg_color='transparent')
lablThre.place(x=3,y=97)

###APP LISTS

fram2 = ctr.CTkFrame(master=root, width=324,height=364,)
fram2.place(x=13, y=158)


addButton = ctr.CTkButton(master=root, width=50, height=50, corner_radius=150, text="Add App", hover=True, cursor='hand2', command=addApp)
addButton.place(x=237,y=540)


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu = ctr.CTkOptionMenu(fram2, values=["option 1", "option 2"],
                                         command=optionmenu_callback)
optionmenu.set("option 2")


liveCpu()
root.mainloop()



