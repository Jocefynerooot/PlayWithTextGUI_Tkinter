from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


class PlayWithText:
    def capitalizeEachWord(self, text):
        textr = text.split(" ")
        returnText = ""
        for word in textr:
            returnText += word.capitalize() + " "
        return returnText

    def newFile(self):
        if len(userTextResult.get(1.0, END) != len(userText.get(1.0, END))):
            newVal = str(userText.get(1.0, End)).replace(
                str(userTextResult.get(1.0, END)), "")
            userTextResult.delete(1.0, END)
            userText.delete(1.0, END)

    def openFile(self):
        global file
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - PlayWithText")
            userText.delete(1.0, " - PlayWithText")
            f = open(file, 'r')
            userText.insert(1.0, f.read())
            userTextResult.delete(1.0, END)
            f.close()

    def saveFile(self):
        global file
        if file == None:
            if file == "":
                file = None
            if len(userTextResult.get(1.0, END)) > 1:
                file = asksaveasfilename(initialfile="untitled.txt",
                                         defaultextension=".txt",
                                         filetypes=[("All Files", "*.*"),
                                                    ("Text Documents", "*.txt")
                                                    ])
                f = open(file, "w")
                f.write(userTextResult.get(1.0, END))
                f.close()
                root.title(os.path.basename(file) + " - PlayWithText")
            else:
                msg = tmsg.askokcancel(
                    title="Result Box is Empty",
                    message=
                    "Result box is empty do you want to save your original content"
                )
                if msg == True:
                    file = asksaveasfilename(initialfile="untitled.txt",
                                             defaultextension=".txt",
                                             filetypes=[("All Files", "*.*"),
                                                        ("Text Documents",
                                                         "*.txt")])
                    f = open(file, "w")
                    f.write(userTextResult.get(1.0, END))
                    f.close()
                    root.title(os.path.basename(file) + " - PlayWithText")
        else:
            f = open(file, "w")
            f.write(userTextResult.get(1.0, END))
            f.close()

    def cut(self):
        userText.event_generate("<<Cut>>")

    def copy(self):
        userText.event_generate("<<Copy>>")

    def paste(self):
        userText.event_generate("<<Paste>>")

    def undo(self):
        userText.event_generate("<<Undo>>")

    def redo(self):
        userText.event_generate("<<Redo>>")

    def help(self):
        tmsg.showinfo(
            "You can use this software for manipulating text in between your work sometimes you have to manipulate text like convert all text into lowercase or uppercase etc and you can do this manually and you also know it is a big headech to you can use this app to do thse things perfetly and in a good manner. Thanks for using my app"
        )

    def click(self, event):
        pass

    # Functions For Themes
    def shiftMode(self, event):
        mode = event.widget.cget('text')
        if mode == "Enable Relax Mode":
            self.theme(bgColor="#3b2664",
                       textColor="white",
                       titleColor="white",
                       textAreaColor="#664a9d")
        else:
            self.theme(bgColor="white",
                       textColor="black",
                       titleColor="#3e1d7e",
                       textAreaColor="white")

    def theme(self,
              bgColor="white",
              textColor="black",
              titleColor="#3b2664",
              textAreaColor="black"):
        root.configure(background=f"{bgColor}")
        heading.configure(background=f"{bgColor}", fg=f"{titleColor}")
        modeBtnsFrame.config(bg=f"{bgColor}")
        screensFrame.config(bg=f"{bgColor}")
        userText.configure(background=textAreaColor, fg=textColor)
        userTextResult.configure(background=textAreaColor, fg=textColor)
        buttonsFrame.config(bg=bgColor)

    def lightTheme(self):
        pass

    def darkTheme(self):
        pass

    def redTheme(self):
        pass

    def purpleTheme(self):
        pass


if __name__ == "__main__":
    file = None
    playWithText = PlayWithText()
    # Gui Starts Here
    root = Tk()
    root.title("PlayWithText - Jocefyneroot")
    root.geometry("830x700")
    root.minsize(500, 400)

    heading = Label(root,
                    text="Welcome to Play With Text",
                    font="sans 15 bold",
                    fg="#3e1d7e")
    heading.pack(pady=5)

    modeBtnsFrame = Frame(root)
    modeBtnsFrame.pack()

    screensFrame = Frame(root)
    screensFrame.pack()

    buttonsFrame = Frame(root)
    buttonsFrame.pack()

    # Text Areas Here
    userText = Text(screensFrame, font="lucida 14", width=35, height=15)
    userText.pack(padx=10, side=LEFT)

    userTextResult = Text(screensFrame, font="lucida 14", width=35, height=15)
    userTextResult.pack(padx=10, side=LEFT)

    modeBtns = ["Enable Relax Mode", "Enable Light Mode"]
    for btn in modeBtns:
        btnColor = "#656572"
        modeBtn = Button(modeBtnsFrame,
                         text=f"{btn}",
                         font="lucida 10 bold",
                         bg=f"{btnColor}",
                         fg="white")
        modeBtn.pack(pady=15, padx=10, side=LEFT)
        modeBtn.bind("<Button-1>", playWithText.shiftMode)

    allBtns = [
        "Capitalize", "Upper Case", "Lower Case", "Cap Each Word", "Copy",
        "Cut", "Paste", "Save", "Open", "Delete"
    ]
    for btn in allBtns:
        btnColor = "#656572"
        modeBtn = Button(buttonsFrame,
                         text=f"{btn}",
                         font="lucida 10 bold",
                         bg=f"{btnColor}",
                         fg="white")
        modeBtn.pack(pady=15, padx=10, side=LEFT)

    # Menu Bar
    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=playWithText.newFile)
    fileMenu.add_command(label="Open", command=playWithText.openFile)
    fileMenu.add_command(label="Save", command=playWithText.saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit")

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Copy")
    editMenu.add_command(label="Cut")
    editMenu.add_command(label="Paste")
    editMenu.add_separator()
    editMenu.add_command(label="Undo")
    editMenu.add_command(label="Redo")

    themeMenu = Menu(menuBar, tearoff=0)
    themeMenu.add_command(label="Light Theme")
    themeMenu.add_command(label="Dark Theme")
    themeMenu.add_command(label="Red Theme")
    themeMenu.add_command(label="Purple Theme")

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="How To Use")

    menuBar.add_cascade(label="File", menu=fileMenu)
    menuBar.add_cascade(label="Edit", menu=editMenu)
    menuBar.add_cascade(label="Theme", menu=themeMenu)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menuBar)

    root.mainloop()