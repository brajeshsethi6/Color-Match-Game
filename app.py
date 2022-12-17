from tkinter import *
from tkinter import messagebox
import random

master = Tk()
master.title("The Color Game")
master.iconbitmap(False,"colors-icon.ico")

global counter
counter = 0

def Score():
    global counter
    counter += 1
    print(counter)


global accScore
accScore = 0

def AccScore(pass_acr_scr):
    global accScore
    global total 
    accScore += pass_acr_scr
    print("Total Score ",accScore)


def main():
    print("-----------------------")
    label = Label(
        text="",
        fg="white",
        bg="black",
        width=40,
        height=10
    )
    label.grid(row=2,column=0)

    r=random.randint(0,225)
    g=random.randint(0,225)
    b=random.randint(0,225)

    print(r,g,b)

    color_q='#%02x%02x%02x' % (r, g, b)

    label_qus = Label(
        text="",
        fg="white",
        bg=color_q,
        width=40,
        height=2
    )
    label_qus.grid(row=0,column=0)

    def my_upd(v):
        color_c='#%02x%02x%02x' % (sc1.get(), sc2.get(), sc3.get())
        # btn1.config(bg=color_c)  # Updating background colour of button
        # btn1.config(text=color_c)# Updating text of the button 
        label.config(bg=color_c)

    # seekbar 
    sc1 = Scale(master, from_=0, to=255, bg='red',orient=HORIZONTAL, length=255,command=my_upd)
    sc1.grid(row=5,column=0)

    sc2 = Scale(master, from_=0, to=255,bg='green', orient=HORIZONTAL, length=255,command=my_upd)
    sc2.grid(row=6,column=0)

    sc3 = Scale(master, from_=0, to=255,bg='blue', orient=HORIZONTAL, length=255,command=my_upd)
    sc3.grid(row=7,column=0)

    UrScrL = Label(
        text="Your Score",
        width=40,
        height=2
    )
    UrScrL.grid(row=10,column=0)

    UrScr = Label(
        font=("Helvetica", 14),
        text=counter
    )
    UrScr.grid(row=11,column=0)

    def verify():
        r_result = abs(r-int(sc1.get()))
        g_result = abs(g-int(sc2.get()))
        b_result = abs(b-int(sc3.get()))
#accuracy 
        acc_list =["Red: ",r_result,"Green: ",g_result,"Blue: ",b_result]
        sum = r_result+g_result+b_result
        acc_scr= 90-sum
        print("the acc score ",acc_scr)
        
        print("The Accuracy" , r_result,g_result,b_result)
        print(sc1.get(),sc2.get(),sc3.get())
        
        if (r_result<=30 and g_result<=30 and b_result <=30):
            messagebox.showinfo("Matched! acuuracy is",acc_list)            
            AccScore(acc_scr)
            Score()
            #print("c test",counter)
            main()
            if (counter==5):
                messagebox.showinfo("Your Score",accScore)
                master.quit()
        else:
            messagebox.showinfo("Message","Not Matched")
        
    btn1=Button(master,text="Done",font=('calibre',10,'bold'),width=25,height=2,command = verify)
    btn1.grid(row=9,column=0)

    
    TotalAccScr = Label(
        font=("Helvetica", 24),
        text=accScore,
        fg="red"
    )
    TotalAccScr.grid(row=12,column=0)

main()
master.mainloop()