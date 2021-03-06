import tkinter as tk0
import tkinter.ttk as ttk0
from tkinter.constants import DISABLED
from ttkthemes import ThemedStyle #This is in order to implement a certain theme. The colors, however, are manually created.
import re

"""
Note: you have to install ttkthemes using pip. Run this command in any shell (cmd, powershell, bash, etc):-
pip install ttkthemes
or
pip3 install ttkthemes
"""

#=================================================
#=================================================
#=================================================

"""
This is the root widget initialization. We imported tkinter as tk0 instead of importing all from tkinter to avoid any potential conflicts.
"""

root_or_win = tk0.Tk()
root_or_win.title("Aleph Node V1.0")
#root_or_win.iconbitmap("/home/omar/EngST/1st Year/2nd Sem/PHYS002/Project/Phys002-Project/Mainfiles/an.ico")
s=ThemedStyle(root_or_win)
s.theme_use('breeze')
root_or_win.configure(bg="#24292C")
#Instead of directly using the original window as a root window, I create a frame inside it that we will use as the root instead, so that we can control it, add padding, and more without affacting the main window.
root_win=tk0.Frame(root_or_win, bg="#24292C")
root_win.grid(column=0, row=0, columnspan=2, rowspan=7, padx=4, pady=4, sticky="nesw")
#Creating frames for the help and exit sections
helpsection=tk0.Frame(root_or_win, bg="#24292C")
aboutsection=tk0.Frame(root_or_win, bg="#24292C")
#Icon
try:
    root_or_win.iconphoto(True, tk0.PhotoImage(file='an.png'))
except:
    pass
#=================================================
#=================================================
#=================================================

"""
This is where we configure some stuff.
for example. by giving a weight of number 1 to the mentioned columns, we can
make them dynamically resizeable as the user changes the size of the window.
Here we configure both the main window (root_or_win), and the frame in which we are going to put everything in (root_win)
"""

root_or_win.columnconfigure(0, weight=1)
root_or_win.columnconfigure(1, weight=1)
root_or_win.rowconfigure(0, weight=1)
root_or_win.rowconfigure(1, weight=1)
root_or_win.rowconfigure(2, weight=1)
root_or_win.rowconfigure(3, weight=1)
root_or_win.rowconfigure(4, weight=1)
root_or_win.rowconfigure(5, weight=1)
root_or_win.rowconfigure(6, weight=1)

#Our WIndow configuration
root_win.columnconfigure(0, weight=1)
root_win.columnconfigure(1, weight=1)
root_win.rowconfigure(0, weight=1)
root_win.rowconfigure(1, weight=1)
root_win.rowconfigure(2, weight=1)
root_win.rowconfigure(3, weight=1)
root_win.rowconfigure(4, weight=1)
root_win.rowconfigure(5, weight=1)
root_win.rowconfigure(6, weight=1)

#Help and about
helpsection.columnconfigure(0, weight=1)
helpsection.columnconfigure(1, weight=1)
helpsection.rowconfigure(0, weight=1)
helpsection.rowconfigure(1, weight=1)
helpsection.rowconfigure(2, weight=1)
helpsection.rowconfigure(3, weight=1)
helpsection.rowconfigure(4, weight=1)
helpsection.rowconfigure(6, weight=1)

aboutsection.columnconfigure(0, weight=1)
aboutsection.columnconfigure(1, weight=1)
aboutsection.rowconfigure(0, weight=1)
aboutsection.rowconfigure(1, weight=1)
aboutsection.rowconfigure(2, weight=1)
aboutsection.rowconfigure(3, weight=1)
aboutsection.rowconfigure(4, weight=1)
aboutsection.rowconfigure(6, weight=1)



#=================================================
#=================================================
#=================================================

"""
This is where we define our functions. The ones that are related to our buttons, text inputs, and more. 
We defined them here since we have to define out functions first and THEN use them. This could be avoided using classes,
but since we are using a procedural approach, we can't do that as easily (if at all).
"""
#These are going to be some user-defined variables and the "previous answer" variable

def closeinput(message):
    inputstatus.insert(0, f"Status: {message}")
    inputstatus.configure(state="readonly")

