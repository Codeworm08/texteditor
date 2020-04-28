'''
A basic text editor created using tkinter
Created on:28-04-2020
'''
from tkinter import filedialog
from tkinter import *
#Create the window
root = Tk()
root.geometry('1280x720')

#Create menubar
menub = Menu(root)

#Make the 'File' dropdown menu
filemenu = Menu(menub, tearoff=0)
filemenu.add_command(label = "New",command = lambda:newFile())
filemenu.add_command(label = "Open",command = lambda:openFile())
filemenu.add_command(label = "Save",command = lambda:saveFile())
filemenu.add_separator()
filemenu.add_command(label = "Exit",command = root.quit)
menub.add_cascade(label="File",menu=filemenu)

#Make the 'Edit' dropdown menu 
editmenu = Menu(menub, tearoff=0)
editmenu.add_command(label="Cut",command = lambda:deltext())
editmenu.add_command(label="Copy",command = lambda:copytext())
editmenu.add_command(label="Paste",command = lambda:paste())
menub.add_cascade(label="Edit", menu=editmenu)

'''
B = Button(root,text="Open",command = lambda:openFile())
B.pack()
'''
T = Text(root, height=1000, width=500)
T.pack()

def newFile():
  T.delete("1.0",END)

def saveFile():
  savef = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
  textsave = str(T.get("1.0",END))
  savef.write(textsave)
  savef.close()
  
def openFile():
  file =  filedialog.askopenfile(mode="r",title = "Select file",filetypes = (("Python files","*.py"),("Text files","*.txt"),("all files","*.*")))
  if file is not None:
    content = file.read()
    T.insert(END,content)
    
def deltext():
       text = T.get(SEL_FIRST, SEL_LAST)
       T.delete(SEL_FIRST, SEL_LAST)
       root.clipboard_clear()
       root.clipboard_append(text)
       
def copytext():
      copy = T.get(SEL_FIRST, SEL_LAST)
      root.clipboard_clear()
      root.clipboard_append(copy)
    
def paste():
    var =root.clipboard_get()
    T.insert("insert",var) 

    
root.config(menu=menub)
root.mainloop()
