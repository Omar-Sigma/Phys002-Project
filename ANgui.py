import tkinter as tk0
import tkinter.ttk as ttk0
from tkinter.constants import DISABLED
from ttkthemes import ThemedStyle #This is in order to implement a certain theme. The colors, however, are manually created.

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
root_or_win.title("Test")
s=ThemedStyle(root_or_win)
s.theme_use('breeze')
root_or_win.configure(bg="#24292C")
#Instead of directly using the original window as a root window, I create a frame inside it that we will use as the root instead, so that we can control it, add padding, and more without affacting the main window.
root_win=tk0.Frame(root_or_win, bg="#24292C")
root_win.grid(column=0, row=0, columnspan=2, rowspan=7, padx=4, pady=4, sticky="nesw")
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

#=================================================
#=================================================
#=================================================

"""
This is where we define our functions. The ones that are related to our buttons, text inputs, and more. 
We defined them here since we have to define out functions first and THEN use them. This could be avoided using classes,
but since we are using a procedural approach, we can't do that as easily (if at all).
"""
#These are going to be some user-defined variables and the "previous answer" variable

def changevalue():
    """
    This function appends the values entered by the user to three files.
    This should be later changed to affect the variables in the arduino file.
    """
    inputstatus.configure(state="normal") #Make the input field statuus writable
    inputstatus.delete(0, tk0.END) #Delete what was previously in here
    
    reqfile1=open("conth.txtcon", "w") #Create and open these files
    reqfile2=open("sensh.txtcon", "w") 
    reqfile3=open("maxl.txtcon", "w") 
    
    try:
        reqfile1.write(f"{inputconth.get()}") #Put the value in the file
        reqfile2.write(f"{inputsensh.get()}")
        reqfile3.write(f"{inputmaxl.get()}")
        inputstatus.insert(0, "Status: Success!") #Output the status of the operation
        inputstatus.configure(state="readonly") #Change it back to read only
    except:
        inputstatus.insert(0, "Status: Error!")
        inputstatus.configure(state="readonly")

    
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
buttonconth = tk0.Button(framemain, text="Sensor Distance:", state=DISABLED, bg="#343A3E", disabledforeground="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0) 
buttonsensh = tk0.Button(framemain, text="Container Depth:", state=DISABLED, bg="#343A3E", disabledforeground="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0) 
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
buttonhelp = tk0.Button(frameaccess, text="Help", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0)
buttonabout = tk0.Button(frameaccess, text="About", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0)
buttonexit = tk0.Button(frameaccess, text="Exit", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = root_or_win.destroy)

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