def finalwrite(a0):
    try:
        if inputconth.get() != "":
            amatch=re.search("\/\*conth\*\/(.*)=(.*);", a0).group(2)
            a0=re.sub(amatch, f" {inputconth.get()} ", a0, 1)
        else:
            pass

        if inputsensh.get() != "":
            amatch=re.search("\/\*sensh\*\/(.*)=(.*);", a0).group(2)
            a0=re.sub(amatch, f" {inputsensh.get()} ", a0, 1)
        else:
            pass

        if inputmaxl.get() != "":
            amatch=re.search("\/\*maxl\*\/(.*)=(.*);", a0).group(2)
            a0=re.sub(amatch, f" {inputmaxl.get()} ", a0, 1)
        else:
            pass

        f1=open("WaterLevel.ino", "w")
        f1.write(a0)
        f1.close()
        
        closeinput("Success!")

    except:
        closeinput("Error: Unexpected error!")



def changevalue():
    """
    This function changes the values of the three user-defined variables.
    """
    inputstatus.configure(state="normal") #Make the input field statuus writable
    inputstatus.delete(0, tk0.END) #Delete what was previously in here
    try:
        f1=open("WaterLevel.ino", "r")
        a0=f1.read()
        f1.close()
        
        try:
            if inputconth.get() == "0":
                closeinput("Error: Container's height can't be 0!")
            elif inputmaxl.get() == "0":
                closeinput("Error: Max water level can't be 0!")
            elif type(eval(inputconth.get())) == float or type(eval(inputsensh.get())) == float or type(eval(inputmaxl.get())) == float:
                closeinput("Error: can't input decimals! Integars only!")
            else:
                float(inputconth.get())
                float(inputsensh.get())
                float(inputmaxl.get())
                finalwrite(a0)
        except:
            closeinput("Error: No charaters allowed!")

    except:
        closeinput("Error: File not found!")

    #=====Here it goes
    #=====

def gotohelp():
    root_win.grid_forget()
    root_or_win.geometry("980x420")
    helpsection.grid(column=0, row=0, columnspan=2, rowspan=7, padx=4, pady=4, sticky="nesw")

def gotoabout():
    root_win.grid_forget()
    root_or_win.geometry("980x420")
    aboutsection.grid(column=0, row=0, columnspan=2, rowspan=7, padx=4, pady=4, sticky="nesw")

def gotomain():
    try:
        aboutsection.grid_forget()
    except:
        pass
    try:
        helpsection.grid_forget()
    except:
        pass
    root_win.grid(column=0, row=0, columnspan=2, rowspan=7, padx=4, pady=4, sticky="nesw")


#=================================================
#=================================================
#=================================================

"""
This is where we define our buttons. text inputs, and more.
Each widget variable name has a descriptive name. so button-sin is for the sin button.
"""

#=====Input fields and buttons

"""
Note that we are defining frames here as well which act as containers
"""

#-----Main field: where the user enters the values and assigns them

framemain = tk0.Frame(root_win, bg="#24292C")

#Same as with root_win. But with this frame instead
framemain.columnconfigure(0, weight=1)
framemain.columnconfigure(1, weight=1)
framemain.rowconfigure(0, weight=1)
framemain.rowconfigure(1, weight=1)
framemain.rowconfigure(2, weight=1)
framemain.rowconfigure(3, weight=1)


#The buttons
buttonassign = tk0.Button(framemain, text="Assign Values"  , bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0,   command=changevalue)
buttonconth = tk0.Button(framemain, text="Container Depth:", state=DISABLED, bg="#343A3E", disabledforeground="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0) 
buttonsensh = tk0.Button(framemain, text="Sensor Distance:", state=DISABLED, bg="#343A3E", disabledforeground="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0) 
buttonmaxl = tk0.Button(framemain, text="Max Water Level:" , state=DISABLED, bg="#343A3E", disabledforeground="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0 ) 

#The entry fields
inputstatus = tk0.Entry(framemain, bg="#323938", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=30, state="readonly", readonlybackground="#323938") 
inputconth = tk0.Entry(framemain, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=30) 
inputsensh = tk0.Entry(framemain, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=30) 
inputmaxl = tk0.Entry(framemain, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=30) 

#Here we place our frame on a certain grid position and put our elements inside. We will be doing this several times from now on.
framemain.grid(row=0 ,column=0, rowspan=4, padx=2, pady=2, columnspan=2, sticky="nesw")

buttonassign.grid(row=0, column=0, padx=1, pady=1, sticky="nesw")
inputstatus .grid(row=0, column=1, padx=1, pady=1, sticky="nesw")

buttonconth .grid(row=1, column=0, padx=1, pady=1, sticky="nesw")
inputconth  .grid(row=1, column=1, padx=1, pady=1, sticky="nesw")

buttonsensh .grid(row=2, column=0, padx=1, pady=1, sticky="nesw")
inputsensh  .grid(row=2, column=1, padx=1, pady=1, sticky="nesw")

buttonmaxl  .grid(row=3, column=0, padx=1, pady=1, sticky="nesw")
inputmaxl   .grid(row=3, column=1, padx=1, pady=1, sticky="nesw")












#-----Exit frame
#Help, About, and Exit buttons and their frames
frameaccess=tk0.Frame(root_win ,bg="#24292C")
buttonhelp = tk0.Button(frameaccess, text="Help", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = gotohelp)
buttonabout = tk0.Button(frameaccess, text="About", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = gotoabout)
buttonexit = tk0.Button(frameaccess, text="Exit", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = root_or_win.destroy)

#Other frames
#Help
textofmainh="""This application is designed to set the values of the:-
1-Container's Height\n2-Sensor's Height\n3-The maximum water level

You simply type the value you want. And then you can upload the code to the arduino directly.

Do NOT tamper with the arduino (.ino) file!

Leave the arduino .ino file and the application in the same directory.

The application rejects any of the following as input:-
1-Characters.
2-Zeros in the Container and Max water level fields.
3-Decimals."""
buttonmainh = tk0.Button(helpsection, text="Main", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = gotomain)
labelh1 = tk0.Label(helpsection, text=textofmainh, bg="#323938", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0)





#About
textofmaina1="""Phys002 Project: Team AlephNode
===============================
This application is designed to set the values of the
1-Container's Height | 2-Sensor's Height | 3-The maximum water level

It is designed as a complementary GUI software to edit the mentioned
values for the arduino's code file.

This application was created by Team AlephNode of the Nile University
for their Physics-002 Project. The members are:-
1-Abdelrahman | 2-Marawan | 3-Mostafa | 4-Nadine | 5-Omar
For more info, go to github. Click on the button to copy the link."""

textofmaina2=tk0.StringVar(value="https://github.com/Omar-Sigma/Phys002-Project")

buttonmaina = tk0.Button(aboutsection, text="Main", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = gotomain)
labela1 = tk0.Label(aboutsection, text=textofmaina1, bg="#323938", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0)
buttongithub = tk0.Button(aboutsection, text="Github: ", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command=lambda : root_or_win.clipboard_append("https://github.com/Omar-Sigma/Phys002-Projects")) #This command copies the link to the clipboard

labela2 = tk0.Entry(aboutsection, textvariable=textofmaina2, bg="#323938", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=30, state="readonly", readonlybackground="#323938") 


#Placing them
frameaccess.grid(row=4, column=0, padx=2, pady=2, columnspan=2, rowspan=3, sticky="nesw")

frameaccess.rowconfigure(0, weight=1)
frameaccess.rowconfigure(1, weight=1)
frameaccess.rowconfigure(2, weight=1)
frameaccess.columnconfigure(0, weight=1)
frameaccess.columnconfigure(1, weight=1)

buttonhelp .grid(row=0, column=0, padx=2, pady=2, columnspan=2, sticky="nesw")    
buttonabout.grid(row=1, column=0, padx=2, pady=2, columnspan=2, sticky="nesw")    
buttonexit .grid(row=2, column=0, padx=2, pady=2, columnspan=2, sticky="nesw")    

#Other non-main frames
buttonmainh .grid(row=6, column=0, padx=2, pady=2, columnspan=2, sticky="nesw")    
labelh1     .grid(row=0, column=0, padx=2, pady=2, rowspan=5, columnspan=2, sticky="nesw")    



buttonmaina .grid(row=6, column=0, padx=2, pady=2, columnspan=2, sticky="nesw")    
labela1     .grid(row=0, column=0, padx=2, pady=2, rowspan=5, columnspan=2, sticky="nesw")    
buttongithub .grid(row=5, column=0, padx=2, pady=2, sticky="nesw")    
labela2     .grid(row=5, column=1, padx=2, pady=2, sticky="nesw")    






#=================================================
#=================================================
#=================================================

"""
This is where we finally start our application. So now, let's quickly explain what these lines mean.
the __name__ is a kind of variable that python assigns a value to depending on how the user uses this script.
so if the user uses it as a main script (a gui for example), the the value assigned is equal to "__main__". If not - such as when using the script as an import - another value is assigned.
This line helps us execute the main windows (the line inside the if block) if the user runs it as a gui/script, but not if it's imported from.
"""

#Starting the application
if __name__ == "__main__":
    root_or_win.mainloop()
